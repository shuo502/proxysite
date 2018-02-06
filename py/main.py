#!/usr/bin/env python
# encoding: utf-8
from py.spiderproxy import *
from py.config import *

from py.checkproxyip import *

"""
@version: ??
@author: mum
@license: Apache Licence 
@contact: shuo502@163.com
@author: ‘yo‘
@site: http://github.com/shuo502
@software: PyCharm
@file: main.py
@time: 2018/1/29 11:44
"""


def func():
    pass

def Main():
    #----------config-web-proxy----spider--req:html-
    urlproxy = conf_x
    y = conf_y
    url = "http://www.xicidaili.com"
    if urlproxy: url = urlproxy + url
    # x = open('temp.html', 'rb').read()
    # #
    x=spider(url)

    if len(str(x))<10 and y:
        url = y + url
        x=spider(url)
    try:
        a = x.decode('utf8')
    except:
        a = x
        print(a)
    # ------import--html--------insert-----req--none----------
    if len(a) > 0:
        ipallist = []
        iplist = strformat(a)
        insert_ip_t(iplist)
        print("insert Complete!")

    else:
        print("Err")
    # ------import-----------checkip--------------
    ipdistx = select_ip_t()
    if ipdistx:y = check_Main(ipdistx)
    # print(y)
    # ----------------update survive ip-----
    if len(y):
        update_check_ip_t(y)
    print("..update Complete")

    pass


if __name__ == '__main__':
    Main()
    # import requests
    # temp_text=requests.get("http://github.com")
    # print(temp_text.status_code)
    # print(temp_text.content)
    # print(temp_text.headers)
    # print(temp_text.history)