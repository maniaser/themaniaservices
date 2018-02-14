
#
#      Copyright (C) 2015 Mikey1234
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
#  This code is a derivative of the YouTube plugin for XBMC and associated works
#  released under the terms of the GNU General Public License as published by
#  the Free Software Foundation; version 3


import re,xbmc
import requests
from types import *



def getNested(s, delim=("(", ")")):
        level = 0
        pos = 0
        for c in s:
                pos+=1
                if c == delim[0]:
                        level +=1
                elif c == delim[1]:
                        level -=1
                if level == -1: 
                        return pos-1
        xbmc.log("Couldn't find matching - level ", level)
        return s
indent = -1
def solveEquation(q):
        global indent
        indent +=1
        pos = 0
        res = 0
        stringify = False
        if q[0] == "!":
                stringify = True
        while pos < len(q):
                if q[pos] == "(":
                        nested = getNested(q[pos+1:len(q)])
                        nres = solveEquation(q[pos+1:pos+1+nested])
                        if type(nres) is StringType and type(res) is not StringType :
                                res = str(res)+nres
                        elif type(res) == StringType and type(nres) is IntType:
                                res = res + str(nres)
                        else:
                                res +=nres
                        pos+=nested+1
                elif q[pos] == ")":
                        pass
                        pos+=1
                elif q[pos:pos+4] == "!+[]":
                        res+=1
                        pos+=4
                elif q[pos:pos+5] == "+!![]":
                        res+=1
                        pos+=5
                elif q[pos:pos+3] == "+[]":
                        pos+=3
                elif q[pos:pos+2] == "+(":
                        pos+=1
                # we dont care about whitespaces
                elif q[pos] == " ": 
                        pos+=1
                elif q[pos] == "\t":
                        pos+=1
                else: 
                        xbmc.log('\t'*indent, "Unknown", q[pos:pos+6])
                        break
        
        indent -=1
        if stringify:
                return str(res)
        return res

def solve(url,cookie_file,dp):
        UA = 'XBMC'
        solverregex = re.compile('var s,t,o,p,b,r,e,a,k,i,n,g,f, (.+?)={"(.+?)":(.+?)};.+challenge-form\'\);.*?\n.*?;(.*?);a\.value',  re.DOTALL)
        vcregex = re.compile('<input type="hidden" name="jschl_vc" value="([^"]+)"/>')
        headers={'User-Agent' : UA,'Referer':url}       
        dp.update(0,"CloudFlare.... ", "Requesting Challenge....")
        request = requests.get(url,headers=headers).content
        
        passv = re.compile('<input type="hidden" name="pass" value="([^"]+)"/>').findall(request)[0]
        res = solverregex.findall(request)
        if len(res) == 0:
                xbmc.log("Couldn't find answer script - No cloudflare check?")
                return False
        res=res[0]
        vc = vcregex.findall(request)
        if len(vc)==0:
                xbmc.log("Couldn't find vc input - No cloudflare check?")
                return False
        vc = vc[0]
        
        varname = (res[0], res[1])
        solved = int(solveEquation(res[2].rstrip()))
        dp.update(10,"CloudFlare.... ", "Solved: " +str(solved))
        xbmc.log("Initial value: "+ str(res[2]) +"Solved: " +str(solved))
        for extra in res[3].split(";"):
                extra = extra.rstrip()
                if extra[:len('.'.join(varname))] != '.'.join(varname):
                        xbmc.log("Extra does not start with varname (", extra, ")")
                else:
                        extra = extra[len('.'.join(varname)):]
                if extra[:2] == "+=":
                        solved += int(solveEquation(extra[2:]))
                elif extra[:2] == "-=":
                        solved -= int(solveEquation(extra[2:]))
                elif extra[:2] == "*=":
                        solved *= int(solveEquation(extra[2:]))
                elif extra[:2] == "/=":
                        solved /= int(solveEquation(extra[2:]))
                else:
                        xbmc.log("Unknown modifier"+ str(extra))
        xbmc.log("Solved value: ", solved)

        http=url.split('//')[0]
        domain1=url.split('//')[1]
        domain=domain1.split('/')[0]
        solved += len(domain)
        xbmc.log("With domain length"+str(solved))
        dp.update(20,"CloudFlare.... ", "With domain length "+str(solved))
        import net
        net = net.Net()
        
 
        import time

        n=0
        while True:
            n+=1
            PercentUpdate=(n*10)+20
            time.sleep(1.25)
            dp.update(PercentUpdate,"CloudFlare if you get an error keep trying IT WILL WORK!!! ", "Sleeping For "+str(n)+" Seconds....")
            if n==7:
                break
        
        final = net.http_POST(http+"//"+domain+"/cdn-cgi/l/chk_jschl?jschl_vc={0}&pass={1}&jschl_answer={2}".format(vc,passv, solved),'',headers=headers)
        dp.update(90,"CloudFlare.... ", "Posting Answers....")
        net.save_cookies(xbmc.translatePath(cookie_file))
            

                

             
        return final.content

        
