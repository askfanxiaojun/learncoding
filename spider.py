#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'/Users/fan/Documents/我的坚果云/收集各种优秀网站/mailing/%s.jpg' % x)
        x+=1

html = getHtml("http://calltoidea.com/mailing/")

print getImg(html)