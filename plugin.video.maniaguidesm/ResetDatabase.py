import os
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs

def deleteDB():
    try:
        xbmc.log("[plugin.video.maniaguidesm] Deleting database...", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'plugin.video.maniaguidesm').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'sportsmania.db')

        delete_file(dbPath)

        passed = not os.path.exists(dbPath)

        if passed:
            xbmc.log("[plugin.video.maniaguidesm] Deleting database...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[plugin.video.maniaguidesm] Deleting database...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[plugin.video.maniaguidesm] Deleting database...EXCEPTION', xbmc.LOGDEBUG)
        return False

def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = int(sys.argv[1])

        if mode in [1,2]:
            if deleteDB():
                d = xbmcgui.Dialog()
                d.ok('TV Guide', 'The database has been successfully deleted.', 'It will be re-created next time you start the guide')
            else:
                d = xbmcgui.Dialog()
                d.ok('TV Guide', 'Failed to delete database.', 'Database may be locked,', 'please restart and try again')
        if mode == 2:
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/addons.ini')
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/categories.ini')
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/custom_stream_urls.ini')
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/mapping.ini')
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/icons.ini')
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/folders.list')
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/tvdb.pickle')
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/tvdb_banners.pickle')
            path = 'special://profile/addon_data/plugin.video.maniaguidesm/'
            dirs, files = xbmcvfs.listdir(path)
            for f in files:
                if (f.endswith('xml') or f.endswith('xmltv')) and f != "settings.xml":
                    xbmcvfs.delete(path+f)
        if mode == 3:
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/tvdb.pickle')
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/tvdb_banners.pickle')
        if mode in [2,4]:
            dirs, files = xbmcvfs.listdir('special://profile/addon_data/plugin.video.maniaguidesm/logos')
            for f in files:
                xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/logos/%s' % f)
        if mode == 5:
            xbmcvfs.delete('special://profile/addon_data/plugin.video.maniaguidesm/settings.xml')					