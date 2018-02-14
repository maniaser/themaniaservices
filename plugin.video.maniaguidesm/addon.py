#

import sys
import xbmc,xbmcaddon,xbmcvfs
import os
import stat

ADDON = xbmcaddon.Addon(id='plugin.video.maniaguidesm')

ffmpeg = ADDON.getSetting('autoplaywiths.ffmpeg')
if ffmpeg:
    st = os.stat(ffmpeg)
    try:
        os.chmod(ffmpeg, st.st_mode | stat.S_IEXEC)
    except:
        pass

if len(sys.argv) > 1:
    category = sys.argv[1]
    if category:
        ADDON.setSetting('category',category)

if len(sys.argv) > 2:
    source = ADDON.getSetting('source.source')
    new_source = sys.argv[2]
    if new_source != source:
        ADDON.setSetting('source.source',new_source)

assets = [
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/sunburst.png','https://raw.githubusercontent.com/primaeval/assets/master/backgrounds/sunburst.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/charcoal.png','https://raw.githubusercontent.com/primaeval/assets/master/backgrounds/charcoal.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/actions.json','special://home/addons/plugin.video.maniaguidesm/resources/actions.json')
]
for (dst,src) in assets:
    if not xbmcvfs.exists(dst):
        xbmcvfs.copy(src,dst)

try:
    import gui
    w = gui.TVGuide()
    w.doModal()
    del w

except:
    import sys
    import traceback as tb
    (etype, value, traceback) = sys.exc_info()
    tb.print_exception(etype, value, traceback)