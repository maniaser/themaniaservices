import xbmcvfs,xbmcgui

xbmcvfs.copy('special://home/addons/plugin.video.maniaguidemh/resources/actions.json','special://profile/addon_data/plugin.video.maniaguidemh/actions.json')
xbmcgui.Dialog().notification("Mania TV Guide","Action Bar Reset")
