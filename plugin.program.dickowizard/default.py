#

import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys
import urllib, urllib2, re, glob
import shutil
import extras
import extract
import addonfix
import addons
import communitybuilds
import CheckPath
import cache
import time
import downloader
import plugintools
import zipfile
import ntpath


ARTPATH      =  'special://home/resources/art/' + os.sep
ADDON        =  xbmcaddon.Addon(id='plugin.program.dickowizard')
AddonID      =  'plugin.program.dickowizard'
AddonTitle   =  "SportsMania Wizard"
zip          =  ADDON.getSetting('zip')
localcopy    =  ADDON.getSetting('localcopy')
privatebuilds=  ADDON.getSetting('private')
reseller     =  ADDON.getSetting('reseller')
resellername =  ADDON.getSetting('resellername')
resellerid   =  ADDON.getSetting('resellerid')
mastercopy   =  ADDON.getSetting('mastercopy')
username     =  ADDON.getSetting('username')
password     =  ADDON.getSetting('password')
login        =  ADDON.getSetting('login')
trcheck      =  ADDON.getSetting('trcheck')
dialog       =  xbmcgui.Dialog()
dp           =  xbmcgui.DialogProgress()
HOME         =  xbmc.translatePath('special://home/')
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
MEDIA        =  xbmc.translatePath(os.path.join('special://home/media',''))
AUTOEXEC     =  xbmc.translatePath(os.path.join(USERDATA,'autoexec.py'))
AUTOEXECBAK  =  xbmc.translatePath(os.path.join(USERDATA,'autoexec_bak.py'))
ADDON_DATA   =  xbmc.translatePath(os.path.join(USERDATA,'addon_data'))
PLAYLISTS    =  xbmc.translatePath(os.path.join(USERDATA,'playlists'))
databasePath = xbmc.translatePath('special://userdata/Database')
MaintTitle="SportsMania Wizard"
thumbnailPath = xbmc.translatePath('special://userdata/Thumbnails');
ADDONS       =  xbmc.translatePath(os.path.join('special://home','addons',''))
cachePath = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath = xbmc.translatePath('special://temp')
CBADDONPATH  =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'default.py'))
FANART       =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'fanart.jpg'))
GUISETTINGS  =  os.path.join(USERDATA,'guisettings.xml')
GUI          =  xbmc.translatePath(os.path.join(USERDATA,'guisettings.xml'))
GUIFIX       =  xbmc.translatePath(os.path.join(USERDATA,'guifix.xml'))
INSTALL      =  xbmc.translatePath(os.path.join(USERDATA,'install.xml'))
FAVS         =  xbmc.translatePath(os.path.join(USERDATA,'favourites.xml'))
SOURCE       =  xbmc.translatePath(os.path.join(USERDATA,'sources.xml'))
ADVANCED     =  xbmc.translatePath(os.path.join(USERDATA,'advancedsettings.xml'))
PROFILES     =  xbmc.translatePath(os.path.join(USERDATA,'profiles.xml'))
RSS          =  xbmc.translatePath(os.path.join(USERDATA,'RssFeeds.xml'))
KEYMAPS      =  xbmc.translatePath(os.path.join(USERDATA,'keymaps','keyboard.xml'))
USB          =  xbmc.translatePath(os.path.join(zip))
CBPATH       =  xbmc.translatePath(os.path.join(USB,'Community Builds',''))
cookiepath   =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'cookiejar'))
startuppath  =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'startup.xml'))
tempfile     =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'temp.xml'))
idfile       =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'id.xml'))
idfiletemp   =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'idtemp.xml'))
notifyart    =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'resources/'))
skin         =  xbmc.getSkinDir()
userdatafolder = xbmc.translatePath(os.path.join(ADDON_DATA,AddonID))
GUINEW       =  xbmc.translatePath(os.path.join(userdatafolder,'guinew.xml'))
guitemp      =  xbmc.translatePath(os.path.join(userdatafolder,'guitemp',''))
tempdbpath   =  xbmc.translatePath(os.path.join(USB,'Database'))
urlbase      =  'None'
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
base='@kodienthusiasts/'
VERSION = "2.0.4"
PATH = "SportsMania Wizard" 

#-----------------------------------------------------------------------------------------------------------------
#Addon removal menu
def Addon_Removal_Menu():
    for file in glob.glob(os.path.join(ADDONS,'*')):
        name=str(file).replace(ADDONS,'[COLOR=red]REMOVE [/COLOR]').replace('plugin.','[COLOR=dodgerblue](PLUGIN) [/COLOR]').replace('audio.','').replace('video.','').replace('skin.','[COLOR=yellow](SKIN) [/COLOR]').replace('repository.','[COLOR=orange](REPOSITORY) [/COLOR]').replace('script.','[COLOR=cyan](SCRIPT) [/COLOR]').replace('metadata.','[COLOR=gold](METADATA) [/COLOR]').replace('service.','[COLOR=pink](SERVICE) [/COLOR]').replace('weather.','[COLOR=green](WEATHER) [/COLOR]').replace('module.','[COLOR=gold](MODULE) [/COLOR]')
        iconimage=(os.path.join(file,'icon.png'))
        fanart=(os.path.join(file,'fanart.jpg'))
        extras.addDir('',name,file,'remove_addons',iconimage,fanart,'','')
#-----------------------------------------------------------------------------------------------------------------
#Function to open addon settings
def Addon_Settings():
    ADDON.openSettings(sys.argv[0])
#---------------------------------------------------------------------------------------------------
#Addon Maintenance Section
def Addon_Fixes():
    extras.addDir('folder','Completely remove an add-on (inc. passwords)','plugin','addon_removal_menu', 'Remove_Addon.png','','','')
    extras.addDir('','Hide my add-on passwords','none','hide_passwords', 'Hide_Passwords.png','','','')
    extras.addDir('','Unhide my add-on passwords','none','unhide_passwords', 'Unhide_Passwords.png','','','')
    extras.addDir('','Update My Add-ons (Force Refresh)', 'none', 'update', 'Update_Addons.png','','','')
    extras.addDir('','Wipe All Add-on Settings (addon_data)','url','remove_addon_data','Delete_Addon_Data.png','','','')
#-----------------------------------------------------------------------------------------------------------------
#Backup/Restore root menu
def Backup_Restore():
    extras.addDir('folder','Backup My Content','none','backup_option','Backup.png','','','')
    extras.addDir('folder','Restore My Content','none','restore_option','Restore.png','','','')
#---------------------------------------------------------------------------------------------------
#Main category list
def Categories():
	sign = 0
	maintenance  =  ADDON.getSetting('maintenance')
	mainmenu  =  ADDON.getSetting('mainmenu')
	guisettings  =  ADDON.getSetting('guisettings')
	adultbuilds  =  ADDON.getSetting('adultbuilds')
	if mainmenu == 'true':
		extras.addDir('folder','DTG Builds','none', 'buildmenu', 'Build_Menu.png','','','')
	if adultbuilds == 'true':
		extras.addDir('folder','SportsMania Builds','none', 'adultmenu', 'Adult_Menu.png','','','')
	if guisettings == 'true':
		extras.addDir('folder','Gui Settings XML','none', 'guisettings', 'Adult_Menu.png','','','')
	if maintenance == 'true':
		extras.addDir('folder','Maintenance','none', 'tools', 'Tools.png','','','')
	
#---------------------------------------------------------------------------------------------------
#Function to clear all known cache files
def Clear_Cache():
    if os.path.exists(cachePath)==True:    
        for root, dirs, files in os.walk(cachePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Kodi Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        try:
							if (f.endswith(".log")): continue
							os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if os.path.exists(tempPath)==True:    
        for root, dirs, files in os.walk(tempPath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Kodi Temp Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        try:
                            if (f.endswith(".log")): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
        
        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'Other'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
        
        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'LocalAndRental'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass    

    dialog = xbmcgui.Dialog()
    dialog.ok(MaintTitle, "Cache files are now deleted.")
#---------------------------------------------------------------------------------------------------
#Get params and clean up into string or integer
def Get_Params():
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
#---------------------------------------------------------------------------------------------------
#Function to clear the addon_data
def Remove_Addon_Data():
    choice = xbmcgui.Dialog().yesno('Delete Addon_Data Folder?', 'This will free up space by deleting your addon_data', 'folder. This contains all addon related settings', 'including username and password info.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        extras.Delete_Userdata()
        dialog.ok("Addon_Data Removed", '', 'Your addon_data folder has now been removed.','')
#---------------------------------------------------------------------------------------------------
#Function to clear the packages folder
def Remove_Crash_Logs():
    choice = xbmcgui.Dialog().yesno('Remove All Crash Logs?', 'There is absolutely no harm in doing this, these are', 'log files generated when Kodi crashes and are','only used for debugging purposes.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        extras.Delete_Logs()
        dialog.ok("Crash Logs Removed", '', 'Your crash log files have now been removed.','')
#---------------------------------------------------------------------------------------------------
#Function to clear the packages folder
def Remove_Packages():
    purgePath = xbmc.translatePath('special://home/addons/packages')
    dialog = xbmcgui.Dialog()
    for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
    if dialog.yesno("Delete Packages", "%d packages found."%file_count, "Delete Them?"):  
        for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:            
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
                dialog = xbmcgui.Dialog()
                dialog.ok(MaintTitle, "Packages all deleted! Thanks for using SportsMania Wizard!")
            else:
                dialog = xbmcgui.Dialog()
                dialog.ok(MaintTitle, "No Packages to Purge")
#---------------------------------------------------------------------------------------------------
#Function to clear the packages folder
def Remove_Textures():
    if os.path.exists(thumbnailPath)==True:  
            dialog = xbmcgui.Dialog()
            if dialog.yesno("Delete Thumbnails", "This option deletes all thumbnails", "Are you sure you want to do this?"):
                for root, dirs, files in os.walk(thumbnailPath):
                    file_count = 0
                    file_count += len(files)
                    if file_count > 0:                
                        for f in files:
                            try:
                                os.unlink(os.path.join(root, f))
                            except:
								pass
    else:
        pass
    
    text13 = os.path.join(databasePath,"Textures13.db")
    try:
		os.unlink(text13)
    except OSError:
        pass

	dialog.ok(MaintTitle, 'Thumbnails have been deleted.','Thank you for using SportsMania Wizard')
#---------------------------------------------------------------------------------------------------
#Maintenance section
def Tools():
    extras.addDir('folder','Backup/Restore My Content','none','backup_restore','Backup.png','','','')
    extras.addDir('','Clear Cache','url','clear_cache','Clear_Cache.png','','','')
    extras.addDir('','Clear Thumbnails', 'none', 'remove_textures', 'Delete_Cached_Artwork.png','','','')
    extras.addDir('','Clear Packages Folder','url','remove_packages','Delete_Packages.png','','','')
    extras.addDir('','Wipe My Install (Fresh Start)', 'none', 'wipe_xbmc', 'Fresh_Start.png','','','')
#-----------------------------------------------------------------------------------------------------------------
#Function to clear the addon_data
def Wipe_Kodi():
    mybackuppath = xbmc.translatePath(os.path.join(USB,'Community Builds','My Builds'))
    choice = xbmcgui.Dialog().yesno("ABSOLUTELY CERTAIN?!!!", 'Are you absolutely certain you want to wipe?', '', 'All addons and settings will be completely wiped!', yeslabel='Yes',nolabel='No')
    if choice == 1:
        if skin!= "skin.confluence":
            dialog.ok('[COLOR=white]The DTG Wizard[/COLOR]','Please switch to the default Confluence skin','before performing a wipe.','')
            xbmc.executebuiltin("ActivateWindow(appearancesettings)")
            return
        else:
            choice = xbmcgui.Dialog().yesno("VERY IMPORTANT", 'This will completely wipe your install.', 'Would you like to create a backup before proceeding?', '', yeslabel='No', nolabel='Yes')
            if choice == 0:
                if not os.path.exists(mybackuppath):
                    os.makedirs(mybackuppath)
                vq = extras.Get_Keyboard( heading="Enter a name for this backup" )
                if ( not vq ): return False, 0
                title = urllib.quote_plus(vq)
                backup_zip = xbmc.translatePath(os.path.join(mybackuppath,title+'.zip'))
                exclude_dirs_full =  ['plugin.program.dickowizard']
                exclude_files_full = ["xbmc.log","xbmc.old.log","kodi.log","kodi.old.log",'.DS_Store','.setup_complete','XBMCHelper.conf']
                message_header = "Creating full backup of existing build"
                message1 = "Archiving..."
                message2 = ""
                message3 = "Please Wait"
                communitybuilds.Archive_Tree(HOME, backup_zip, message_header, message1, message2, message3, exclude_dirs_full, exclude_files_full)
            choice = xbmcgui.Dialog().yesno("Remove The SportsMania Wizard?", 'Do you also want to remove the SportsMania wizard', 'add-on and have a complete fresh start or would you', 'prefer to keep this on your system?', yeslabel='Remove',nolabel='Keep')
            if choice == 0:
                cache.Remove_Textures()
                trpath = xbmc.translatePath(os.path.join(ADDONS,AddonID,''))
                trtemp = xbmc.translatePath(os.path.join(HOME,'..','shadowbuilds.zip'))
                communitybuilds.Archive_File(trpath, trtemp)
                deppath = xbmc.translatePath(os.path.join(ADDONS,'script.module.addon.common',''))
                deptemp = xbmc.translatePath(os.path.join(HOME,'..','shadowbuildsdep.zip'))
                communitybuilds.Archive_File(deppath, deptemp)
                extras.Destroy_Path(HOME)
                if not os.path.exists(trpath):
                    os.makedirs(trpath)
                if not os.path.exists(deppath):
                    os.makedirs(deppath)
                time.sleep(1)
                communitybuilds.Read_Zip(trtemp)
                dp.create("[[COLOR=white]SportsMania Wizard[/COLOR][/B]","Checking ",'', 'Please Wait')
                dp.update(0,"", "Extracting Zip Please Wait")
                extract.all(trtemp,trpath,dp)
                communitybuilds.Read_Zip(deptemp)
                extract.all(deptemp,deppath,dp)
                dp.update(0,"", "Extracting Zip Please Wait")
                dp.close()
                time.sleep(1)
                extras.Kill_XBMC()
            elif choice == 1:
                cache.Remove_Textures()
                extras.Destroy_Path(HOME)
                dp.close()
                extras.Kill_XBMC()
            else: return
#-----------------------------------------------------------------------------------------------------------------    
#Maintenance section
def Wipe_Tools():
    extras.addDir('','Clear Cache','url','clear_cache','Clear_Cache.png','','','')
    extras.addDir('','Clear Thumbnails', 'none', 'remove_textures', 'Delete_Cached_Artwork.png','','','')
    extras.addDir('','Clear Packages Folder','url','remove_packages','Delete_Packages.png','','','')
    extras.addDir('','Wipe My Install (Fresh Start)', 'none', 'wipe_xbmc', 'Fresh_Start.png','','','')
#-----------------------------------------------------------------------------------------------------------------
#Builds Section
def BuildMenu():
    link = OPEN_URL('https://archive.org/download/BuildUrls_201511/Build_Urls.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,'wizard',iconimage,fanart,description)
    setView('movies', 'MAIN')
	
def AdultMenu():
    link = OPEN_URL('https://archive.org/download/SMBuilds/SMBuilds.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,'wizard',iconimage,fanart,description)
    setView('movies', 'MAIN')
	
def guisettings():
    link = OPEN_URL('https://archive.org/download/GUIUrls_201512/GUI_Urls.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,'wizard',iconimage,fanart,description)
    setView('movies', 'MAIN')
	
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link  
    
def wizard(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("The DTG Wizard ","Downloading ",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    dialog = xbmcgui.Dialog()
    dialog.ok("DOWNLOAD COMPLETE", 'To ensure all changes are saved you must now close Kodi', 'to force close Kodi. Click ok,', 'DO NOT use the quit/exit options in Kodi.')
    killxbmc()
	            
def killxbmc():
    choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    if choice == 0:
        return
    elif choice == 1:
        pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass        
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "Your system has been detected as Android, you ", "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Pulling the power cable is the simplest method to force close.")
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.","Either force stop or just pull the power plug.")    

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'


def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
		
#-----------------------------------------------------------------------------------------------------------------
#Addon starts here
params=Get_Params()
addon_id=None
audioaddons=None
author=None
buildname=None
data_path=None
description=None
DOB=None
email=None
fanart=None
forum=None
iconimage=None
link=None
local=None
messages=None
mode=None
name=None
posts=None
programaddons=None
provider_name=None
repo_id=None
repo_link=None
skins=None
sources=None
updated=None
unread=None
url=None
version=None
video=None
videoaddons=None
welcometext=None
zip_link=None

try:    addon_id=urllib.unquote_plus(params["addon_id"])
except: pass
try:    adult=urllib.unquote_plus(params["adult"])
except: pass
try:    audioaddons=urllib.unquote_plus(params["audioaddons"])
except: pass
try:    author=urllib.unquote_plus(params["author"])
except: pass
try:    buildname=urllib.unquote_plus(params["buildname"])
except: pass
try:    data_path=urllib.unquote_plus(params["data_path"])
except: pass
try:    description=urllib.unquote_plus(params["description"])
except: pass
try:    DOB=urllib.unquote_plus(params["DOB"])
except: pass
try:    email=urllib.unquote_plus(params["email"])
except: pass
try:    fanart=urllib.unquote_plus(params["fanart"])
except: pass
try:    forum=urllib.unquote_plus(params["forum"])
except: pass
try:    guisettingslink=urllib.unquote_plus(params["guisettingslink"])
except: pass
try:    iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try:    link=urllib.unquote_plus(params["link"])
except: pass
try:    local=urllib.unquote_plus(params["local"])
except: pass
try:    messages=urllib.unquote_plus(params["messages"])
except: pass
try:    mode=str(params["mode"])
except: pass
try:    name=urllib.unquote_plus(params["name"])
except: pass
try:    pictureaddons=urllib.unquote_plus(params["pictureaddons"])
except: pass
try:    posts=urllib.unquote_plus(params["posts"])
except: pass
try:    programaddons=urllib.unquote_plus(params["programaddons"])
except: pass
try:    provider_name=urllib.unquote_plus(params["provider_name"])
except: pass
try:    repo_link=urllib.unquote_plus(params["repo_link"])
except: pass
try:    repo_id=urllib.unquote_plus(params["repo_id"])
except: pass
try:    skins=urllib.unquote_plus(params["skins"])
except: pass
try:    sources=urllib.unquote_plus(params["sources"])
except: pass
try:    updated=urllib.unquote_plus(params["updated"])
except: pass
try:    unread=urllib.unquote_plus(params["unread"])
except: pass
try:    url=urllib.unquote_plus(params["url"])
except: pass
try:    version=urllib.unquote_plus(params["version"])
except: pass
try:    video=urllib.unquote_plus(params["video"])
except: pass
try:    videoaddons=urllib.unquote_plus(params["videoaddons"])
except: pass
try:    zip_link=urllib.unquote_plus(params["zip_link"])
except: pass

print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )

if mode==None or url==None or len(url)<1:
        Categories()
elif mode == 'addon_removal_menu' : Addon_Removal_Menu()
elif mode == 'addonfix'           : addonfix.fixes()
elif mode == 'addonfixes'         : Addon_Fixes()
elif mode == 'addonmenu'          : Addon_Menu()
elif mode == 'addon_settings'     : Addon_Settings()
elif mode == 'backup'             : BACKUP()
elif mode == 'backup_option'      : communitybuilds.Backup_Option()
elif mode == 'backup_restore'     : Backup_Restore()
elif mode == 'adultmenu'          : AdultMenu()
elif mode == 'buildmenu'		  : BuildMenu()
elif mode == 'categories'         : Categories()
elif mode == 'clear_cache'        : Clear_Cache()
elif mode == 'community_backup'   : communitybuilds.Community_Backup()
elif mode == 'community_menu'     : communitybuilds.Community_Menu(url,video)        
elif mode == 'description'        : communitybuilds.Description(name,url,buildname,author,version,description,updated,skins,videoaddons,audioaddons,programaddons,pictureaddons,sources,adult)
elif mode == 'fix_special'        : communitybuilds.Fix_Special(url)
elif mode == 'genres'             : Genres(url)
elif mode == 'grab_addons'        : addons.Grab_Addons(url)
elif mode == 'grab_builds_premium': communitybuilds.Grab_Builds_Premium(url)
elif mode == 'guisettingsfix'     : communitybuilds.GUI_Settings_Fix(url,local)
elif mode == 'guisettings'        : guisettings()   
elif mode == 'hide_passwords'     : extras.Hide_Passwords()
elif mode == 'LocalGUIDialog'     : communitybuilds.Local_GUI_Dialog()
elif mode == 'remove_addon_data'  : Remove_Addon_Data()
elif mode == 'remove_addons'      : extras.Remove_Addons(url)
elif mode == 'remove_build'       : extras.Remove_Build()
elif mode == 'remove_crash_logs'  : Remove_Crash_Logs()
elif mode == 'remove_packages'    : Remove_Packages()
elif mode == 'remove_textures'    : Remove_Textures()
elif mode == 'restore'            : extras.RESTORE()
elif mode == 'restore_backup'     : communitybuilds.Restore_Backup_XML(name,url,description)
elif mode == 'restore_local_CB'   : communitybuilds.Restore_Local_Community()
elif mode == 'restore_local_gui'  : communitybuilds.Restore_Local_GUI()
elif mode == 'restore_option'     : communitybuilds.Restore_Option()
elif mode == 'restore_zip'        : communitybuilds.Restore_Zip_File(url)         
elif mode == 'restore_community'  : communitybuilds.Restore_Community(name,url,video,description,skins,guisettingslink)        
elif mode == 'showinfo'           : communitybuilds.Show_Info(url)
elif mode == 'SortBy'             : extras.Sort_By(BuildURL,type)
elif mode == 'text_guide'         : news.Text_Guide(name,url)
elif mode == 'tools'              : Tools()     
elif mode == 'unhide_passwords'   : extras.Unhide_Passwords()
elif mode == 'update'             : addons.Update_Repo()
elif mode == 'uploadlog'          : extras.Upload_Log()
elif mode == 'user_info'          : Show_User_Info()
elif mode == 'wipetools'          : Wipe_Tools()
elif mode == 'xbmcversion'        : extras.XBMC_Version(url)
elif mode == 'wipe_xbmc'          : Wipe_Kodi()
elif mode ==  'wizard'            : wizard(name,url,description)
xbmcplugin.endOfDirectory(int(sys.argv[1]))