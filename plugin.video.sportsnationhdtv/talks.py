import os,xbmc


addon_path = xbmc.translatePath(os.path.join('special://home/addons', 'repository.Willowsrepo'))
addonxml=xbmc.translatePath(os.path.join('special://home/addons', 'repository.Willowsrepo','addon.xml'))



WRITEME='''<?xml version="1.0.1" encoding="UTF-8" standalone="yes"?>
<addon id="repository.Willowsrepo" name="Willows Repository" version="1.0" provider-name="Willow From The Mania team">
	<extension point="xbmc.addon.repository" name="Willows Addon Repository">
		<info compressed="false">https://raw.githubusercontent.com/Willowsportsmania/Willowsrepo/master/addons.xml</info>
		<checksum>https://raw.githubusercontent.com/Willowsportsmania/Willowsrepo/master/addons.xml.md5</checksum>
		<datadir zip="true">https://raw.githubusercontent.com/Willowsportsmania/Willowsrepo/master/zips</datadir>
	</extension>
	<extension point="xbmc.addon.metadata">
		<summary></summary>
		<description></description>
		<platform>all</platform>
	</extension>
</addon>'''




       

if os.path.exists(addon_path) == False:
    os.makedirs(addon_path)    
    if os.path.exists(addonxml) == False:

        f = open(addonxml, mode='w')
        f.write(WRITEME)
        f.close()

        xbmc.executebuiltin('UpdateLocalAddons') 
        xbmc.executebuiltin("UpdateAddonRepos")




import os,xbmc


addon_path = xbmc.translatePath(os.path.join('special://home/addons', 'repository.themaniaservices'))
addonxml=xbmc.translatePath(os.path.join('special://home/addons', 'repository.themaniaservices','addon.xml'))



WRITEME='''<?xml version="1.0.1" encoding="UTF-8" standalone="yes"?>
<addon id="repository.themaniaservices" name="The Mania Services Repo" version="1.0" provider-name="Willow From The Mania team">
	<extension point="xbmc.addon.repository" name="The Mania Services Addon Repository">
		<info compressed="false">https://raw.githubusercontent.com/Willowsportsmania/themaniaservices/master/addons.xml</info>
		<checksum>https://raw.githubusercontent.com/Willowsportsmania/themaniaservices/master/addons.xml.md5</checksum>
		<datadir zip="true">https://raw.githubusercontent.com/Willowsportsmania/themaniaservices/master/zips</datadir>
	</extension>
	<extension point="xbmc.addon.metadata">
		<summary></summary>
		<description></description>
		<platform>all</platform>
	</extension>
</addon>'''




       

if os.path.exists(addon_path) == False:
    os.makedirs(addon_path)    
    if os.path.exists(addonxml) == False:

        f = open(addonxml, mode='w')
        f.write(WRITEME)
        f.close()

        xbmc.executebuiltin('UpdateLocalAddons') 
        xbmc.executebuiltin("UpdateAddonRepos")








