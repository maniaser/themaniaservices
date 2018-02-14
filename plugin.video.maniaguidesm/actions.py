import xbmcvfs,xbmcgui

xbmcvfs.copy('special://home/addons/plugin.video.maniaguidesm/resources/actions.json','special://profile/addon_data/plugin.video.maniaguidesm/actions.json')
xbmcgui.Dialog().notification("Mania TV Guide","Action Bar Reset")
