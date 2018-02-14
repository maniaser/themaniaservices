import xbmc,xbmcaddon,xbmcvfs,xbmcgui
import sys
which = sys.argv[1]

ADDON = xbmcaddon.Addon(id='plugin.video.maniaguidesm')

if which == "commands":
    path = xbmc.translatePath('special://home/addons/plugin.video.maniaguidesm/commands.txt')
elif which == "autoplaywith":
    path = xbmc.translatePath('special://home/addons/plugin.video.maniaguidesm/resources/playwith/readme.txt')
f = xbmcvfs.File(path,"rb")
data = f.read()
dialog = xbmcgui.Dialog()
dialog.textviewer('Help', data)
