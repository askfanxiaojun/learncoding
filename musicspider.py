import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getMusic(html):
    reg = r'/song?id=27984071'
    songre = re.compile(reg)
    songlist = re.findall(songre,html)
    return songlist



html = getHtml("http://music.163.com/#/playlist?id=11872226")

print getMusic(html)
