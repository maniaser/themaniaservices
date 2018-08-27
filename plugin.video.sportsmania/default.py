import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os
import cloudflare
import datetime
import time
import net

from threading import Timer
import json

PLUGIN='plugin.video.sportsmania'
ADDON = xbmcaddon.Addon(id=PLUGIN)
SETTINGS = xbmc.translatePath(os.path.join(ADDON.getAddonInfo('profile'),'settings.xml'))
image='http://xunitytalk.com/stvb/'
MEDIA_URL = 'special://home/addons/{0}/resources/'.format('plugin.video.sportsmania')
auth=ADDON.getSetting('authtoken')
ontapp1=int(ADDON.getSetting('ontapp_id_1'))
ontapp2=int(ADDON.getSetting('ontapp_id_2'))

USER='[COLOR yellow]'+ADDON.getSetting('snusername')+'[/COLOR]'
updateid= int(ADDON.getSetting('id'))
THESITE='sportsmania.rocks'

 
UA='XBMC'

net=net.Net()

STVBINI = os.path.join(ADDON.getAddonInfo('path'), 'resources', 'sportsmania.ini')

try:
   filename = 'sportsmania.ini' 
   import xbmcvfs
   ottv = xbmcaddon.Addon('script.tvguidedixie')
   path = ottv.getAddonInfo('profile')
   file = os.path.join(path, 'ini', filename)
   if not xbmcvfs.exists(file):
       stvb = xbmcaddon.Addon('plugin.video.sportsmania')
       src = os.path.join(stvb.getAddonInfo('path'), 'resources', filename)
       xbmcvfs.copy(src, file)
except:
   pass
                

def OPEN_URL(url):
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib2.urlopen( req )
    link= con.read()
    return link

def EXIT():
        xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
        xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
    
    
if ADDON.getSetting('snusername')=='':
    dialog = xbmcgui.Dialog()
    if dialog.yesno(THESITE.upper(), "If You Dont Have An Account", "Please Sign Up At",THESITE.upper(),"Exit","Carry On"):
        
        dialog.ok(THESITE.upper(), "You Now Need To Input", "Your [COLOR yellow]Username[/COLOR]")
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, THESITE.upper())
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() 
        ADDON.setSetting('snusername',search_entered)
        
        dialog.ok(THESITE.upper(), "You Now Need To Input", "Your [COLOR yellow]Password[/COLOR]")
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, THESITE.upper())
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() 
        ADDON.setSetting('snpassword',search_entered)
        ADDON.setSetting('login_time','2000-01-01 00:00:00')
    else:
        EXIT()

        



def TryAgain():
     dialog = xbmcgui.Dialog()       
     dialog.ok(THESITE.upper(), "You Now Need To Input", "Your [COLOR yellow]Username[/COLOR]")
     search_entered = ''
     keyboard = xbmc.Keyboard(search_entered, THESITE.upper())
     keyboard.doModal()
     if keyboard.isConfirmed():
         search_entered = keyboard.getText() 
     ADDON.setSetting('snusername',search_entered)
     
     dialog.ok(THESITE.upper(), "You Now Need To Input", "Your [COLOR yellow]Password[/COLOR]")
     search_entered = ''
     keyboard = xbmc.Keyboard(search_entered, THESITE.upper())
     keyboard.doModal()
     if keyboard.isConfirmed():
         search_entered = keyboard.getText() 
     ADDON.setSetting('snpassword',search_entered)
     ADDON.setSetting('login_time','2000-01-01 00:00:00')
     CATEGORIES()
 
        
site='http://'+THESITE+'/site/live-tv/'


datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
cookie_path = os.path.join(datapath, 'cookies')
cookie_jar = os.path.join(cookie_path, THESITE+"15_amember_new_matrix.lwp")
cookie_amember = os.path.join(cookie_path, THESITE+"_amember_.lwp")
cookies_123 = os.path.join(cookie_path, '123.lwp')
channeljs=os.path.join(cookie_path, "channels.json")
paki=os.path.join(datapath, "paki")

if os.path.exists(cookie_path) == False:
      os.makedirs(cookie_path)

def checksub():
   
   if sessionExpired() or os.path.exists(cookie_jar) == False:
       Login()
   addDir('[COLOR chocolate]My Subscriptions[/COLOR]','',2007,'','','','')    
   #print'########################## checking ########################'
   username = ADDON.getSetting('snusername')
   password = ADDON.getSetting('snpassword')

   net.set_cookies(cookie_jar)

   html = net.http_GET('http://sportsmania.rocks/user_test.php').content
   link=json.loads(html)
   for field in link:
      exp =field['exp']
      try:
         EXP=datetime.datetime.strptime(exp,  '%Y-%m-%d').strftime('%A %d %B %Y')
      except TypeError:
         EXP=datetime.datetime(*(time.strptime(exp,  '%Y-%m-%d')[0:6])).strftime('%A %d %B %Y')
     # EXP=datetime.datetime.strptime(exp, '%Y-%m-%d').strftime('%A %d %B %Y')
      name=field['name']
      status=field['status'].title()
      if 'Active' in status:
         status='[COLOR green]%s[/COLOR]'%status
      else:
         status='[COLOR red]%s[/COLOR]'%status     
      TITLE='[COLOR white]%s[/COLOR] - %s'% (name,status)  
      addDir(TITLE,'',2007,'','','','')
      addDir('Expires - '+EXP,'',2007,'','','','')
      addDir('','',2007,'','','','')


def resetpass():
    loginurl = 'http://'+THESITE+'/payments/sendpass'
    headers  = {'Host':THESITE,
                                            'Origin':'http://'+THESITE,
                                            'Referer':'http://'+THESITE+'/payments/login',
                                                    'X-Requested-With':'XMLHttpRequest'}
    
    get = net.http_POST(loginurl, {'login':ADDON.getSetting('snusername')}, headers).content

    message=re.compile('"error":\["(.+?)"\]').findall(get)[0]
    try:
        line1 = message.split('.')[0]
        line2 = message.split('.')[1]
        line3 = ''
        dialog = xbmcgui.Dialog()
        dialog.ok(THESITE.upper(), line1,line2, line3)
        dialog.ok(THESITE.upper(), '','Please Check Your Junk Folder', '')
        ADDON.setSetting('resetpass','false')
    except:
        line1 = message.split('[')[0]
        line2 = message.split('[')[1]
        line2 = '[COLOR red]'+line2.split(']')[0]+'[/COLOR]'
        line3 = message.split(']')[1]      
        dialog = xbmcgui.Dialog()
        dialog.ok(THESITE.upper(), line1,line2, line3)
        EXIT()
        import update
        update.reset()
      


    
def WAIT():
        try:
            os.remove(cookie_jar)
            #print'cookie removed'
        except:
            pass   
        dialog = xbmcgui.Dialog()
        dialog.ok('[COLOR red]ERROR !![/COLOR]',"", "[COLOR red]Cannot Retrieve Channels[/COLOR]", "")
        Login()
               

def LOGOUT():
    net.set_cookies(cookie_jar)
    html = net.http_GET(site).content
    match=re.compile('  href="(.+?)">Log Out</a>').findall(html)[0]
    net.set_cookies(cookie_jar)
    logout = net.http_GET(match.replace('#038;','')).content
    if 'You are now logged out' in logout:
        #print'===============LOGGED OUT !!==============='
        dialog = xbmcgui.Dialog()
        dialog.ok(THESITE.upper(),'', "You Are Now Logged Out", "")
        EXIT()
        
        
def SYSEXIT():
    sys.exit()
    xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
    xbmc.executebuiltin("XBMC.ActivateWindow(Videos)")

def Login():
    #print'###############    LOGIN TO Sports Mania   #####################'
    loginurl = 'http://'+THESITE+'/payments/login'
    username = ADDON.getSetting('snusername')
    password = ADDON.getSetting('snpassword')
	
    import time
    TIME = time.time()- 3600
    
    data={'amember_login':username,'amember_pass':password,'login_attempt_id':str(TIME).split('.')[0],'remember_login':'1'} 
  

    headers={'Accept':'*/*',
    'Accept-Encoding':'gzip,deflate,sdch',
    'Accept-Language':'en-US,en;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':THESITE,
    'Origin':'http://'+THESITE,
    'Referer':'http://'+THESITE+'/payments/login',
    'User-Agent':'XBMC',
    'X-Requested-With':'XMLHttpRequest'}

    try:
       net.set_cookies(cookie_jar)
       html = net.http_POST(loginurl, data, headers).content
    except:
       dp = xbmcgui.DialogProgress()
       dp.create(THESITE.upper(),"CloudFlare.... ",'', 'Please Wait If you get an error KEEP TRYING!')
       cloudflare.solve(loginurl,cookie_jar,dp)
       net.save_cookies(cookie_jar)
       net.set_cookies(cookie_jar)
       dp.update(100,"Login into SPORTSMANIA.... ", "Please Wait")
       html = net.http_POST(loginurl, data, headers).content
       dp.close()
       
       
    
    if 'true' in html:
       import json
       ADDON.setSetting('login_time',str(datetime.datetime.today()+ datetime.timedelta(minutes=60)).split('.')[0])
       try:os.remove(cookie_jar)
       except:pass

       add_ontapp = ontapp1 + 1        
       ADDON.setSetting('ontapp_id_1',str(add_ontapp))
       net.save_cookies(cookie_jar)
       net.set_cookies(cookie_jar)
       sub = net.http_GET('http://sportsmania.rocks/user_test.php').content
       subs=json.loads(sub)
       stat = False
       for field in subs:
            status=field['status'].title()
            if 'Active' in status:
                 stat = True
	
       if stat:		
            a=net.http_GET('http://'+THESITE+'/reloaded.php?do=channels',headers={'User-Agent' :UA}).content
            f = open(channeljs, mode='w')
            f.write(a)
            f.close()
       else:
            dialog = xbmcgui.Dialog()
            dialog.ok(THESITE.upper(), '','Your subscription has expired please go to http://sportsmania.rocks/payments/login to resubscribe to SPORTS MANIA','')
            try:os.remove(cookie_jar)
            except:pass
            SYSEXIT()
            return False
    if 'false' in html:
       import json
       link=json.loads(html)
       error=link['error']
       dialog = xbmcgui.Dialog()
       dialog.ok(THESITE.upper(), '',str(error).replace("[u'",'').replace("']",''), "")
       dialog.ok(THESITE.upper(), '','We Will Exit Now', "")
       if not 'please' in str(error).lower() or not 'administator' in str(error).lower():
          username = ADDON.setSetting('snusername','')
          password = ADDON.setSetting('snpassword','')
          try:os.remove(cookie_jar)
          except:pass
       SYSEXIT()
       return False


def downloadchannel():
    if os.path.exists(cookie_path) == False:
        os.makedirs(cookie_path)
    if sessionExpired():
        Login()
    net.set_cookies(cookie_jar)
    a=net.http_GET('http://'+THESITE+'/reloaded.php?do=channels',headers={'User-Agent' :UA}).content
    f = open(channeljs, mode='w')
    f.write(a)
    f.close()


def parse_date(dateString):
    import time
    return datetime.datetime.fromtimestamp(time.mktime(time.strptime(dateString.encode('utf-8', 'replace'), "%Y-%m-%d %H:%M:%S")))


def getday():
    today = datetime.datetime.today()
    return today.strftime("%A")  


def sessionExpired():
   
    expiry=ADDON.getSetting('login_time')


    now        = datetime.datetime.today()
 
    
    prev = parse_date(expiry)


    return (now > prev)
    



def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime


def InTime():
    utc = datetime.datetime.utcnow() .strftime("%I:%M%p")
    #DAY=getday()

    if DAY=='Saturday':
        timeStart = '12:30PM'
        timeEnd = '3:00PM'
    elif DAY=='Sunday':
        timeStart = '1:30PM'
        timeEnd = '4:00PM'
    elif DAY=='Tuesday' or DAY=='Wednesday':
        timeStart = '7:30PM'
        timeEnd = '8:00PM'
    else:
        return False
        
    timeEnd = datetime.datetime.strptime(timeEnd, "%I:%M%p")
    timeStart = datetime.datetime.strptime(timeStart, "%I:%M%p")
    timeNow = datetime.datetime.strptime(utc,"%I:%M%p")

    return (isNowInTimePeriod(timeStart, timeEnd, timeNow))

def server():
   
    if sessionExpired() or os.path.exists(cookie_jar) == False:
        Login()
    if os.path.exists(channeljs) == False:
       return RefreshChannels()
       
    a=open(channeljs).read()
    if len(a)<2:
       return RefreshChannels()


    return a


def CheckChannels():
    update=OPEN_URL('http://xty.me/xunitytalk/addons/plugin.video.offside/update.txt')
    ADDON.setSetting('pakauth',re.compile('<pakauth>(.+?)</pakauth>').findall(update)[0]) 
    ADDON.setSetting('pakurl',re.compile('<pakurl>(.+?)</pakurl>').findall(update)[0])

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))

#

def CreatIniNow(name,url,mode,iconimage,play,date,description,page=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&play="+urllib.quote_plus(play)+"&date="+urllib.quote_plus(date)+"&description="+urllib.quote_plus(description)+"&page="+str(page)
        a=name.replace('-[US]','').replace('-[EU]','').replace('[COLOR yellow]','').replace('[/COLOR]','').replace(' GB','').replace(' (G)','').replace(' HD','').replace(' EU','')+'='+u
        f = open(STVBINI, mode='a')
        f.write(a+'\n')
        f.close()           

def CATEGORIES():
    #CheckChannels()
    link = json.loads(server())

    for c in link:
        name = c['_id'].encode("utf-8");
        catName = name.lower().replace(" ","_")
        if ".GAME ZONE" in name:
            addDir('[COLOR blueviolet]' + name + '[/COLOR]', catName, 4, MEDIA_URL+'games.png','','','')
        elif ".Match Day" in name:
            if '2' in name:
                addDir('[COLOR chartreuse]'+name + ' (Recommended)[/COLOR]', catName, 4, MEDIA_URL+'epl1.png','','','')
            else:
                addDir('[COLOR chartreuse]' + name + ' (Recommended)[/COLOR]', catName, 4,
                       MEDIA_URL + 'epl1.png', '', '', '')
        elif "Aussie Mania" in name:
            addDir('[COLOR yellow]' + name + '[/COLOR]', catName,4, MEDIA_URL+"aus.png",'','','')
        else:
            addDir(name,catName, 4, MEDIA_URL+catName+".png",'','','')


    #data2 = link['channels']
    #lista = []
    # for k in data2:
    #     #print'id: '+k['cat_id']
    #     lista.append(k['cat_id'])
    #
    # if ontapp1 > ontapp2:
    #     a='[%s]\n'% PLUGIN
    #     f = open(STVBINI, mode='w')
    #     f.write(a)
    #     f.close()
    #
    #
    # uniques=[]
    # uniquesurl=[]
    # data=link['categories']
    # ret = ''
    # for j in data:
    #
    #     if j in lista:
    #         url = j
    #         name = data[j].encode("utf-8")
    #
    #         if name not in uniques:
    #             uniques.append(name)
    #             uniquesurl.append(url)
    #             if ".GAME ZONE" in name:
    #                 #print"gamezone::::: "+url
    #                 addDir('[COLOR blueviolet]'+name+'[/COLOR]',url,4,MEDIA_URL+'games.png','','','')
    #             elif ".Match Day" in name:
    #                 if '2' in name:
    #                     name = name+' (Recommended)'
    #                 addDir('[COLOR chartreuse]'+name+'[/COLOR]',url,4,MEDIA_URL+'epl1.png','','','')
    #             elif "Aussie Mania" in name:
    #                 addDir('[COLOR yellow]'+name+'[/COLOR]',url,4,MEDIA_URL+'aus.png','','','')
    #             else:
    #                 addDir(name,url,4,MEDIA_URL+url+'.png','','','')
    #
    #
    #
    # if ontapp1 > ontapp2:
    #     #print'################# CREATING INI ########################'
    #     data=link['channels']
    #     for field in data:
    #         id= str(field['id'])
    #         name= field['title'].encode("utf-8")
    #         if ".GAME ZONE" in name:
    #
    #             CreateInitNow('[COLOR blueviolet]'+name+'[/COLOR]',url,2,MEDIA_URL+'games.png','','','')
    #         elif ".EPL Match Day" in name:
    #             CreateInitNow('[COLOR aquamarine]'+name+'[/COLOR]',url,2,MEDIA_URL+'premiere.jpg','','','')
    #         else:
    #             iconimage=id+'.png'
    #             CreatIniNow(name,id,2,MEDIA_URL+iconimage,'False','','')

                 
    if os.path.exists(cookie_jar) == True:
        try:
            import random
            text = ''
            twit = 'http://twitrss.me/twitter_user_to_rss/?user=@Mania_Team_Info'
            link = OPEN_URL(twit)
            link = link.split('<item>')[1]

            match = re.compile("<title>(.+?)</title>", re.DOTALL).findall(link)
            x = cleanHex(match[0])
            status = replaceN(x, 60)
            addDir('.[COLOR royalblue]*** [/COLOR] [COLOR orange]' + status.strip() + '[/COLOR]','url',1,MEDIA_URL+'twitter.png', '', '', '')
        except:pass
        addDir('.[COLOR white]-->>[/COLOR][COLOR chocolate]Click Here To Check When Your Sub Expires [/COLOR][COLOR white]<---[/COLOR]','url',2007,MEDIA_URL+'sub.png','','','')
        addDir('[COLOR aliceblue].Maintenance Tools[/COLOR]','url',16000,MEDIA_URL+'tools.png','','','')
        addDir('[COLOR beige].View Calendar[/COLOR]','http://sportsmania.rocks/sites/ukcalendar.html',2005,MEDIA_URL+'calendar.png','','','')
        addDir('[COLOR beige].View USA Calendar[/COLOR]','http://sportsmania.rocks/sites/usacalendar.html',2005,MEDIA_URL+'test.png','','','')
        addDir('[COLOR azure].THE MANIA SERVICES VIDEO TUTORIALS[/COLOR]','http://'+THESITE+'/apisprotected/tutorials.php',2003,MEDIA_URL+'howto.png','','','')
        #addDir('[COLOR gold].Manias Sports Mix (Football Rugby & More)[/COLOR]','http://'+THESITE+'/apisprotected/extrassm.php',2003,MEDIA_URL+'extra.png','','','')
        #addDir('[COLOR powderblue].Sports Extra Section (Football, Boxing & More)[/COLOR]','http://'+THESITE+'/apisprotected/plp2.php',2003,MEDIA_URL+'extra.png','','','')
        #addDir('[COLOR chartreuse].EPL Match Day Section 3 (Recommended)[/COLOR]','http://'+THESITE+'/apisprotected/plp.php',2003,MEDIA_URL+'epl1.png','','','')
        #addDir('[COLOR navajowhite].NBA Live Games[/COLOR]','http://'+THESITE+'/apisprotected/nba.php',2003,MEDIA_URL+'nba.png','','','')
        #addDir('[COLOR orange].NFL Game Day[/COLOR]','http://'+THESITE+'/apisprotected/nfl.php',2003,MEDIA_URL+'nfl.png','','','')
        #addDir('[COLOR mintcream].MLB Game Pass[/COLOR]','http://'+THESITE+'/apisprotected/mlb.php',2003,MEDIA_URL+'mlb.png','','','')
        #addDir('[COLOR orchid].NHL Live Game Pass[/COLOR]','http://'+THESITE+'/apisprotected/nhl.php',2003,MEDIA_URL+'nhl.png','','','')
        addDir('[COLOR cyan].Sports On Demand[/COLOR]','http://'+THESITE+'/apisprotected/channels1.php',2003,MEDIA_URL+'cup.png','','','')                
        #addDir('[COLOR mediumspringgreen].Movies / TV Shows On Demand [/COLOR][COLOR gold][/COLOR]','http://xtyrepo.me/xunitytalk/playlist/OSS%20MAIN',12000,MEDIA_URL+'movies.png','','','')           
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
    ADDON.setSetting('ontapp_id_2',str(ontapp1))
    xbmc.executebuiltin('Container.SetViewMode(51)')


def replaceN(s, n):
    return ''.join('\n' if not i%n else char for i, char in enumerate(s, 1))

def schedule(url):
    if 'usa' in url:
       media=os.path.join(ADDON.getAddonInfo('path'), 'resources', 'icons','usa')
    else:
       media=os.path.join(ADDON.getAddonInfo('path'), 'resources', 'icons','uk')
       
    net.set_cookies(cookie_jar)
    response = net.http_GET(url)
    link = response.content.replace('\t','').replace('\n','').replace('\r','')
    titles=re.compile('<div class="panel-heading"><center><b>(.+?)</b></center>').findall(link)
    for heading in titles:
        if not 'sport' in heading.lower():
           if getday().lower() in heading.lower():           
              addDir('[COLOR cyan]*** %s ***[/COLOR]'% heading,'url',200,'','','','')

              links=link.split(heading)[1]
              links=links.split('</table>')[0]
              links=links.split('<tr>')
              for p in links:
                  try:
                      match=re.compile('bgcolor="(.+?)"><font color=".+?">(.+?)</font>',re.DOTALL).findall(p)

                      font= match[0][0]
                      if font =='#624F27':       #CRICKET/NFL
                        font = 'sienna'
                      if font =='#0000FF':       #FOOTBALL/SOCCER
                        font = 'royalblue'
                      if font =='#006F09':       #RUGBY/NBA
                        font = 'coral'
                      if font =='#69005F':       #SNOOKER/NHL
                        font = 'purple'
                      if font =='#FF0000':       #MOTOR/MLB
                        font = 'red'
                      if font =='#E68300':       #MMA
                        font = 'orange'
                      if font =='#000000':       #HORSE
                        font = 'grey'
                      if font =='#ADFF2F':       #TENNIS
                        font = 'lime'
                      if font =='#FF1493':       #GOLF
                        font = 'pink'
                      if font =='#40E0D0':       #GAA/NASCAR
                        font = 'turquoise'
                      if font =='#DAA520':       #DARTS/NCAA
                        font = 'darkcyan'
                          
                          
                      time= match[0][1]
                      name= match[1][1]
                      channels= match[2][1].replace('Game Zone / ','').strip()
        
                      NAME= '[COLOR %s]%s - %s -[/COLOR][COLOR green]%s[/COLOR]' % (font,time.replace('-',''),name.replace('-',''),channels.replace('-',''))
                      
                      addDir(NAME.encode('utf-8'),'url',2,media+'/'+font+'.png','GET_EVENT','',NAME)
                  except:pass
    setView('movies', 'calendar')  


def MySearch():
    addDir('[COLOR white]Click to >> [/COLOR][COLOR lime]Search Tv/Movies [COLOR white]<<[/COLOR]','url',3000,'','','','','')
    favs = ADDON.getSetting('favs').split(',')
    for title in favs:
        if len(title)>1:
            addDir(title.title(),title,3000,'','','','','')      
        #addDir(title,NEW_URL,8,'','')


def OnDemandFirstCat():
    addDir('[COLOR white]Search Tv/Movies[/COLOR]','url',3003,'','','','','')
    addDir('[COLOR white]Movies[/COLOR]','movie',4001,'','','','','')
    addDir('[COLOR white]Tv Shows[/COLOR]','series',4001,'','','','','')


def OnDemandSecondCat(url):
    addDir('[COLOR white]Most Popular[/COLOR]','http://123movies.to/movie/filter/%s/view/all/all/all/all/all/'%url,4002,'','','','',0)   
    addDir('[COLOR white]Latest[/COLOR]','http://123movies.to/movie/filter/%s/latest/all/all/all/all/all/'%url,4002,'','','','',0)
    addDir('[COLOR white]Most Favourite[/COLOR]','http://123movies.to/movie/filter/%s/favorite/all/all/all/all/all/'%url,4002,'','','','',0)
    addDir('[COLOR white]Most Rating[/COLOR]','http://123movies.to/movie/filter/%s/rating/all/all/all/all/all/'%url,4002,'','','','',0)
    addDir('[COLOR white]Top IMDb[/COLOR]','http://123movies.to/movie/filter/%s/imdb_mark/all/all/all/all/all/'%url,4002,'','','','',0)
            

def OnDemandThirdCat(url,page):

    page =page+1
    THE_URL =url
    user='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    headers={'User-Agent':user}
                          
    try:
       net.set_cookies(cookies_123)
       LINK=net.http_GET(url+str(page),headers=headers).content
       net.save_cookies(cookies_123)
       #print'CLOUDFLARE BYPASSED'
    except:
       import cloudflare
               
       LINK=cloudflare.solve(url+str(page),cookies_123,user)

    LINK = LINK.split('"ml-item">')
    for p in LINK:
        try:
           URL=re.compile('a href="(.+?)"',re.DOTALL).findall(p)[0]
           name=re.compile('title="(.+?)"',re.DOTALL).findall(p)[0]
           iconimage=re.compile('img data-original="(.+?)"',re.DOTALL).findall(p)[0]           

           addDir(name,URL,3001,iconimage,'','','','')
        except:pass  
    addDir('[COLOR royalblue]>> Next Page >>[/COLOR]',THE_URL,4002,'','','','',page)
            
       

def getme():
   return '|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'


def Oo0Oool(url):
 iI111iI = urllib2 . Request (url )
 IiII = urllib2 . urlopen ( iI111iI )
 iI1Ii11111iIi = IiII . read ( )
 IiII . close ( )
 return iI1Ii11111iIi

def auth():
 DATA_URL='https://app.dynns.com/keys/apps_token.php'
 request = urllib2.Request(DATA_URL)
 base64string = 'dm94c29mdGV4cGVydDpAdm94c29mdGV4cGVydEA='
 request.add_header("Authorization", "Basic %s" % base64string)   
 return urllib2.urlopen(request).read()
           
def worldlinks(name,url):
    NAME=name
    genre=name.split('[COLOR')[0].replace('.','')
    addDir('[COLOR gold]hmmm...[/COLOR]','url',2004,'','','','')
    AUTH=auth()
    aa=open(url).read()
    link=aa.split('<items>')
    for p in link:
        try:
            name=re.compile('<programTitle>(.+?)</programTitle>').findall(p)[0]
            URL=re.compile('<programURL>(.+?)</programURL>').findall(p)[0]
            iconimage=re.compile('<programImage>(.+?)</programImage>').findall(p)[0]
            if '<programCategory>'+genre+'<' in p:
                addDir(name,URL+AUTH,2004,iconimage,'','','')
        except:pass             
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
    
def parseAPI(url):

       ADDME=[]
       net.set_cookies(cookie_jar)
       a=net.http_GET(url,headers={'User-Agent':'XBMC'}).content
       PASS=False
       import json
       link=json.loads(a)
       data=link['vod_channels']
                           
       nameSelect=['All']
  
       uniques =[]
       for field in data:
           try:
              plot= str(field['channel_description'])

              if plot not in uniques: 
                  if not plot=='':
                      uniques.append(plot)
                      nameSelect.append(plot)
           except:pass
           
           
       if len(str(nameSelect))> 7:
           nameSelect.insert(0,'[COLOR yellow]Search[/COLOR]')
           GENRE = nameSelect[xbmcgui.Dialog().select('Please Select Category', nameSelect)]
           PASS=True

       
           if '[COLOR yellow]Search[/COLOR]' in str(GENRE):
               keyboard = xbmc.Keyboard('', 'Search Sports On Demand')
               keyboard.doModal()
               if keyboard.isConfirmed():
                   search_entered = keyboard.getText()
           
       for field in data:
           id= str(field['channel_url'])
           name= field['channel_title'].encode("utf-8")
           if '(' in name:
              date='('+name.split('(')[1]
              name=name.split('(')[0]
              NAME='[COLOR aqua]%s[/COLOR] - [COLOR yellow]%s[/COLOR]' % (name,date)
           else:
              NAME='[COLOR aqua]%s[/COLOR]' % (name)
           if PASS==True:
               
              if GENRE=='All':
                  addDir(NAME,id,2004,'','','','')
              elif '[COLOR yellow]Search[/COLOR]' in GENRE:
                  if search_entered.lower() in NAME.lower():
                      addDir(NAME,id,2004,'','','','') 
              else:

                  if GENRE in str(field['channel_description']):
                      addDir(NAME,id,2004,'','','','') 
           else:   
              addDir(NAME,id,2004,'','','','')  


def SportsOnDemand(url):
       ADDME=[]
       net.set_cookies(cookie_jar)
       a=net.http_GET(url,headers={'User-Agent':'XBMC'}).content

       import json
       link=json.loads(a)
       data=link['vod_channels']
       for field in data:
           id= str(field['channel_url'])
           name= field['channel_title'].encode("utf-8")
           if '(' in name:
              date='('+name.split('(')[1]
              name=name.split('(')[0]
              NAME='[COLOR darkgrey]%s[/COLOR] - [COLOR yellow]%s[/COLOR]' % (name,date)
           else:
              NAME='[COLOR darkgrey]%s[/COLOR]' % (name)
           addDir(NAME,id,2004,'','','','') 
        
        
def playAPI(name,url,iconimage):
    print url
    if not "http" in url:
      if not "rtmp" in url:
       
           return Play_Youtube(name,url,iconimage)
    if 'wmsAuthSign=' in url:
        url = url+'|User-Agent='+getuser()
         
    if url =='none':
        dialog = xbmcgui.Dialog()
        return dialog.ok(THESITE.upper(), '',"Streams Not Active Until match Time", "")
      
    if '.f4m' in url:
        import F4MProxy
        player=F4MProxy.f4mProxyHelper()
        player.playF4mLink(url, name,iconimage)      
    else:  
       if 'CHANGEME' in url:
          URL=['1600','3000','4500']
          NAME=['480P','720P','1080P']
          RES = URL[xbmcgui.Dialog().select('Please Select Resolution', NAME)]
          url=url.replace('CHANGEME',RES)+getme()
       liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
       liz.setInfo(type='Video', infoLabels={'Title':name})
       liz.setProperty("IsPlayable","true")
       liz.setPath(url)
       xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

       
def GENRES(name,url):

    #if InTime():
        #link = json.loads(server())
        
    #else:
    link = json.loads(server())
    type(link)
    for field in link:
        channels = field['channels']
        name = field['_id']
        for ch in channels:
            cid = ch['id']
            title = ch['title'].encode("utf-8")
            genre = name.lower().replace( " ","_" )
            iconimage = image + cid + '.png'
            if url == genre:
                if ':' in title:

                    TITLEHACK = title.split(':', 1)[1].replace(' HD', '')
                    if len(TITLEHACK) > 3:
                        addDir(title, cid, 2, iconimage, 'False', '', '')
                else:
                    addDir(title, cid, 2, iconimage, 'False', '', '')
          
    if url=='79':
       try:SportsOnDemand('http://'+THESITE+'/apisprotected/plp.php')
       except:pass

    if url=='70':
       try:SportsOnDemand('http://'+THESITE+'/apisprotected/clubs.php')
       except:pass

    if url=='42':
       try:SportsOnDemand('http://'+THESITE+'/apisprotected/ppv.php')
       except:pass

    if url=='40':
       try:SportsOnDemand('http://'+THESITE+'/apisprotected/bt.php')
       except:pass

    if url=='42':
       try:SportsOnDemand('http://'+THESITE+'/apisprotected/wwe.php')
       except:pass

    if url=='32':
       try:SportsOnDemand('http://'+THESITE+'/apisprotected/nfl.php')
       except:pass

    if url=='27':
       try:SportsOnDemand('http://'+THESITE+'/apisprotected/bbc.php')
       except:pass
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)             
    setView('movies', 'channels')        


def SEARCH(search_entered):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'}
    favs = ADDON.getSetting('favs').split(',')
    if 'url' in search_entered:
        keyboard = xbmc.Keyboard('', 'Search Movies / Tv Shows')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText()

    search_entered = search_entered.replace(',', '')

    if len(search_entered) == 0:
        return

    if not search_entered in favs:
        favs.append(search_entered)
        ADDON.setSetting('favs', ','.join(favs))

    search_entered = search_entered.replace(' ','%20')
        
    url='http://123movies.to/movie/search/' + str(search_entered).replace(' ','+')
    #printurl
    try:
       net.set_cookies(cookies_123)
       LINK=net.http_GET(url,headers=headers).content
       net.save_cookies(cookies_123)
       #print'CLOUDFLARE BYPASSED'
    except:
       import cloudflare
       user='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'                   
       LINK=cloudflare.solve(url,cookies_123,user)
                          
    #match=re.compile('class="ml-item">.+?a href="(.+?)".+?class="ml-mask jt".+?title="(.+?)">.+?data-original="(.+?)"',re.DOTALL).findall(LINK)
    LINK = LINK.split('"ml-item">')
    for p in LINK:
        try:
           URL=re.compile('a href="(.+?)"',re.DOTALL).findall(p)[0]
           name=re.compile('title="(.+?)"',re.DOTALL).findall(p)[0]
           iconimage=re.compile('img data-original="(.+?)"',re.DOTALL).findall(p)[0]           

           addDir(name,URL,3001,iconimage,'','','','')
        except:pass

        

def GetSearchLinks(name,url,iconimage,page):
  
    user='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    headers={'User-Agent':user}
                          
    try:
       net.set_cookies(cookies_123)
       LINK=net.http_GET(url+'watching.html',headers=headers).content
       net.save_cookies(cookies_123)
       #print'CLOUDFLARE BYPASSED'
    except:
       import cloudflare
               
       LINK=cloudflare.solve(url+'watching.html',cookies_123,user)
                          
    uniques=[]
    try:movie_id = re.compile('movie-id="(.+?)"').findall(LINK)[0]
    except:movie_id = re.compile('updateMovieView\((.+?)\)').findall(LINK)[0]
    token = re.compile('player-token="(.+?)"').findall(LINK)[0]
    coookie_1 = re.compile('ds_hash: "(.*?)"').findall(LINK)[0]
    coookie_2 = re.compile('ds_token: "(.*?)"').findall(LINK)[0]
    coookie = coookie_1 + '=' + coookie_2

    net.set_cookies(cookies_123)                      
    LOAD =net.http_GET('http://123movies.to/ajax/get_episodes/%s/%s'%(movie_id,token),headers=headers).content
    link=LOAD.split('<div id="server-')
    for p in link:
        #try:
             host= p.split('"')[0]
           
             HTML=p.split('<a title="')

             for d in HTML:
                 TITLE=d.split('"')[0]
                 if 'Season' in name:
                    TITLE=TITLE
                    if TITLE not in uniques:
                       uniques.append(TITLE)
                       if ':' in TITLE:
                           addDir(TITLE,LOAD,3010,iconimage,'','',coookie,'')
                           xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)   
                 else:
                    TITLE=name+' - '+TITLE
          
                    try:
                        YEAR=re.compile('Release:</strong>(.+?)<').findall(LINK)[0].strip()
                        #printYear
                        token = re.compile('hash="(.+?)"').findall(d)[0]
                        SERVER=d.split('loadEpisode(')[1]
                        server=SERVER.split(',')[0]
                        episodeid=re.compile(',(.+?),').findall(SERVER)[0]

                        URL='http://123movies.to/ajax/load_episode/%s/%s' % (episodeid,token)                            
                        
                        #printHTML
                        addDir(TITLE,URL,3002,iconimage,'','',coookie,'')
                        

                    except:pass
                    
    match=re.compile('data-episodes="(.+?)-(.+?)"').findall(LOAD)
  
    for episodeid , token in match:

      URL='http://123movies.to/ajax/load_episode/%s/%s' % (episodeid,token)                            
      addDir('.'+name+' HD',URL,3002,iconimage,'','',coookie,'')
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)      


def GetEpisodeLinks(name,LOAD,iconimage,page):
    NAME = name
    link=LOAD.split('<div id="server-')
    for p in link:
        #try:
             host= p.split('"')[0]
           
             HTML=p.split('<a title="')

             for d in HTML:
                 TITLE=d.split('"')[0]
          
                 try:
                     token = re.compile('hash="(.+?)"').findall(d)[0]
                     SERVER=d.split('loadEpisode(')[1]
                     server=SERVER.split(',')[0]
                     episodeid=re.compile(',(.+?),').findall(SERVER)[0]

                     URL='http://123movies.to/ajax/load_episode/%s/%s' % (episodeid,token)                            
                     
                     if NAME in TITLE:
                         addDir(TITLE,URL,3002,iconimage,'','',page,'')
                     

                 except:pass                
    match=re.compile('data-episodes="(.+?)-(.+?)"').findall(LOAD)

    for episodeid , token in match:

      URL='http://123movies.to/ajax/load_episode/%s/%s' % (episodeid,token)                            
      addDir('.'+NAME+' HD',URL,3002,iconimage,'','',page,'')
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)      
        

def OnDemand(url):
    addDir('[COLOR lime]Search[/COLOR]','url',3003,'','','','','')
    
    link = OPEN_URL(url).replace('\n','').replace('\t','').replace('\r','')
    if '<streamtvbox>' in link:
        message=re.compile('<streamtvbox>(.+?)</streamtvbox>').findall (link)
        for name in message:
            addLink(name,'url','','')


    DIRS=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail>',re.DOTALL).findall (link)

    for name , url , iconimage  in DIRS:      
        addDir(name,url,6,iconimage,'','','','')

        
    DIRS=re.compile('<title>(.+?)</title><dir>(.+?)</dir><thumbnail>(.+?)</thumbnail>',re.DOTALL).findall (link)

    for name , url , iconimage  in DIRS:      
        addDir(name,url,6,iconimage,'','','','')        



def OnDemandLinks(url):
    link = OPEN_URL(url).replace('\n','').replace('\t','').replace('\r','')
    if '<message>' in link:
       message=re.compile('<message>(.+?)</message>').findall (link)
       for name in message:
           addLink(name,'url','','')   

    DIRS=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail>',re.DOTALL).findall (link)

    for name , url , iconimage  in DIRS:      
        addDir(name,url,6,iconimage,'','','','')  

    LINKS=re.compile('<title>(.+?)</title.+?<link>(.+?)</link.+?<thumbnail>(.+?)</thumbnail>',re.DOTALL).findall (link)
    
   
    for name , url , iconimage in LINKS:
        addDir(name,url,7,iconimage,'','','','')


def GrabVK(url):
    html=OPEN_URL(url)
    r      ='"url(\d+)":"(.+?)"'
    name=[]
    url=[]
    match = re.compile(r,re.DOTALL).findall(html)
    for quality,stream in match:
        name.append(quality.replace('\\','')+'p')
        url.append(stream.replace('\/','/'))
    return url[xbmcgui.Dialog().select('Please Select Resolution', name)]
    
def afdah(url):
    url= 'https://m.afdah.org/watch?v='+url

    loginurl = 'https://m.afdah.org/video_info/html5'

    v=url.split('v=')[1]
    data={'v': v}
    headers = {'host': 'm.afdah.org','origin':'https://m.afdah.org', 'referer': url,
               'user-agent':'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5','x-requested-with':'XMLHttpRequest'}

    first= net.http_POST(loginurl,data,headers).content

    link= json.loads(first)
    name=[]
    url=[]
    for j in link:
        name.append(j.upper())
   
        url.append(urllib.unquote(link[j][3]))

    THEURL= url[xbmcgui.Dialog().select('Please Select Resolution', name)]
    import requests
    r=requests.get(THEURL,allow_redirects=False, verify=False )   

    r = requests.get(str(r.headers['Location']),allow_redirects=False, verify=False )

    return r.headers['location']


def PlayOnDemand(url):

    if 'googlevideo' in url or 'blogspot' in url:
        url=url
    elif not 'http' in url:
        url=afdah(url)
    elif 'http://vk' in url:
        url=GrabVK(url)

    elif 'movreel' in url:
        import movreel
        url=movreel.solve(url)
    elif 'xmovies8.tv' in url:
        url=url        
    else:
        import urlresolver
        url=urlresolver.resolve(url)
            
         
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title':description})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)


    


 
def EVENTS():
    link = OPEN_URL('http://channelstatus.weebly.com/upcoming-events.html')
    link=link.split('<div class="paragraph" style="text-align:left;"')[1]
    link=link.split('>***')
    for p in link:
        try:
            DATE=re.compile('(.+?)\*').findall(p)[0]
            addDir('[COLOR cyan]'+DATE+'[/COLOR]','',2000,'','False','','')  
            match=re.compile('\[(.+?)\]</strong>__ (.+?) - (.+?)__',re.DOTALL).findall (p)
            for TIME ,VS , CHANNEL in match:

                CHANNEL=CHANNEL.replace('beIN','beIN Sports ').replace('Sports  Sports','Sports')
                name= '[COLOR white][%s][/COLOR][COLOR yellow]- %s -[/COLOR][COLOR green]%s[/COLOR]' %(TIME,VS,CHANNEL)
                addDir(name,'url',2,'','GET_EVENT','','')       
        except:pass
    xbmc.executebuiltin('Container.SetViewMode(51)')  
        

 
def Show_Dialog():
    dialog = xbmcgui.Dialog()
    dialog.ok(THESITE.upper(), '',"All Done Try Now", "")
        
def REPLAY():
       
        xbmc.executebuiltin('ActivateWindow(videos,plugin://plugin.video.footballreplays)')

 
    
def OPEN_MAGIC(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent' , "Magic Browser")
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
        
        
        
def timeout():
    if ADDON.getSetting('hlsenable')=='true':
       return ''
    else:  
       quality = ADDON.getSetting('timeout')
       return ''
       if quality == '0':
           return ' timeout=5 '
       elif quality == '1':
           return ' timeout=10'
       elif quality == '2':
           return ' timeout=15'
       elif quality == '3':
           return ' timeout=20'
       elif quality == '4':
           return ' timeout=25'
       elif quality == '5':
           return ' timeout=30'
       elif quality == '6':
           return ' timeout=35'
       elif quality == '7':
           return ' timeout=40'
       elif quality == '8':
           return ' timeout=45'
       elif quality == '9':
           return ' timeout=50'
        


def Show_Down():
    dialog = xbmcgui.Dialog()
    dialog.ok(THESITE.upper(), 'Sorry Channel is Down',"Will Be Back Up Soon", "Try Another Channel")  
    
def Show_Cover():
    dialog = xbmcgui.Dialog()
    dialog.ok(THESITE.upper(), '',"Sorry We Dont Cover This Channel", "")

    
def Show_Dif_Channel():
    dialog = xbmcgui.Dialog()
    dialog.ok(THESITE.upper(), '',"Please Use A Different Channel", "")

def Play_Youtube(name,url,iconimage):
    import youtube

    url=youtube.GetVideoInfo(url)[0]['best']    
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title':name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(str(url))
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)


def PLAY_DEMAND_STREAM(name, url, iconimage,cookie):

   headers={'Cookie':cookie,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','Referer': 'http://123movies.to','x-requested-with':'XMLHttpRequest'}
   STREAM=[]
   NAMED=[]
   GRAB=[]
   uniques=[]
   try:
      #net.set_cookies(cookies_123)
      #print'CLOUDFLARE BYPASSED'
      HTML=net.http_GET(url,headers=headers).content
      
      if 'oops' in HTML.lower():
        dialog = xbmcgui.Dialog()
        return dialog.ok(THESITE.upper(), 'Sorry Channel',"", "Could Not Find A Stream") 
      match=re.compile('file="(.+?)".+?label="(.+?)"',re.DOTALL).findall(HTML)
      #printmatch
      for FINAL_URL , res in match:
           if len(res)>4:
              res='700'
           
           GRAB.append([FINAL_URL , res])
      matched=re.compile('file="(.+?)"',re.DOTALL).findall(HTML)

      for FINAL_URL  in matched:
   
           HOST=FINAL_URL.split('://')[1]
           HOST=HOST.split('/')[0]              
           GRAB.append([FINAL_URL , '700'])
           
      for FINAL_URL , res  in GRAB:
           HOST=FINAL_URL.split('://')[1]
           HOST=HOST.split('/')[0]                                  
            
           if not '.srt' in FINAL_URL:
               res=res.replace('p','')
               
               res=int(res)
               if (res > 700):
                   res='[COLOR green]1080P[/COLOR]'
                   NAME='%s - [COLOR royalblue]%s[/COLOR]' %(res,HOST.upper())
                   if FINAL_URL not in uniques:
                      uniques.append(FINAL_URL)   
                      STREAM.append(FINAL_URL)
                      NAMED.append(NAME)
             
              
               if (res > 500):
                   res='[COLOR yellow]720P[/COLOR]'
                   NAME='%s - [COLOR royalblue]%s[/COLOR]' %(res,HOST.upper())
                   if FINAL_URL not in uniques:
                      uniques.append(FINAL_URL)   
                      STREAM.append(FINAL_URL)
                      NAMED.append(NAME)                

                        
               if (res < 500):
                   res='[COLOR orange]SD[/COLOR]'
                 

                   NAME='%s - [COLOR royalblue]%s[/COLOR]' %(res,HOST.upper())
                   if FINAL_URL not in uniques:
                      uniques.append(FINAL_URL)   
                      STREAM.append(FINAL_URL)
                      NAMED.append(NAME)
                        
                       
   except:pass
   url=STREAM[xbmcgui.Dialog().select('Choose Source !!', NAMED)]
   if 'streaming.fshare' in url:
      req = urllib2.Request(url, headers=headers) 
      url = urllib2.urlopen( req )  .geturl()    
      #url=urllib.urlopen(url).geturl()
      #printurl
   liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
   liz.setInfo(type='Video', infoLabels={'Title':name})
   liz.setProperty("IsPlayable","true")
   liz.setPath(url.replace('amp;',''))
   xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

    
def PLAY_STREAM(name, url, iconimage, play, description):
    if sessionExpired() or os.path.exists(cookie_jar) == False:
        Login()
    
    if play =='GET_EVENT':
        url=PLAY_FROM_EVENTS(name, url, iconimage, play, description)

    if not url:
        return Show_Cover()

    net.set_cookies(cookie_jar)
    stream_url= net.http_GET('http://'+THESITE+'/reloaded.php?do=stream&type=rtmp&channel=%s'%url,headers={'User-Agent' :UA}).content+timeout()
    tmpUrl = str(stream_url)
    print stream_url
    if stream_url=='':
        return Show_Down()
    elif tmpUrl.startswith('direct'):
        playAPI(name,stream_url.replace('direct#','',2),'')
    else:
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setInfo(type='Video', infoLabels={'Title':description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)


def PLAY_FROM_EVENTS(name, url, iconimage, play, description):
    name=name.split('[COLOR green]')[1].replace('[/COLOR]','')
    name=name.replace('/',',').strip()

  
    if not 'EPL' in name:
       name.replace('-','').strip()
    nameFINAL=[]
    urlFINAL=[]
    if ',' in name:
       
        nameSelect=[]
        urlSelect=[]
        name=name.split(',')
        for p in name:
            urlSelect.append(p.strip().lower())
            nameSelect.append(p.strip())
        TITLE = urlSelect[xbmcgui.Dialog().select('Please Select Channel', nameSelect)]      
        TITLE=TITLE.replace(' ','').lower().strip()
        PASS=False
        BLUFF=True
        if 'btsport' in TITLE:
             URL='http://'+THESITE+'/apisprotected/bt.php'
             PASS=True
             BLUFF=False
        if 'matchday' in TITLE:
             URL='http://'+THESITE+'/apisprotected/plp.php'
             PASS=True
             BLUFF=True
        if 'mlb' in TITLE:
             URL='http://'+THESITE+'/apisprotected/mlb.php'
             PASS=True
        if 'foxsports' in TITLE:
            URL = 'http://' + THESITE + '/apisprotected/plp2.php'
            PASS = True
            BLUFF = False
        if 'nfl' in TITLE:
             URL='http://'+THESITE+'/apisprotected/usa.php'
             PASS=True
        if 'nhl' in TITLE:
             URL='http://'+THESITE+'/apisprotected/nhl.php'
             PASS=True
        if PASS==True:     
             net.set_cookies(cookie_jar)
             a=net.http_GET(URL,headers={'User-Agent':'XBMC'}).content
             link=json.loads(a)
             data=link['vod_channels']
             for field in data:
                 id= str(field['channel_url'])
                 if BLUFF== True:
                    YOYO= field['channel_title'].encode("utf-8")
                    GAME_TITLE=re.compile('/COLOR\] (.+?)\[COLOR yellow').findall(YOYO)[0]
                    if GAME_TITLE.replace(' ','').lower() in description.replace(' ','').lower():
                        urlFINAL.append(id)
                        nameFINAL.append('[COLOR lime]%s[/COLOR]'%(YOYO)+' <<-- (Recommended)')
                 else:
                    YOYO= field['channel_title'].encode("utf-8")
                    if TITLE in YOYO.replace(' ','').lower():
                        urlFINAL.append(id)
                        nameFINAL.append('[COLOR lime]%s[/COLOR]'%(YOYO)+' <<-- (Recommended)')
        link = json.loads(server())
        data=link['channels']
        for field in data:
            id= str(field['id'])
            YOYO= field['title'].encode("utf-8")    
            if TITLE in YOYO.replace(' ','').lower():
                urlFINAL.append(id)
                nameFINAL.append('[COLOR lime]%s[/COLOR]'%(YOYO))     
        if urlFINAL:
            return urlFINAL[xbmcgui.Dialog().select('Multiple Channels Found', nameFINAL)]


    else:
    
        NAME=name.replace(' ','').lower().strip()
        
        PASS=False
        BLUFF=True
        if 'btsport' in NAME:
             URL='http://'+THESITE+'/apisprotected/bt.php'
             PASS=True
             LEN=7
             BLUFF=False
        if 'matchday' in NAME:
             URL='http://'+THESITE+'/apisprotected/plp.php'
             PASS=True
             BLUFF=True
             LEN=8
        if 'foxsports' in NAME:
            URL = 'http://' + THESITE + '/apisprotected/plp2.php'
            PASS = True
            BLUFF = False
            LEN = 9
        if 'ppv' in NAME:
             URL='http://'+THESITE+'/apisprotected/ppv.php'
             PASS=True
             BLUFF=True
             LEN=8
        if 'mlb' in NAME:
             URL='http://'+THESITE+'/apisprotected/mlb.php'
             PASS=True
             LEN=3
        if 'nfl' in NAME:
             URL='http://'+THESITE+'/apisprotected/usa.php'
             PASS=True
             LEN=3
        if 'nhl' in NAME:
             URL='http://'+THESITE+'/apisprotected/nhl.php'
             PASS=True
             LEN=3
        if PASS==True:     
             net.set_cookies(cookie_jar)
             a=net.http_GET(URL,headers={'User-Agent':'XBMC'}).content
             link=json.loads(a)
             data=link['vod_channels']
             for field in data:
                 id= str(field['channel_url'])
                 if BLUFF== True:
                    YOYO= field['channel_title'].encode("utf-8")
                    GAME_TITLE=re.compile('/COLOR\] (.+?)\[COLOR yellow').findall(YOYO)[0]

                    if GAME_TITLE.replace(' ','').lower() in description.replace(' ','').lower():
                        urlFINAL.append(id)
                        nameFINAL.append('[COLOR lime]%s[/COLOR]'%(YOYO)+' <<-- (Recommended)')
                 else:
                    YOYO= field['channel_title'].encode("utf-8")
                    if NAME in YOYO.replace(' ','').lower():
                        urlFINAL.append(id)
                        nameFINAL.append('[COLOR lime]%s[/COLOR]'%(YOYO)+' <<-- (Recommended)')
        link = json.loads(server())
        data=link['channels']
        for field in data:
            id= str(field['id'])
            NAME_= field['title'].encode("utf-8")
            
            if NAME in NAME_.replace(' ','').lower().strip():
                urlFINAL.append(id)
                nameFINAL.append('[COLOR lime]%s[/COLOR]'%(NAME_))
        if urlFINAL:
            return urlFINAL[xbmcgui.Dialog().select('Multiple Channels Found', nameFINAL)] 
        else:
            return False
         
         
def setView(content, viewType):
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
      
def getSetting(setting):
        import json
        setting = '"%s"' % setting
 
        query = '{"jsonrpc":"2.0", "method":"Settings.GetSettingValue","params":{"setting":%s}, "id":1}' % (setting)
        response = xbmc.executeJSONRPC(query)

        response = json.loads(response)                

        if response.has_key('result'):
            if response['result'].has_key('value'):
                return response ['result']['value'] 


def setSetting(setting, value):
    value="%s" % value
    query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":"%s","value":"%s"}, "id":1}' % (setting, value)
    if value=='false':
        value= value
        query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":"%s","value":%s}, "id":1}' % (setting, value)
    if value=='true':
        value= value
        query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":"%s","value":%s}, "id":1}' % (setting, value)
    if len(value)<4:
        value= value
        query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":"%s","value":%s}, "id":1}' % (setting, value)

        
    #query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":"%s","value":%s}, "id":1}' % (setting, value)
    xbmc.log(str(query))
    xbmc.executeJSONRPC(query)
    xbmc.executebuiltin("Container.Refresh")  


def RefreshChannels():
    if sessionExpired() or os.path.exists(cookie_jar) == False:
        Login()
    net.set_cookies(cookie_jar)
    a=net.http_GET('http://'+THESITE+'/reloaded.php?do=channels',headers={'User-Agent' :UA}).content
    f = open(channeljs, mode='w')
    f.write(a)
    f.close()
    return a

def SearchProxy():

    addDir('[COLOR red]Disconnect From Proxy[/COLOR]','off**off',16012,'','','','',0)
    #<tr><td>89.197.56.246</td><td>8080</td><td>GB</td><td>United Kingdom</td><td>anonymous</td><td>no</td><td>yes</td><td>20 minutes ago</td>
    link= net.http_GET('http://free-proxy-list.net/uk-proxy.html').content
    match=re.compile('<tr><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>.+?</td><td>.+?</td><td>(.+?)</td><td>(.+?)</td>').findall(link)
    for ip , port , short , protocol, up in match:
        #if protocol=='no':
        name= '%s %s (%s)' % (ip,short,up)
        if getSetting('network.usehttpproxy')== True:
            if getSetting('network.httpproxyserver')== ip:
                name='[COLOR green]%s[/COLOR]' % name
                
        addDir(name,ip+'**'+port,16012,'','','','',0)

def ping(host):
    from platform import system as system_name # Returns the system/OS name
    from os import system as system_call       # Execute a shell command
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"

    # Pinging
    return system_call("ping " + parameters + " " + host) == 0


def AddProxy(url):
    ip=url.split('**')[0]
    port =url.split('**')[1]

    if ip=='off':
        setSetting('network.usehttpproxy', 'false')
        setSetting('network.httpproxyserver', ' ')
        setSetting('network.httpproxyport', ' ')
    else:
        if ping(ip):
            setSetting('network.usehttpproxy', 'true')
            setSetting('network.httpproxyserver', str(ip))
            setSetting('network.httpproxyport', str(port))
        else:
            dialog = xbmcgui.Dialog()
            dialog.ok(THESITE.upper(),'', "This IP %s Is Down" % ip, "")
    xbmc.executebuiltin("XBMC.Container.Refresh()")
         
def Tools():
    addDir('>>> [COLOR aliceblue]If you are seeing this section as soon as you login then delete cookie and start again[/COLOR] <<<','.f4m',202,'','','','',0)
    addDir('>>> [COLOR green]Open Addon Settings[/COLOR] <<<','.f4m',16008,'','','','',0)
    addDir('Check For Updates','.f4m',16005,'','','','',0)
    addDir('>>> [COLOR red]REFRESH CHANNELS LIST[/COLOR] <<<','.f4m',202,'','','','',0)
    addDir('Delete Cache','.f4m',16006,'','','','',0)
    

    addDir('Speed Test','.f4m',16001,'','','','',0)   
    addDir('Change Username or Password','.f4m',16002,'','','','',0)  


    if int(getSetting('videoplayer.stretch43'))<4:       
        addDir('Force 16:9 Video','.f4m',16004,'','','','videoplayer.stretch43',4)

        
    if getSetting('videoplayer.usedxva2')==True:      
        addDir('Disable Hardware Acceleration','.f4m',16004,'','','','videoplayer.usedxva2','false')
    else:      
        addDir('Enable Hardware Acceleration','.f4m',16004,'','','','videoplayer.usedxva2','true')
    addDir('Delete Cookie','.f4m',203,'','','','',0)

    

    

def changeEnableHLS():
    if ADDON.getSetting('hlsenable')=='true':
       change='false'
    else:
       change='true'
       
    ADDON.setSetting('hlsenable',change)
    xbmc.executebuiltin("Container.Refresh")
    

def CheckUpdate():
    dialog = xbmcgui.Dialog()
    link=OPEN_URL('https://raw.githubusercontent.com/Willowsportsmania/themaniaservices/master/plugin.video.sportsmania/addon.xml')
    match=re.compile('name="SportsMania" version="(.+?)"').findall(link)[0]
    if ADDON.getAddonInfo('version')==match:

        dialog.ok(THESITE.upper(),'', "You Are On Latest Version", "")
    else:   
        xbmc.executebuiltin('UpdateLocalAddons') 
        xbmc.executebuiltin("UpdateAddonRepos")
        dialog.ok(THESITE.upper(),'', "Updating Repo Now", "")
        

def Deletecache():
     dialog = xbmcgui.Dialog()
     packages_cache_path = xbmc.translatePath(os.path.join('special://home/addons/packages', ''))
   
     for root, dirs, files in os.walk(packages_cache_path):
         file_count = 0
         file_count += len(files)
         
     # Count files and give option to delete
         if file_count > 0:

             dialog = xbmcgui.Dialog()
             for f in files:
                 os.unlink(os.path.join(root, f))
             for d in dirs:
                 shutil.rmtree(os.path.join(root, d))


     xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
     if os.path.exists(xbmc_cache_path)==True:    
         for root, dirs, files in os.walk(xbmc_cache_path):
             file_count = 0
             file_count += len(files)
        
         # Count files and give option to delete
             if file_count > 0:

                  for f in files:
                      if not '.db' in f:
                         try:
                             os.unlink(os.path.join(root, f))
                         except:
                             pass
                  for d in dirs:
                      if not '.db' in f:     
                         try:
                             shutil.rmtree(os.path.join(root, d))
                         except:
                             pass
 
     xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'temp')
     if os.path.exists(xbmc_cache_path)==True:    
         for root, dirs, files in os.walk(xbmc_cache_path):
             file_count = 0
             file_count += len(files)
        
         # Count files and give option to delete
             if file_count > 0:
 
                 
                  for f in files:
                      try:
                          os.unlink(os.path.join(root, f))
                      except:
                          pass
                  for d in dirs:
                      try:
                          shutil.rmtree(os.path.join(root, d))
                      except:
                          pass
     dialog.ok(THESITE.upper(),'', "All Done And Deleted", "")


def addDir(name,url,mode,iconimage,play,date,description,page=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&play="+urllib.quote_plus(play)+"&date="+urllib.quote_plus(date)+"&description="+urllib.quote_plus(description)+"&page="+str(page)
        #printname.replace('-[US]','').replace('-[EU]','').replace('[COLOR yellow]','').replace('[/COLOR]','').replace(' (G)','')+'='+u
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Premiered":date,"Plot":description} )
        menu=[]
        menu.append(('[COLOR green]Refresh Channel List[/COLOR]','XBMC.RunPlugin(%s?mode=202&url=None)'% (sys.argv[0])))
        menu.append(('[COLOR blue]Reset Password[/COLOR]','XBMC.RunPlugin(%s?mode=2008&url=None)'% (sys.argv[0])))
        menu.append(('[COLOR red]Delete Cookie[/COLOR]','XBMC.RunPlugin(%s?mode=203&url=None)'% (sys.argv[0])))
        menu.append(('[COLOR cyan]Log Out[/COLOR]','XBMC.RunPlugin(%s?mode=205&url=None)'% (sys.argv[0])))
        liz.addContextMenuItems(items=menu, replaceItems=False)
        if mode == 2 or mode==7  or mode==2004 or mode==3002 or mode==16001 or mode==16002 or mode==16003 or mode==16004 or mode==16005 or mode==16006 or mode==203 or mode==202 or mode==16008 or mode==16012:
            if not mode == 2000:
                if not '.f4m' in url:
                    liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
          
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok




def addLink(name,url,iconimage, fanart):
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable","true")
        liz.setProperty("Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)

        
def setView(content, viewType):
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type
                      
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
date=None
description=None
page=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:
        play=urllib.unquote_plus(params["play"])
except:
        pass
try:
        date=urllib.unquote_plus(params["date"])
except:
        pass
try:
        description=urllib.unquote_plus(params["description"])
except:
        pass
try:        
        page=int(params["page"])
except:
        try:        
               page=params["page"]
        except:
               pass
   
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        try:CATEGORIES()
        except:Tools()

elif mode==2:
        PLAY_STREAM(name,url,iconimage,play,description)
        
elif mode==3:
        REPLAY()
        
elif mode==4:
        GENRES(name,url)

elif mode==5:
        OnDemand(url)


elif mode==6:
        OnDemandLinks(url)

elif mode==7:
        PlayOnDemand(url)         
        
elif mode==200:
        schedule(name,url,iconimage)
        
elif mode==201:
        fullguide(name,url,iconimage,description)
        
elif mode==202:
        RefreshChannels()
        Show_Dialog()
        
elif mode==203:
   
        try:os.remove(cookie_jar)
        except:pass
        try:os.remove(cookie_amember)
        except:pass
        Show_Dialog()

elif mode==204:
        downloadchannel()      
        
elif mode==205:
        LOGOUT()


elif mode==501:
        worldlinks(name,url)  
        

elif mode==1999:
        EVENTS()        
        
elif mode==2001:
        ADDON.openSettings()

elif mode==2003:
        parseAPI(url)

elif mode==20003:
        SportsOnDemand(url) 
        
elif mode==2004:
        playAPI(name,url,iconimage)
        
elif mode==2005:
        schedule(url)

elif mode==2006:
        PremPass(url)

elif mode==2007:
        checksub()

elif mode==2008:
     resetpass()        

elif mode==2009:
     TryAgain()
     
elif mode==3000:
     SEARCH(url)

elif mode==3001:
     GetSearchLinks(name,url,iconimage,description)      


elif mode==3010:
     GetEpisodeLinks(name,url,iconimage,description) 

elif mode==3002:
     PLAY_DEMAND_STREAM(name,url,iconimage,description)

elif mode==3003:
     MySearch()

elif mode == 3004:
    
    favs = ADDON.getSetting('favs').split(",")
    try:
        favs.remove(name.lower())
        ADDON.setSetting('favs', ",".join(favs))
    except:pass

elif mode == 4000:
    OnDemandFirstCat()

elif mode == 4001:
    OnDemandSecondCat(url)

elif mode == 4002:
    OnDemandThirdCat(url,page)      
    
elif mode==10000:
     import update

    
elif mode==11000:
     import skininstall    

elif mode==12000:
     xbmc.executebuiltin('ActivateWindow(videos,plugin://script.icechannel)')
     
elif mode==16000:
     Tools()
     
elif mode==16001:
     import speedtest

elif mode==16002:
     ADDON.openSettings()

elif mode==16003:
     changeEnableHLS()

elif mode==16004:
     setSetting(description, page)
     
elif mode==16005:
     CheckUpdate()

elif mode==16006:
     Deletecache()

elif mode==16011:
     SearchProxy()

elif mode==16012:
     AddProxy(url)
     
else:
        #just in case mode is invalid 
        try:CATEGORIES()
        except:Tools()

               
xbmcplugin.endOfDirectory(int(sys.argv[1]))


