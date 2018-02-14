import datetime
import os
import xbmc
import xbmcgui, xbmcaddon
import source as src

from strings import *

ADDON = xbmcaddon.Addon(id='plugin.video.maniaguide')


class Autoplay(object):
    def __init__(self, database, addonPath):
        """
        @param database: source.Database
        """
        self.database = database
        self.addonPath = addonPath
        self.icon = os.path.join(self.addonPath, 'icon.png')

    def createAlarmClockName(self, programTitle, startTime):
        return 'tvguide-%s-%s' % (programTitle, startTime)
        
    def scheduleAutoplays(self):
        for program in self.database.getFullAutoplays():
            self._scheduleAutoplay(program.channel.id, program.title, program.startDate, program.endDate)


    def _scheduleAutoplay(self, channelId, programTitle, startTime, endTime):
        t = startTime - datetime.datetime.now()
        timeToAutoplay = ((t.days * 86400) + t.seconds) / 60
        if timeToAutoplay < 0:
            return
        #timeToAutoplay = 1
        name = self.createAlarmClockName(programTitle, startTime)
        xbmc.executebuiltin('AlarmClock(%s-start,RunScript(special://home/addons/plugin.video.maniaguide/play.py,%s,%s),%d,True)' %
        (name.encode('utf-8', 'replace'), channelId.encode('utf-8'), startTime, timeToAutoplay - int(ADDON.getSetting('autoplays.before'))))

        t = endTime - datetime.datetime.now()
        timeToAutoplay = ((t.days * 86400) + t.seconds) / 60
        #timeToAutoplay = 0
        if ADDON.getSetting('autoplays.stop') == 'true':
            xbmc.executebuiltin('AlarmClock(%s-stop,RunScript(special://home/addons/plugin.video.maniaguide/stop.py,%s,%s),%d,True)' %
            (name.encode('utf-8', 'replace'), channelId.encode('utf-8'), startTime, timeToAutoplay + int(ADDON.getSetting('autoplays.after'))))


    def _unscheduleAutoplay(self, programTitle, startTime):
        name = self.createAlarmClockName(programTitle, startTime)
        xbmc.executebuiltin('CancelAlarm(%s-start,True)' % name.encode('utf-8', 'replace'))
        xbmc.executebuiltin('CancelAlarm(%s-stop,True)' % name.encode('utf-8', 'replace'))

    def addAutoplay(self, program,type):
        self.database.addAutoplay(program,type)
        self._scheduleAutoplay(program.channel.id, program.title, program.startDate, program.endDate)

    def removeAutoplay(self, program):
        self.database.removeAutoplay(program)
        self._unscheduleAutoplay(program.title, program.startDate)


if __name__ == '__main__':
    database = src.Database()

    def onAutoplaysCleared():
        xbmcgui.Dialog().ok(strings(CLEAR_NOTIFICATIONS), strings(DONE)) #TODO

    def onInitialized(success):
        if success:
            database.clearAllAutoplays()
            database.close(onAutoplaysCleared)
            ADDON.setSetting('playing.channel','')
            ADDON.setSetting('playing.start','')
        else:
            database.close()

    database.initialize(onInitialized)
