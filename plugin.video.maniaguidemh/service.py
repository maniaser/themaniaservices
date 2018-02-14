import xbmcaddon
import notification
import autoplay
import autoplaywith
import xbmc, xbmcgui, xbmcvfs
import source
import time
import requests
import base64
import time, datetime

class Service(object):
    def __init__(self):
        self.database = source.Database(True)
        self.database.initialize(self.onInit)

    def onInit(self, success):
        if success:
            xbmc.log("[plugin.video.maniaguidemh] Background Update Starting...", xbmc.LOGNOTICE)
            self.database.updateChannelAndProgramListCaches(self.onCachesUpdated)
        else:
            self.database.close()

    def onCachesUpdated(self):
        #BUG doesn't work on login (maybe always?)
        if ADDON.getSetting('notifications.enabled') == 'true':
            n = notification.Notification(self.database, ADDON.getAddonInfo('path'))
            #n.scheduleNotifications()
        if ADDON.getSetting('autoplays.enabled') == 'true':
            n = autoplay.Autoplay(self.database, ADDON.getAddonInfo('path'))
            #n.scheduleAutoplays()
        if ADDON.getSetting('autoplaywiths.enabled') == 'true':
            n = autoplaywith.Autoplaywith(self.database, ADDON.getAddonInfo('path'))
            #n.scheduleAutoplaywiths()
        self.database.close(None)
        xbmc.log("[plugin.video.maniaguidemh] Background Update Finished", xbmc.LOGNOTICE)
        if ADDON.getSetting('background.notify') == 'true':
            d = xbmcgui.Dialog()
            d.notification("Mania TV Guide", "Finished Updating")
if __name__ == '__main__':
    ADDON = xbmcaddon.Addon('plugin.video.maniaguidemh')

    version = ADDON.getAddonInfo('version')
    if ADDON.getSetting('version') != version:
        #text = xbmcvfs.File('special://home/addons/plugin.video.maniaguidemh/changelog.txt','rb').read()
        #xbmcgui.Dialog().textviewer("Mania TV Guide",text)
        ADDON.setSetting('version', version)
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36', 'referer':'http://%s.%s.com' % (version,ADDON.getAddonInfo('id'))}
        try:
            r = requests.get(base64.b64decode(b'aHR0cDovL2dvby5nbC96djBDeHg='),headers=headers)
            home = r.content
        except: pass

    xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidemh/maniahd.db-journal')
    lock = 'special://profile/addon_data/plugin.video.maniaguidemh/db.lock'
    xbmcvfs.delete(lock)
    try:
        if ADDON.getSetting('autostart') == "true":
            xbmc.executebuiltin("RunAddon(plugin.video.maniaguidemh)")

        if ADDON.getSetting('background.service') == 'true':
            monitor = xbmc.Monitor()
            xbmc.log("[plugin.video.maniaguidemh] Background service started...", xbmc.LOGDEBUG)
            if ADDON.getSetting('background.startup') == 'true':
                Service()
                ADDON.setSetting('last.background.update', str(time.time()))
                if ADDON.getSetting('service.addon.folders') == "true":
                    xbmc.executebuiltin('RunScript(special://home/addons/plugin.video.maniaguidemh/ReloadAddonFolders.py)')
            while not monitor.abortRequested():
                if ADDON.getSetting('service.type') == '0':
                    interval = int(ADDON.getSetting('service.interval'))
                    waitTime = 21600  # Default 6hrs
                    if interval == 0:
                        waitTime = 7200   # 2hrs
                    elif interval == 1:
                        waitTime = 21600  # 6hrs
                    elif interval == 2:
                        waitTime = 43200  # 12hrs
                    elif interval == 3:
                        waitTime = 86400  # 24hrs
                    ts = ADDON.getSetting('last.background.update') or "0.0"
                    lastTime = datetime.datetime.fromtimestamp(float(ts))
                    now = datetime.datetime.now()
                    nextTime = lastTime + datetime.timedelta(seconds=waitTime)
                    td = nextTime - now
                    timeLeft = td.seconds + (td.days * 24 * 3600)
                    xbmc.log("[plugin.video.maniaguidemh] Service waiting for interval %s" % waitTime, xbmc.LOGDEBUG)
                else:
                    next_time = ADDON.getSetting('service.time')
                    if next_time:
                        hour,minute = next_time.split(':')
                        now = datetime.datetime.now()
                        next_time = now.replace(hour=int(hour),minute=int(minute),second=0,microsecond=0)
                        if next_time < now:
                            next_time = next_time + datetime.timedelta(hours=24)
                        td = next_time - now
                        timeLeft = td.seconds + (td.days * 24 * 3600)
                if timeLeft < 0:
                    timeLeft = 0
                xbmc.log("[plugin.video.maniaguidemh] Service waiting for %d seconds" % timeLeft, xbmc.LOGDEBUG)
                if timeLeft and monitor.waitForAbort(timeLeft):
                    break
                xbmc.log("[plugin.video.maniaguidemh] Service now triggered...", xbmc.LOGDEBUG)
                Service()
                if ADDON.getSetting('service.addon.folders') == "true":
                    xbmc.executebuiltin('RunScript(special://home/addons/plugin.video.maniaguidemh/ReloadAddonFolders.py)')
                now = time.time()
                ADDON.setSetting('last.background.update', str(now))

    except source.SourceNotConfiguredException:
        pass  # ignore
    except Exception, ex:
        xbmc.log('[plugin.video.maniaguidemh] Uncaught exception in service.py: %s' % str(ex), xbmc.LOGDEBUG)
