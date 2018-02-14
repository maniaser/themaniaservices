
#

import xbmc
import xbmcgui
import xbmcaddon
import shutil


def resetAddon():
    path = xbmc.translatePath('special://profile/addon_data/plugin.program.dickowizard')
    shutil.rmtree(path)
    
    d = xbmcgui.Dialog()
    d.ok('TR Community Builds', 'Community builds addon_data now removed.', 'Your locally stored builds will be unaffected but your', 'settings have now reset back to the defaults.')


if __name__ == '__main__':
    resetAddon()
