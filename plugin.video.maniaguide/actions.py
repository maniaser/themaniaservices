import xbmcvfs,xbmcgui

xbmcvfs.copy('special://home/addons/plugin.video.maniaguide/resources/actions.json','special://profile/addon_data/plugin.video.maniaguide/actions.json')
xbmcgui.Dialog().notification("Mania TV Guide","Action Bar Reset")
