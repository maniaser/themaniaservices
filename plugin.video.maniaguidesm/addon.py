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
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/default.png','http://maniaguide.co.uk/backgrounds/default.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/DarkMiddle50.png','http://maniaguide.co.uk/backgrounds/DarkMiddle50.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/DarkMiddle100.png','http://maniaguide.co.uk/backgrounds/DarkMiddle100.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/LightMiddle50.png','http://maniaguide.co.uk/backgrounds/LightMiddle50.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/LightMiddle100.png','http://maniaguide.co.uk/backgrounds/LightMiddle100.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/PlainColours.png','http://maniaguide.co.uk/backgrounds/PlainColours.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/PlainColoursHelp.png','http://maniaguide.co.uk/backgrounds/PlainColoursHelp.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/radial_dark_centre.png','http://maniaguide.co.uk/backgrounds/radial_dark_centre.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/radial_dark_edges.png','http://maniaguide.co.uk/backgrounds/radial_dark_edges.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/textured_1.png','http://maniaguide.co.uk/backgrounds/textured_1.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/textured_2.png','http://maniaguide.co.uk/backgrounds/textured_2.png'),
('special://profile/addon_data/plugin.video.maniaguidesm/backgrounds/Use_For_Black.png','http://maniaguide.co.uk/backgrounds/Use_For_Black.png'),
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