import datetime,time
import os
import xbmc
import xbmcgui, xbmcaddon, xbmcvfs
import source as src
import re

from strings import *

ADDON = xbmcaddon.Addon(id='plugin.video.maniaguidesm')


class Autoplaywith(object):
    def __init__(self, database, addonPath):
        """
        @param database: source.Database
        """
        self.database = database
        self.addonPath = addonPath
        self.icon = os.path.join(self.addonPath, 'icon.png')

    def createAlarmClockName(self, programTitle, startTime):
        return 'tvguide-%s-%s' % (programTitle, startTime)

    def scheduleAutoplaywiths(self):
        for program in self.database.getFullAutoplaywiths():
            self._scheduleAutoplaywith(program.channel.id, program.title, program.startDate, program.endDate)

    def _scheduleAutoplaywith(self, channelId, programTitle, startTime, endTime):
        t = startTime - datetime.datetime.now()
        timeToAutoplaywith = ((t.days * 86400) + t.seconds) / 60
        if timeToAutoplaywith < 0:
            return
        #timeToAutoplaywith = 1
        name = self.createAlarmClockName(programTitle, startTime)
        timestamp = time.mktime(startTime.timetuple())
        xbmc.executebuiltin('AlarmClock(%s-start,RunScript(special://home/addons/plugin.video.maniaguidesm/playwith.py,%s,%s),%d,True)' %
        (name.encode('utf-8', 'replace'), channelId.encode('utf-8'), timestamp, timeToAutoplaywith - int(ADDON.getSetting('autoplaywiths.before'))))

        t = endTime - datetime.datetime.now()
        timeToAutoplaywith = ((t.days * 86400) + t.seconds) / 60
        #timeToAutoplaywith = 0
        if ADDON.getSetting('autoplaywiths.stop') == 'true':
            xbmc.executebuiltin('AlarmClock(%s-stop,RunScript(special://home/addons/plugin.video.maniaguidesm/stopwith.py,%s,%s),%d,True)' %
            (name.encode('utf-8', 'replace'), channelId.encode('utf-8'), timestamp, timeToAutoplaywith + int(ADDON.getSetting('autoplaywiths.after'))))


    def _unscheduleAutoplaywith(self, programTitle, startTime):
        name = self.createAlarmClockName(programTitle, startTime)
        xbmc.executebuiltin('CancelAlarm(%s-start,True)' % name.encode('utf-8', 'replace'))
        xbmc.executebuiltin('CancelAlarm(%s-stop,True)' % name.encode('utf-8', 'replace'))

    def addAutoplaywith(self, program,type):
        self.database.addAutoplaywith(program,type)
        if type == 0:
            self._scheduleAutoplaywith(program.channel.id, program.title, program.startDate, program.endDate)
        else:
            self.scheduleAutoplaywiths()

    def removeAutoplaywith(self, program):
        self.database.removeAutoplaywith(program)
        self._unscheduleAutoplaywith(program.title, program.startDate)

if __name__ == '__main__':
    database = src.Database()

    def onAutoplaywithsCleared():
        xbmcgui.Dialog().ok(strings(CLEAR_NOTIFICATIONS), strings(DONE)) #TODO

    def onInitialized(success):
        if success:
            database.clearAllAutoplaywiths()
            database.close(onAutoplaywithsCleared)
            ADDON.setSetting('playing.channel','')
            ADDON.setSetting('playing.start','')
        else:
            database.close()

    database.initialize(onInitialized)
