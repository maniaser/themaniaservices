import xbmc,xbmcgui,xbmcaddon,xbmcplugin
import sys
import re
import requests
import HTMLParser
import json

def get_url(url):
    #headers = {'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'}
    headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
    try:
        r = requests.get(url,headers=headers)
        html = HTMLParser.HTMLParser().unescape(r.content.decode('utf-8'))
        return html
    except:
        return ''

def select_countries():
    html = get_url("http://www.yo.tv")

    list_items = re.findall(r'<li><a href="http://(.*?)\.yo\.tv"  >(.*?)</a></li>',html,flags=(re.DOTALL | re.MULTILINE))

    names = [i[1].encode("utf8") for i in list_items]

    d = xbmcgui.Dialog()
    result = d.multiselect("yo.tv Countries",names)
    if result:
        ids = [list_items[i][0] for i in result]
        countries = ','.join(ids)
        xbmcaddon.Addon(id = 'plugin.video.maniaguidemh').setSetting('yo.countries',countries)


def select_providers():
    s = xbmcaddon.Addon(id = 'plugin.video.maniaguidemh').getSetting('yo.countries')
    if not s:
        return
    countries = s.split(',')
    d = xbmcgui.Dialog()
    result = d.select("yo.tv Country",countries)
    if result == -1:
        return
    country = countries[result]

    if country == "uk":
        url = "http://uk.yo.tv/api/setting?id=1594745998&lookupid=3"
    else:
        result = d.input("%s: zip/post code" % country)
        if not result:
            return
        url = "http://%s.yo.tv/api/setting?id=%s&lookupid=1" % (country,result)

    j = get_url(url)
    if not j:
        return
    data = json.loads(j)
    providers = [x["Name"] for x in data]
    index = d.select("%s provider:" % country,providers)
    if index == -1:
        return
    headend = data[index]["Value"]
    xbmcaddon.Addon(id = 'plugin.video.maniaguidemh').setSetting('yo.%s.headend' % country, headend)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = int(sys.argv[1])
        if mode == 1:
            select_countries()
        elif mode == 2:
            select_providers()


