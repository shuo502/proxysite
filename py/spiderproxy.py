#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: mum
@license: Apache Licence 
@contact: shuo502@163.com
@author: ‘yo‘
@site: http://github.com/shuo502
@software: PyCharm
@file: spiderproxy.py
@time: 2018/1/25 15:22
"""

import requests
import re

def strformat(intext):
    r = re.compile(r'<tr.*?y"><(.*?)</tr>', re.S)
    n = re.findall(r, intext)
    proxyiplist = []
    def findx(s):
        return s[s.find(">") + 1:s.find("</t")]
    for i in n:
        arri = i.split("<td")
        ip = findx(arri[1])
        prot = findx(arri[2])
        art = findx(arri[3])
        ck = findx(arri[4])
        ct = findx(arri[5])
        proxyiplist.append([ip, prot, art, ck, ct])
    return proxyiplist
    print(x)

def spider(url):
    return requests.get(url).text
urlproxy=""
if __name__ == '__main__':
    import config
    urlproxy=config.x
    url="http://www.xicidaili.com"
    # url="https://github.com"
    if urlproxy:url=urlproxy+url
    x=spider(url)
    # x=open('temp.html','rb').read()
    # a=x.decode('utf8')
    if x:print(strformat(x))



