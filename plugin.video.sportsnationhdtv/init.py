import urllib , urllib2 , sys , re , xbmcplugin , xbmcgui , xbmcaddon , datetime , os , json , base64 , plugintools , calendar , time , hashlib
import xml . etree . ElementTree as ElementTree
reload ( sys )
sys . setdefaultencoding ( 'utf8' )
oo000 = "515"
ii = plugintools . get_runtime_path ( )
global oOOo
O0 = "YmFja2dyb3VuZC5qcGc="
o0O = "ZGVmYXVsdGxvZ28ucG5n"
iI11I1II1I1I = "aG9tZXRoZWF0ZXIuanBn"
oooo = "bm9wb3N0ZXIuanBn"
iIIii1IIi = "dGhlYXRlci5qcGc="
o0OO00 = "YWRkb24ueG1s"
oo = "ZGVmYXVsdC5weQ=="
i1iII1IiiIiI1 = "aWNvbi5wbmc="
iIiiiI1IiI1I1 = "ZmFuYXJ0LnBuZw=="
o0OoOoOO00 = "VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"
# Entry point
def I11i ( ) :
 global pnimi
 global televisioonilink
 global filmilink
 global andmelink
 global uuenduslink
 global lehekylg
 global LOAD_LIVE
 global vanemalukk
 global version
 global tvlink
 global tvseries
 global tvkategoorialink
 global arhiivilink
 global striimiv2ljund
 global tvshows
 version = int ( O0O ( "Mw==" ) )
 Oo = plugintools . get_setting ( O0O ( "a2FzdXRhamFuaW1p" ) )
 if not Oo :
  plugintools . open_settings_dialog ( )
  Oo = plugintools . get_setting ( O0O ( "a2FzdXRhamFuaW1p" ) )
 I1ii11iIi11i = plugintools . get_setting ( I1IiI ( "c2FsYXNvbmE=" ) )
 lehekylg = o0OOO ( "aHR0cDovL21hbmlhLnNlcnZpY2Vz" )
 iIiiiI = o0OOO ( "MjU0NjE=" )
 tvshows = o0OOO ( "YmFja2dyb3VuZC5qcGc=" )
 vanemalukk = plugintools . get_setting ( o0OOO ( "dmFuZW1hbHVraw==" ) )
 striimiv2ljund = plugintools . get_setting ( o0OOO ( "c3RyaWltaXYybGp1bmQ=" ) )
 pnimi = O0O ( "TWFuaWEgSEQ=" )
 LOAD_LIVE = os . path . join ( plugintools . get_runtime_path ( ) , O0O ( "cmVzb3VyY2Vz" ) , I1IiI ( "YXJ0" ) )
 plugintools . log ( pnimi + O0O ( "U3RhcnRpbmcgdXA=" ) )
 televisioonilink = O0O ( "JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9jYXRlZ29yaWVz" ) % ( lehekylg , iIiiiI , Oo , I1ii11iIi11i )
 filmilink = I1IiI ( "JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX2NhdGVnb3JpZXM=" ) % ( lehekylg , iIiiiI , Oo , I1ii11iIi11i )
 andmelink = I1IiI ( "JXM6JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw==" ) % ( lehekylg , iIiiiI , Oo , I1ii11iIi11i )
 uuenduslink = O0O ( "aHR0cHM6Ly93d3cuZHJvcGJveC5jb20vcy9wb3dieGswZDBieDgxNzkva2luZ1ZlcnNpb24udHh0P2RsPTE=" )
 tvlink = I1IiI ( "JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX2NhdGVnb3JpZXM=" ) % ( lehekylg , iIiiiI , Oo , I1ii11iIi11i )
 tvseries = I1IiI( "JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfc2VyaWVzX2NhdGVnb3JpZXM=" ) % (lehekylg, iIiiiI, Oo, I1ii11iIi11i )
 arhiivilink = I1IiI ( "JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM=" ) % ( lehekylg , iIiiiI , Oo , I1ii11iIi11i )
 if O0O ( "TWFuaWEgSEQ=" ) not in open ( ii + "/" + o0OOO ( "YWRkb24ueG1s" ) ) . read ( ) :
  Iii1ii1II11i ( )
  if 10 - 10: I1iII1iiII + I1Ii111 / OOo
 params = plugintools . get_params ( )
 if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
 if params . get ( "action" ) is None :
  o0oOoO00o ( params )
 else :
  i1 = params . get ( "action" )
  exec i1 + "(params)"
  if 64 - 64: ooO0Oooo00 % Ooo0
 plugintools . close_item_list ( )
 if 89 - 89: I111i1i1111i - Ii1Ii1iiii11 % I1I1i1
def o0oOoO00o ( params ) :
 plugintools . log ( pnimi + I1IiI ( "TWFpbiBNZW51" ) + repr ( params ) )
 #IiI1i ( )
 if not lehekylg :
  plugintools . open_settings_dialog ( )
 OOo0o0 = oOOo ( )
 ii11i1i1ii00ooo00o0o0o0o = (time.strftime("%d/%m/%Y"))
 #gksie0s011saew ( )
 if OOo0o0 == 1 :
  plugintools . log ( pnimi + I1IiI ( "TG9naW4gU3VjY2Vzcw==" ) )
  plugintools . add_item( action = "maintenance", title = I1IiI ("TWFpbnRlbmFuY2UgVG9vbHMgIChVbmRlciBEZXZlbG9wbWVudCk="), thumbnail = os.path.join(LOAD_LIVE, o0OOO("")), fanart = os . path . join ( LOAD_LIVE , I1IiI ( "bWFpbnRlbmFuY2UucG5n" ) ) , folder = False)
  plugintools . add_item ( action = "O0ooo0O0oo0" , title = I1IiI ( "TXkgQWNjb3VudA==" ) , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "YWNjb3VudF9pY29uLnBuZw==" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = True )
  plugintools . add_item ( action = "OoOo" , title = I1IiI ( "TGl2ZSBUVg==" ) , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bGl2ZV9pY29uLnBuZw==" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = True )
  plugintools . add_item ( action = "O0O00o0OOO0" , title = I1IiI ( "VmlkZW8gT24gRGVtYW5k" ) , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "dm9kX2ljb24ucG5n" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = True )
  plugintools . add_item ( action = "O0O00o0OOO02" , title = I1IiI ( "VFYgU2VyaWVz" ) , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = True )
  plugintools . add_item ( action = "oo00O00oO" , title = I1IiI ( "TWFuaWEgSEQgQ2F0Y2h1cCAgKFVuZGVyIERldmVsb3BtZW50KQ==" ) , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "YXJjaGl2ZV9pY29uLnBuZw==" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = True )
  plugintools . add_item ( action = "i1I111I" , title = I1IiI ( "U2V0dGluZ3M=" ) , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "c2V0dGluZ3NfaWNvbi5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = False )
  plugintools . add_item ( action = "speedTest" , title = I1IiI ( "SW50ZXJuZXQgU3BlZWQgVGVzdA==" ) , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "c3BlZWR0ZXN0LnBuZw==" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "c3BlZWRiZy5wbmc=" ) ) , folder = False )
  plugintools . set_view ( plugintools . LIST )
 else :
  plugintools . log ( pnimi + I1IiI ( "TG9naW4gZmFpbGVk" ) )
  plugintools . message ( I1IiI ( "TG9naW4gZmFpbGVk" ) , I1IiI ( "UG9zc2libGUgcmVhc29uczogV3JvbmcgaG9zdCxwb3J0LHVzZXJuYW1lIG9yIHBhc3MuICAgICAgICAgIFBsZWFzZSByZWNvbmZpZ3VyZSAlcyBwbHVnaW4gd2l0aCBjb3JyZWN0IGRldGFpbHMh" ) % ( pnimi ) )
  plugintools . open_settings_dialog ( )
  #Oo = plugintools . get_setting ( O0O ( "a2FzdXRhamFuaW1p" ) )
  #I1ii11iIi11i = plugintools . get_setting ( I1IiI ( "c2FsYXNvbmE=" ) )
  I11i ( )
 if plugintools . get_setting ( "improve" ) == "true" :
  O0OoOoo00o = xbmc . translatePath ( o0OOO ( "c3BlY2lhbDovL3VzZXJkYXRhL2FkdmFuY2Vkc2V0dGluZ3MueG1s" ) )
  if not os . path . exists ( O0OoOoo00o ) :
   file = open ( os . path . join ( plugintools . get_runtime_path ( ) , I1IiI ( "cmVzb3VyY2Vz" ) , o0OOO ( "YWR2YW5jZWRzZXR0aW5ncy54bWw=" ) ) )
   iiiI11 = file . read ( )
   file . close ( )
   file = open ( O0OoOoo00o , "w" )
   file . write ( iiiI11 )
   file . close ( )
   plugintools . message ( pnimi , O0O ( "TmV3IGFkdmFuY2VkIHN0cmVhbWluZyBzZXR0aW5ncyBhZGRlZC4=" ) )
   if 91 - 91: oOOOO / i1iiIII111ii + iiIIi1IiIi11 . i1Ii
   if 25 - 25: OO00O0O0O00Oo + OOoooooO / Oo0ooO0oo0oO . oOOOO % Oo0oO0ooo . Ooo0
def i1I111I ( params ) :
 plugintools . log ( pnimi + O0O ( "U2V0dGluZ3MgbWVudQ==" ) + repr ( params ) )
 plugintools . open_settings_dialog ( )
 if 1 - 1: i1Ii % Oo0oO0ooo * oOOOO
def O0O00o0OOO0 ( params ) :
 plugintools . log ( pnimi + I1IiI ( "Vk9EIE1lbnUg" ) + repr ( params ) )
 IiIiIi = urllib2 . Request ( filmilink , headers = { "Accept" : "application/xml" } )
 II = urllib2 . urlopen ( IiIiIi )
 iI = ElementTree . parse ( II )
 iI11iiiI1II = iI . getroot ( )
 for O0oooo0Oo00 in iI . findall ( o0OOO ( "Y2hhbm5lbA==" ) ) :
  Ii1iIIIi1ii = O0oooo0Oo00 . find ( O0O ( "dGl0bGU=" ) ) . text
  if Ii1iIIIi1ii == "QWxs" :
     continue
  Ii1iIIIi1ii = base64 . b64decode ( Ii1iIIIi1ii )
  oOo00Oo00O = O0oooo0Oo00 . find ( I1IiI ( "cGxheWxpc3RfdXJs" ) ) . text
  if "scat_id" in oOo00Oo00O:
    plugintools.log("IS SUBCAT!")
    plugintools . add_item ( action = "I11i1I1I" , title = Ii1iIIIi1ii, url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = True )
  else:
    plugintools . add_item ( action = I1IiI ( "T29PbzAwbw==" ) , title = Ii1iIIIi1ii , url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "dGhlYXRlci5qcGc=" ) ) , folder = True )
 plugintools . set_view ( plugintools . LIST )
 if 80 - 80: oOOOO * I1iII1iiII / OO00O0O0O00Oo

def O0O00o0OOO02 ( params ) :
 plugintools . log ( pnimi + I1IiI ( "Vk9EIE1lbnUg" ) + repr ( params ) )
 IiIiIi = urllib2 . Request ( tvseries , headers = { "Accept" : "application/xml" } )
 II = urllib2 . urlopen ( IiIiIi )
 iI = ElementTree . parse ( II )
 iI11iiiI1II = iI . getroot ( )
 for O0oooo0Oo00 in iI . findall ( o0OOO ( "Y2hhbm5lbA==" ) ) :
  Ii1iIIIi1ii = O0oooo0Oo00 . find ( O0O ( "dGl0bGU=" ) ) . text
  if Ii1iIIIi1ii == "QWxs" :
     continue
  Ii1iIIIi1ii = base64 . b64decode ( Ii1iIIIi1ii )
  oOo00Oo00O = O0oooo0Oo00 . find ( I1IiI ( "cGxheWxpc3RfdXJs" ) ) . text
  if "scat_id" in oOo00Oo00O:
    plugintools.log("IS SUBCAT!")
    plugintools . add_item ( action = "I11i1I1I" , title = Ii1iIIIi1ii, url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = True )
  else:
    plugintools . add_item ( action = "O0O00o0OOO03" , title = Ii1iIIIi1ii , url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "dGhlYXRlci5qcGc=" ) ) , folder = True )
 plugintools . set_view ( plugintools . LIST )
 if 80 - 80: oOOOO * I1iII1iiII / OO00O0O0O00Oo

def O0O00o0OOO03 ( params ) :
 plugintools . log ( pnimi + I1IiI ( "Vk9EIE1lbnUg" ) + repr ( params ) )
 o0OOoo0OO0OOO = params.get(O0O("dXJs"))
 IiIiIi = urllib2 . Request ( o0OOoo0OO0OOO , headers = { "Accept" : "application/xml" } )
 II = urllib2 . urlopen ( IiIiIi )
 iI = ElementTree . parse ( II )
 iI11iiiI1II = iI . getroot ( )
 for O0oooo0Oo00 in iI . findall ( o0OOO ( "Y2hhbm5lbA==" ) ) :
  Ii1iIIIi1ii = O0oooo0Oo00 . find ( O0O ( "dGl0bGU=" ) ) . text
  if Ii1iIIIi1ii == "QWxs" :
     continue
  Ii1iIIIi1ii = base64 . b64decode ( Ii1iIIIi1ii )
  oOo00Oo00O = O0oooo0Oo00 . find ( I1IiI ( "cGxheWxpc3RfdXJs" ) ) . text
  if "scat_id" in oOo00Oo00O:
    plugintools.log("IS SUBCAT!")
    plugintools . add_item ( action = "I11i1I1I" , title = Ii1iIIIi1ii, url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = True )
  else:
    plugintools . add_item ( action = "O0O00o0OOO04" , title = Ii1iIIIi1ii , url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "dGhlYXRlci5qcGc=" ) ) , folder = True )
 plugintools . set_view ( plugintools . LIST )
 if 80 - 80: oOOOO * I1iII1iiII / OO00O0O0O00Oo

def O0O00o0OOO04 ( params ) :
 plugintools . log ( pnimi + I1IiI ( "Vk9EIE1lbnUg" ) + repr ( params ) )
 o0OOoo0OO0OOO = params.get(O0O("dXJs"))
 IiIiIi = urllib2 . Request ( o0OOoo0OO0OOO , headers = { "Accept" : "application/xml" } )
 II = urllib2 . urlopen ( IiIiIi )
 iI = ElementTree . parse ( II )
 iI11iiiI1II = iI . getroot ( )
 for O0oooo0Oo00 in iI . findall ( o0OOO ( "Y2hhbm5lbA==" ) ) :
  Ii1iIIIi1ii = O0oooo0Oo00 . find ( O0O ( "dGl0bGU=" ) ) . text
  if Ii1iIIIi1ii == "QWxs" :
     continue
  Ii1iIIIi1ii = base64 . b64decode ( Ii1iIIIi1ii )
  oOo00Oo00O = O0oooo0Oo00 . find ( I1IiI ( "cGxheWxpc3RfdXJs" ) ) . text
  if "scat_id" in oOo00Oo00O:
    plugintools.log("IS SUBCAT!")
    plugintools . add_item ( action = "I11i1I1I" , title = Ii1iIIIi1ii, url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = True )
  else:
    #OOO0OOo
    plugintools . add_item ( action = I1IiI ( "T29PbzAwbw==" ) , title = Ii1iIIIi1ii , url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "dGhlYXRlci5qcGc=" ) ) , folder = True )
 plugintools . set_view ( plugintools . LIST )
 if 80 - 80: oOOOO * I1iII1iiII / OO00O0O0O00Oo

def OoOo ( params ) :
 plugintools . log ( pnimi + o0OOO ( "TGl2ZSBNZW51" ) + repr ( params ) )
 IiIiIi = urllib2 . Request ( televisioonilink , headers = { "Accept" : "application/xml" } )
 II = urllib2 . urlopen ( IiIiIi )
 iI = ElementTree . parse ( II )
 iI11iiiI1II = iI . getroot ( )
 for O0oooo0Oo00 in iI . findall ( o0OOO ( "Y2hhbm5lbA==" ) ) :
  Ii11iii11I = O0oooo0Oo00 . find ( O0O ( "dGl0bGU=" ) ) . text
  Ii11iii11I = base64 . b64decode ( Ii11iii11I )
  oOo00Oo00O = O0oooo0Oo00 . find ( I1IiI ( "cGxheWxpc3RfdXJs" ) ) . text
  plugintools . add_item ( action = O0O ( "STExSUkxaQ==" ) , title = Ii11iii11I , url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "dGhlYXRlci5qcGc=" ) ) , folder = True )
 plugintools . set_view ( plugintools . LIST )
 if 43 - 43: o00ooo0 - iiIIi1IiIi11 * OOo
def I11II1i ( params ) :
 plugintools . log ( pnimi + o0OOO ( "TGl2ZSBDaGFubmVscyBNZW51IA==" ) + repr ( params ) )
 if O0O ( "TWFuaWEgSEQ=" ) not in open ( ii + "/" + o0OOO ( "YWRkb24ueG1s" ) ) . read ( ) :
  Iii1ii1II11i ( )
 if vanemalukk == "true" :
  IIIII = params . get ( o0OOO ( "dGl0bGU=" ) )
  ooooooO0oo ( IIIII )
 IIiiiiiiIi1I1 = params . get ( O0O ( "dXJs" ) )
 IiIiIi = urllib2 . Request ( IIiiiiiiIi1I1 , headers = { "Accept" : "application/xml" } )
 II = urllib2 . urlopen ( IiIiIi )
 iI = ElementTree . parse ( II )
 iI11iiiI1II = iI . getroot ( )
 for O0oooo0Oo00 in iI . findall ( o0OOO ( "Y2hhbm5lbA==" ) ) :
  Ii11iii11I = O0oooo0Oo00 . find ( O0O ( "dGl0bGU=" ) ) . text
  Ii11iii11I = base64 . b64decode ( Ii11iii11I )
  Ii11iii11I = Ii11iii11I . partition ( "[" )
  I1IIIii = O0oooo0Oo00 . find ( O0O ( "c3RyZWFtX3VybA==" ) ) . text
  oOoOooOo0o0 = O0oooo0Oo00 . find ( I1IiI ( "ZGVzY19pbWFnZQ==" ) ) . text
  OOOO = Ii11iii11I [ 1 ] + Ii11iii11I [ 2 ]
  OOOO = OOOO . partition ( "]" )
  OOOO = OOOO [ 2 ]
  OOOO = OOOO . partition ( "min" )
  plugintools.log(OOOO[0]+" "+ OOOO[1]+" "+ OOOO[2])
  OOOO = OOOO [ 2 ]
  OOO00 = O0O ( "W0NPTE9SIGdyZXldJXMgWy9DT0xPUl0=" ) % ( Ii11iii11I [ 0 ] ) + OOOO
  iiiiiIIii = O0oooo0Oo00 . find ( o0OOO ( "ZGVzY3JpcHRpb24=" ) ) . text
  if iiiiiIIii :
   iiiiiIIii = base64 . b64decode ( iiiiiIIii )
   O000OO0 = iiiiiIIii . partition ( "(" )
   O000OO0 = o0OOO ( "Tk9XOiA=" ) + O000OO0 [ 0 ]
   I11iii1Ii = iiiiiIIii . partition ( ")\n" )
   I11iii1Ii = I11iii1Ii [ 2 ] . partition ( "(" )
   I11iii1Ii = o0OOO ( "TkVYVDog" ) + I11iii1Ii [ 0 ]
   I1IIiiIiii = O000OO0 + I11iii1Ii
  else :
   I1IIiiIiii = ""
  if striimiv2ljund == "true":
   I1IIIii = I1IIIii .replace(".ts",".m3u8")
  if oOoOooOo0o0 :
   oOoOooOo0o0 = oOoOooOo0o0.strip()
   plugintools . add_item ( action = o0OOO ( "T09PME9Pbw==" ) , title = OOO00 , url = I1IIIii , thumbnail = oOoOooOo0o0 , plot = I1IIiiIiii , fanart = os . path . join ( LOAD_LIVE , I1IiI ( "aG9tZXRoZWF0ZXIuanBn" ) ) , extra = "" , isPlayable = True , folder = False )
  else :
   plugintools . add_item ( action = o0OOO ( "T09PME9Pbw==" ) , title = OOO00 , url = I1IIIii , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "ZGVmYXVsdGxvZ28ucG5n" ) ) , plot = I1IIiiIiii , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "aG9tZXRoZWF0ZXIuanBn" ) ) , extra = "" , isPlayable = True , folder = False )
 plugintools . set_view ( plugintools . EPISODES )
 #xbmc . executebuiltin ( I1IiI ( "Q29udGFpbmVyLlNldFZpZXdNb2RlKDU1KQ==" ) )
 if 97 - 97: OOoooooO - I1I1i1 * I1iII1iiII / ooO0Oooo00 % OO00O0O0O00Oo - o0OO0
def OoOo00o ( params ) :
 plugintools . log ( pnimi + O0O ( "Vk9EIGNoYW5uZWxzIG1lbnUg" ) + repr ( params ) )
 if vanemalukk == "true" :
  IIIII = params . get ( o0OOO ( "dGl0bGU=" ) )
  ooooooO0oo ( IIIII )
 o0OOoo0OO0OOO = params . get ( O0O ( "dXJs" ) )
 IiIiIi = urllib2 . Request ( o0OOoo0OO0OOO , headers = { "Accept" : "application/xml" } )
 II = urllib2 . urlopen ( IiIiIi )
 iI = ElementTree . parse ( II )
 iI11iiiI1II = iI . getroot ( )
 for O0oooo0Oo00 in iI . findall ( o0OOO ( "Y2hhbm5lbA==" ) ) :
  IIIII = O0oooo0Oo00 . find ( O0O ( "dGl0bGU=" ) ) . text
  IIIII = base64 . b64decode ( IIIII )
  IIIII = IIIII . encode ( "utf-8" )
  I1IIIii = O0oooo0Oo00 . find ( o0OOO ( "c3RyZWFtX3VybA==" ) ) . text
  oOoOooOo0o0 = O0oooo0Oo00 . find ( o0OOO ( "ZGVzY19pbWFnZQ==" ) ) . text
  iiiiiIIii = O0oooo0Oo00 . find ( I1IiI ( "ZGVzY3JpcHRpb24=" ) ) . text
  if iiiiiIIii :
   iiiiiIIii = base64 . b64decode ( iiiiiIIii )
  if iiiiiIIii is None :
    iiiiiIIii = ""
  if oOoOooOo0o0 is not None :
   plugintools . add_item ( action = "II11i1iIiII1" , title = IIIII , url = I1IIIii , thumbnail = oOoOooOo0o0 , plot = iiiiiIIii , fanart = os . path . join ( LOAD_LIVE , "theater.jpg" ) , extra = "" , isPlayable = True , folder = False )
  else :
   plugintools . add_item ( action = "II11i1iIiII1" , title = IIIII , url = I1IIIii , thumbnail = os . path . join ( LOAD_LIVE , "noposter.jpg" ) , plot = iiiiiIIii , fanart = "" , extra = "" , isPlayable = True , folder = False )
 plugintools . set_view ( plugintools . MOVIES )
 #xbmc . executebuiltin ( 'Container.SetViewMode(515)' )
 if 19 - 19: Ii1Ii1iiii11 % Oo0ooO0oo0oO % Ooo0
def oo0OooOOo0 ( params ) :
 plugintools . log ( pnimi + I1IiI ( "VFYgU2hvd3M=" ) + repr ( params ) )
 o0OOoo0OO0OOO = params . get ( O0O ( "dXJs" ) )
 ##TODO ADD
 IiIiIi = urllib2 . Request ( o0OOoo0OO0OOO , headers = { "Accept" : "application/xml" } )
 II = urllib2 . urlopen ( IiIiIi )
 iI = ElementTree . parse ( II )
 iI11iiiI1II = iI . getroot ( )
 o0OO00oO = 0
 for O0oooo0Oo00 in iI . findall ( o0OOO ( "Y2hhbm5lbA==" ) ) :
  Ii1iIIIi1ii = O0oooo0Oo00 . find ( O0O ( "dGl0bGU=" ) ) . text
  if Ii1iIIIi1ii == "YmFja2dyb3VuZC5qcGc=" :
   o0OO00oO = 1
   global tvkategoorialink
   tvkategoorialink = O0oooo0Oo00 . find ( I1IiI ( "cGxheWxpc3RfdXJs" ) ) . text
   I11i1I1I ( params )
   if 83 - 83: I111i1i1111i / OOoooooO
 if o0OO00oO == 0 :
  plugintools . message ( pnimi , "There are no TV series available" )
  if 49 - 49: Ooo0
def I11i1I1I ( params ) :
 plugintools . log ( pnimi + "Get tv show cats" + repr ( params ) )
 tvkategoorialink = params . get ( O0O ( "dXJs" ) )
 IiIiIi = urllib2 . Request ( tvkategoorialink , headers = { "Accept" : "application/xml" } )
 II = urllib2 . urlopen ( IiIiIi )
 iI = ElementTree . parse ( II )
 iI11iiiI1II = iI . getroot ( )
 for O0oooo0Oo00 in iI . findall ( o0OOO ( "Y2hhbm5lbA==" ) ) :
  Ii1iIIIi1ii = O0oooo0Oo00 . find ( O0O ( "dGl0bGU=" ) ) . text
  Ii1iIIIi1ii = base64 . b64decode ( Ii1iIIIi1ii )
  oOo00Oo00O = O0oooo0Oo00 . find ( I1IiI ( "cGxheWxpc3RfdXJs" ) ) . text
  plugintools . add_item ( action = I1IiI ( "T29PbzAwbw==" ) , title = Ii1iIIIi1ii , url = oOo00Oo00O , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "c2VyaWVzLmpwZw==" ) ) , folder = True )
 plugintools . set_view ( plugintools . LIST )
def gksie0s011saew ( ) :
 IIii1Ii1 = hashlib . md5 ( open ( ii + "/" + o0OOO ( "YWRkb24ueG1s" ) , 'rb' ) . read ( ) ) . hexdigest ( )
 I1II11IiII = I1IiI ( "NTJiNjdhYmE5MWM0ZTJhZjhhYmJjZmNlNTg2NmIzZTI=" )
 # if ( IIii1Ii1 != I1II11IiII ) :
 #  exit ( )
def OOO0OOo ( params ) :
 plugintools . log ( pnimi + o0OOO ( "UExBWV9MSVZF" ) + repr ( params ) )
 if vanemalukk == "true" :
  IIIII = params . get ( o0OOO ( "dGl0bGU=" ) )
  ooooooO0oo ( IIIII )
 I1I111 = params . get ( I1IiI ( "dXJs" ) )
 #I1I111 = "http://iptv.leeztv.com/relocate.php?loc=" + I1I111
 plugintools.log(I1I111)
 plugintools . play_resolved_url ( I1I111 )
def o0OOO ( channel ) :
 i11iiI111I = base64 . b64decode ( channel )
 return i11iiI111I
def II11i1iIiII1 ( params ) :
 plugintools . log ( pnimi + O0O ( "UExBWSBWT0Qg" ) + repr ( params ) )
 if vanemalukk == "true" :
  IIIII = params . get ( o0OOO ( "dGl0bGU=" ) )
  ooooooO0oo ( IIIII )
 I1I111 = params . get ( I1IiI ( "dXJs" ) )
 plugintools . play_resolved_url ( I1I111 )
def exit ( ) :
 plugintools . log ( I1IiI ( "WW91ciBrb2RpIHZlcnNpb24gaXMgb3V0ZGF0ZWQh" ) )
 sys . exit ( )
def iIi1iIiii111 ( ) :
 iIIIi1 = urllib2 . Request ( andmelink )
 iIIIi1 . add_header ( o0OOO ( "VXNlci1BZ2VudA==" ) , I1IiI ( "S29kaSBwbHVnaW4gYnkgTWlra00=" ) )
 iiII1i1 = urllib2 . urlopen ( iIIIi1 )
 o00oOO0o = iiII1i1 . read ( )
 OOO00O = json . loads ( o00oOO0o . decode ( 'utf8' ) )
 iiII1i1 . close ( )
 if OOO00O :
  plugintools . log ( pnimi + o0OOO ( "amRhdGEgbG9hZGVkIA==" ) )
  return OOO00O
def oOOo ( ) :
 OOoOO0oo0ooO = iIi1iIiii111 ( )
 O0o0O00Oo0o0 = OOoOO0oo0ooO [ o0OOO ( "dXNlcl9pbmZv" ) ]
 oOOo = O0o0O00Oo0o0 [ O0O ( "YXV0aA==" ) ]
 return oOOo
def O0O ( channel ) :
 i11iiI111I = base64 . b64decode ( channel )
 return i11iiI111I
 if 87 - 87: OOoooooO * o00 % I1iII1iiII % ooO0Oooo00 - I1I1i1
def speedTest( params ):
 import speedtest

def maintenance(params):
 return 1
def O0ooo0O0oo0 ( params ) :
 plugintools . log ( pnimi + O0O ( "TXkgYWNjb3VudCBNZW51IA==" ) + repr ( params ) )
 oo0oOo = iIi1iIiii111 ( )
 o000O0o = oo0oOo [ o0OOO ( "dXNlcl9pbmZv" ) ]
 iI1iII1 = o000O0o [ O0O ( "c3RhdHVz" ) ]
 oO0OOoo0OO = o000O0o [ o0OOO ( "ZXhwX2RhdGU=" ) ]
 if oO0OOoo0OO :
  oO0OOoo0OO = datetime . datetime . fromtimestamp ( int ( oO0OOoo0OO ) ) . strftime ( '%H:%M %d.%m.%Y' )
 else :
  oO0OOoo0OO = I1IiI ( "TmV2ZXI=" )
 O0ii1ii1ii = o000O0o [ I1IiI ( "aXNfdHJpYWw=" ) ]
 if O0ii1ii1ii == "0" :
  O0ii1ii1ii = o0OOO ( "Tm8=" )
 else :
  O0ii1ii1ii = o0OOO ( "WWVz" )
 oooooOoo0ooo = o000O0o [ O0O ( "bWF4X2Nvbm5lY3Rpb25z" ) ]
 I1I1IiI1 = o000O0o [ o0OOO ( "dXNlcm5hbWU=" ) ]
 plugintools . add_item ( action = "" , title = o0OOO ( "W0NPTE9SID0gd2hpdGVdVXNlcjogWy9DT0xPUl0=" ) + I1I1IiI1 , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) )  , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = False )
 plugintools . add_item ( action = "" , title = o0OOO ( "W0NPTE9SID0gd2hpdGVdU3RhdHVzOiBbL0NPTE9SXQ==" ) + iI1iII1 , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) )  , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = False )
 plugintools . add_item ( action = "" , title = O0O ( "W0NPTE9SID0gd2hpdGVdRXhwaXJlczogWy9DT0xPUl0=" ) + oO0OOoo0OO , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) )  , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = False )
 plugintools . add_item ( action = "" , title = I1IiI ( "W0NPTE9SID0gd2hpdGVdVHJpYWwgYWNjb3VudDogWy9DT0xPUl0=" ) + O0ii1ii1ii , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) )  , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = False )
 plugintools . add_item ( action = "" , title = I1IiI ( "W0NPTE9SID0gd2hpdGVdTWF4IGNvbm5lY3Rpb25zOiBbL0NPTE9SXQ==" ) + oooooOoo0ooo , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) )  , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "YmFja2dyb3VuZC5qcGc=" ) ) , folder = False )
 plugintools . set_view ( plugintools . LIST )
 #xbmc . executebuiltin ( I1IiI ( "Q29udGFpbmVyLlNldFZpZXdNb2RlKDU1KQ==" ) )
def ooooooO0oo ( name ) :
 plugintools . log ( pnimi + o0OOO ( "UGFyZW50YWwgbG9jayA=" ) )
 III1iII1I1ii = 'XXX' , 'Adult' , 'Adults' , 'ADULT' , 'ADULTS' , 'adult' , 'adults' , 'Porn' , 'PORN' , 'porn' , 'Porn' , 'xxx'
 if any ( s in name for s in III1iII1I1ii ) :
  xbmc . executebuiltin ( ( u'XBMC.Notification("Parental Lock", "Channels may contain adult content", 2000)' ) )
  oOOo0 = plugintools . keyboard_input ( default_text = "" , title = O0O ( "UGFyZW50YWwgbG9jaw==" ) )
  if oOOo0 == plugintools . get_setting ( o0OOO ( "dmFuZW1ha29vZA==" ) ) :
   return
  else :
   exit ( )
 else :
  name = ""
def Iii1ii1II11i ( ) :
 plugintools . message ( O0O ( "RVJST1I=" ) , I1IiI ( "VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h" ) )
 sys . exit ( )
def oo00O00oO ( params ) :
 #tv archive cat
 iIiIIIi = urllib2 . urlopen ( andmelink )
 ooo00OOOooO = json . load ( iIiIIIi )
 O00OOOoOoo0O = ooo00OOOooO [ 'available_channels' ]
 for O000OOo00oo in O00OOOoOoo0O . values ( ) :
  oo0OOo = O000OOo00oo [ 'tv_archive' ]
  if ( oo0OOo == 1 ) :
   ooOOO00Ooo = O000OOo00oo [ 'name' ]
   IiIIIi1iIi = O000OOo00oo [ 'stream_id' ]
   plugintools . add_item ( action = "IIII" , title = ooOOO00Ooo , url = IiIIIi1iIi , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "dHZjLmpwZw==" ) ) , isPlayable = False , folder = True )
def ooOOoooooo ( params ) :
 plugintools . log ( pnimi + " TESTING" + repr ( params ) )
 #gksie0s011saew ( )
 II1I = params . get ( I1IiI ( "dXJs" ) )
 II1I = II1I . split ( "#" )
 IiIIIi1iIi = II1I [ 0 ]
 O0i1II1Iiii1I11 = II1I [ 1 ]
 I1I111 = arhiivilink + "&stream=" + IiIIIi1iIi + "&duration=120" + "&start=" + O0i1II1Iiii1I11
 plugintools . log ( "Lopplink " + I1I111 )
 plugintools . play_resolved_url ( I1I111 )
def IIII ( params ) :
 #tv archive list
 IiIIIi1iIi = params . get ( I1IiI ( "dXJs" ) )
 IIiiiiiiIi1I1 = andmelink + "&action=get_epg&stream_id=" + IiIIIi1iIi
 iIiIIIi = urllib2 . urlopen ( IIiiiiiiIi1I1 )
 iiiI11 = json . load ( iIiIIIi )
 iiIiI = datetime . datetime . utcnow ( ) - datetime . timedelta ( days = 3 )
 o00oooO0Oo = calendar . timegm ( iiIiI . timetuple ( ) )
 o00oooO0Oo = int ( o00oooO0Oo )
 o0O0OOO0Ooo = time . time ( )
 o0O0OOO0Ooo = int ( o0O0OOO0Ooo )
 for iiIiII1 in iiiI11 :
  OOO00O0O = iiIiII1 [ 'title' ]
  OOO00O0O = base64 . b64decode ( OOO00O0O )
  iii = int ( iiIiII1 [ 'start' ] )
  if ( iii > o00oooO0Oo and iii < o0O0OOO0Ooo ) :
   if 90 - 90: Ooo0 % Oo0ooO0oo0oO / Oo0oO0ooo
   IIi = datetime . datetime . fromtimestamp ( int ( iii ) ) . strftime ( '%d.%m %H:%M' )
   i1Iii1i1I = datetime . datetime . fromtimestamp ( int ( iii ) ) . strftime ( '%Y-%m-%d:%H-%M' )
   OOO00O0O = IIi + " " + OOO00O0O
   II1I = IiIIIi1iIi + "#" + i1Iii1i1I
   plugintools . add_item ( action = "ooOOoooooo" , title = OOO00O0O , url = II1I , thumbnail = os . path . join ( LOAD_LIVE , o0OOO ( "bG9nby5wbmc=" ) ) , fanart = os . path . join ( LOAD_LIVE , o0OOO ( "dHZjLmpwZw==" ) ) , isPlayable = True , folder = False )
#def IiI1i ( ) :
 #gksie0s011saew ( )
def I1IiI ( channel ) :
 i11iiI111I = base64 . b64decode ( channel )
 return i11iiI111I
I11i ( ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
