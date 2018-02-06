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

    proxyiplist=[]
    def findx(s):
        return s[s.find(">") + 1:s.find("</t")]
    for i in n:
        arri = i.split("<td")
        ip = findx(arri[1])
        port = findx(arri[2])
        art = findx(arri[3])
        ck = findx(arri[4])
        ct = findx(arri[5])

        xdict={"ipport":str(ip)+":"+str(port),"ip":ip, "port":port, "address":art,"other":str(art)+str(ck), "privacy":ck, "itype":ct}
        # print(xdict)
        proxyiplist.append(xdict)
    print("spider ip all is :",len(proxyiplist))
    return proxyiplist

# def iplistfomatetbdict(iplist):
#     ipdict=dict
#     for i in iplist:
#         ipdict['ipport']=str(i[0])+":"+str(i[1])
#         ipdict['ip']=i[0]
#         ipdict['port']=i[1]
#         ipdict['itype']=i[4]
#         ipdict['other']=str(i[2])+str(i[3])
#         ipdict['isok']=""
#         # 'c_time': '',
#         # 'l_time': '',
#     return ipdict


def spider(url):
    print(url)
    h={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate',
'Cookie': 'rotate_ad_from_rd=1; _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWM1YzdjMjc2ZDBlMTE5NWJhODI1ODJlNjVkN2JjNmM3BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMS8xMEd5NkZFM1NjVVFUWkZidDNyVTZnT0VBdFBDUUhGQVZlMzlpLzc0RDg9BjsARg%3D%3D--68f73208e88dbef3d5764495f89eb0f304f650a2; 7702cee25e179949776f0afec2272614=468149a29da1ba3b076caf01cf9bd732; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1516955244; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1516955244',
'DNT': '1',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'If-None-Matc': 'W/"248abe2d89136f0fb2067d0272a18c37"'}
    header = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
              'Upgrade-Insecure-Requests': '1',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.9'}
    # s=requests.get(url,h,timeout=2).text
    s=requests.get(url).text
    # time.sleep(3)
    return s
urlproxy=""
if __name__ == '__main__':

    from py.config import *
    urlproxy= conf_x
    y= conf_y
    #
    url="http://www.xicidaili.com"
    # # # url="https://github.com"
    if urlproxy:url=urlproxy+url
    print(url)
    x = open('temp.html', 'rb').read()
    # x=spider(url)#
    # a=""
    # if len(str(x))>10:
    #     if y: url = y + url
    #     x=spider(url)
    #     pass


    try:
        a=x.decode('utf8')
    except:
        a=x
    # print(a)

    if  len(a)>0:
        ipallist=[]
        iplist=strformat(a)
        from py.proxydb import *
        insert_ip_t(iplist)
        # ix=iplist
        # print(type(ix))
        # if isinstance(ix, list):
        #     for i in ix:
        #         print(i)
        #         if isinstance(i, dict):
        #             x = {}
        #             y = dict(x, **i)
        #             try:
        #                 x = tb_ip_p.create(**i)
        #                 x.save()  # ????????buyao?
        #             except Exception as b:
        #                 print(b)
        #         else:
        #             print("Err _INSERT_IP_T  type Err")
        # elif isinstance(ix, dict):
        #     x = tb_ip_p.create(**ix)
        #     x.save()  # ????????
        # else:
        #     print("Err _INSERT_IP_T type Err")
        # print("o")

    else:
        print("代理无法访问，或服务器无响应")
    #
    # #
    # #
    # # #
    # # iplist=[['116.248.160.45', '80', '云南', '高匿', 'HTTP'], ['49.89.86.176', '24235', '江苏宿迁', '高匿', 'HTTPS'], ['221.8.168.253', '8118', '吉林', '高匿', 'HTTP'], ['114.231.12.100', '28516', '江苏南通', '高匿', 'HTTPS'], ['49.85.1.161', '48636', '江苏泰州', '高匿', 'HTTPS'], ['61.135.217.7', '80', '北京', '高匿', 'HTTP'], ['122.114.31.177', '808', '河南郑州', '高匿', 'HTTP'], ['125.122.119.211', '8118', '浙江杭州', '高匿', 'HTTPS'], ['113.121.47.147', '808', '山东烟台', '高匿', 'HTTPS'], ['123.232.174.175', '8118', '山东济南', '高匿', 'HTTP'], ['139.208.187.142', '8118', '吉林', '高匿', 'HTTP'], ['49.81.32.187', '808', '江苏徐州', '高匿', 'HTTPS'], ['110.200.70.152', '80', '湖北', '高匿', 'HTTPS'], ['58.253.117.55', '80', '广东潮州', '高匿', 'HTTPS'], ['220.166.241.246', '8118', '四川成都', '高匿', 'HTTPS'], ['122.225.17.123', '8080', '浙江嘉兴', '高匿', 'HTTP'], ['115.46.65.236', '8123', '广西南宁', '高匿', 'HTTP'], ['121.31.158.19', '8123', '广西北海', '高匿', 'HTTP'], ['221.215.169.40', '8118', '山东青岛', '高匿', 'HTTPS'], ['27.40.146.71', '61234', '广东湛江', '高匿', 'HTTP'], ['163.125.158.220', '8888', '广东深圳', '透明', 'HTTP'], ['14.211.116.80', '808', '广东佛山', '透明', 'HTTPS'], ['61.155.164.107', '3128', '江苏苏州', '透明', 'HTTP'], ['113.89.55.147', '9999', '广东深圳', '透明', 'HTTPS'], ['120.78.62.57', '3128', '长城宽带', '透明', 'HTTPS'], ['58.252.6.165', '9000', '广东东莞', '透明', 'HTTP'], ['61.155.164.110', '3128', '江苏苏州', '透明', 'HTTP'], ['222.195.92.76', '3128', '安徽合肥', '透明', 'HTTP'], ['122.72.18.34', '80', '甘肃', '透明', 'HTTPS'], ['120.78.78.141', '8888', '长城宽带', '透明', 'HTTPS'], ['115.29.236.46', '3128', '北京', '透明', 'HTTP'], ['58.220.95.107', '8080', '江苏扬州', '透明', 'HTTPS'], ['122.72.18.35', '80', '甘肃', '透明', 'HTTPS'], ['139.224.80.139', '3128', '', '透明', 'HTTPS'], ['60.205.125.201', '8888', '广东深圳', '透明', 'HTTPS'], ['211.159.177.212', '3128', '北京', '透明', 'HTTPS'], ['121.199.42.198', '3129', '北京', '透明', 'HTTPS'], ['61.155.164.111', '3128', '江苏苏州', '透明', 'HTTP'], ['61.166.251.84', '9999', '云南昆明', '透明', 'HTTPS'], ['163.125.99.84', '9797', '广东深圳', '透明', 'HTTPS'], ['14.211.116.80', '808', '广东佛山', '透明', 'HTTPS'], ['49.89.86.176', '24235', '江苏宿迁', '高匿', 'HTTPS'], ['114.231.12.100', '28516', '江苏南通', '高匿', 'HTTPS'], ['113.89.55.147', '9999', '广东深圳', '透明', 'HTTPS'], ['49.85.1.161', '48636', '江苏泰州', '高匿', 'HTTPS'], ['120.78.62.57', '3128', '长城宽带', '透明', 'HTTPS'], ['122.72.18.34', '80', '甘肃', '透明', 'HTTPS'], ['120.78.78.141', '8888', '长城宽带', '透明', 'HTTPS'], ['58.220.95.107', '8080', '江苏扬州', '透明', 'HTTPS'], ['122.72.18.35', '80', '甘肃', '透明', 'HTTPS'], ['139.224.80.139', '3128', '', '透明', 'HTTPS'], ['60.205.125.201', '8888', '广东深圳', '透明', 'HTTPS'], ['211.159.177.212', '3128', '北京', '透明', 'HTTPS'], ['121.199.42.198', '3129', '北京', '透明', 'HTTPS'], ['125.122.119.211', '8118', '浙江杭州', '高匿', 'HTTPS'], ['61.166.251.84', '9999', '云南昆明', '透明', 'HTTPS'], ['163.125.99.84', '9797', '广东深圳', '透明', 'HTTPS'], ['175.146.97.91', '8080', '辽宁', '透明', 'HTTPS'], ['113.121.47.147', '808', '山东烟台', '高匿', 'HTTPS'], ['124.152.84.65', '53281', '甘肃', '透明', 'HTTPS'], ['163.125.158.220', '8888', '广东深圳', '透明', 'HTTP'], ['116.248.160.45', '80', '云南', '高匿', 'HTTP'], ['61.155.164.107', '3128', '江苏苏州', '透明', 'HTTP'], ['221.8.168.253', '8118', '吉林', '高匿', 'HTTP'], ['58.252.6.165', '9000', '广东东莞', '透明', 'HTTP'], ['61.155.164.110', '3128', '江苏苏州', '透明', 'HTTP'], ['222.195.92.76', '3128', '安徽合肥', '透明', 'HTTP'], ['115.29.236.46', '3128', '北京', '透明', 'HTTP'], ['61.135.217.7', '80', '北京', '高匿', 'HTTP'], ['122.114.31.177', '808', '河南郑州', '高匿', 'HTTP'], ['61.155.164.111', '3128', '江苏苏州', '透明', 'HTTP'], ['139.129.166.68', '3128', '北京', '透明', 'HTTP'], ['113.200.159.155', '9999', '陕西西安', '透明', 'HTTP'], ['123.232.174.175', '8118', '山东济南', '高匿', 'HTTP'], ['139.208.187.142', '8118', '吉林', '高匿', 'HTTP'], ['203.174.112.13', '3128', '北京', '透明', 'HTTP'], ['122.225.17.123', '8080', '浙江嘉兴', '高匿', 'HTTP'], ['115.46.65.236', '8123', '广西南宁', '高匿', 'HTTP'], ['121.31.158.19', '8123', '广西北海', '高匿', 'HTTP'], ['27.40.146.71', '61234', '广东湛江', '高匿', 'HTTP'], ['121.31.103.33', '6666', '广西防城港', '高匿', 'socks4/5'], ['171.38.64.67', '6675', '广西玉林', '高匿', 'socks4/5'], ['112.114.76.176', '6668', '云南临沧', '高匿', 'socks4/5'], ['222.172.239.69', '6666', '云南昆明市呈贡县', '高匿', 'socks4/5'], ['112.114.78.54', '6673', '云南临沧', '高匿', 'socks4/5'], ['113.121.245.32', '6667', '山东德州', '高匿', 'socks4/5'], ['110.73.30.246', '6666', '广西防城港', '高匿', 'socks4/5'], ['114.239.253.38', '6666', '江苏宿迁市泗阳县', '高匿', 'socks4/5'], ['116.28.106.165', '6666', '广东中山', '高匿', 'socks4/5'], ['220.179.214.77', '6666', '安徽铜陵', '高匿', 'socks4/5'], ['110.73.32.7', '6666', '广西防城港', '高匿', 'socks4/5'], ['114.139.48.8', '6668', '贵州遵义', '高匿', 'socks4/5'], ['111.124.231.101', '6668', '贵州铜仁地区铜仁', '高匿', 'socks4/5'], ['118.80.181.186', '6675', '山西阳泉', '高匿', 'socks4/5'], ['113.122.42.161', '6675', '山东菏泽', '高匿', 'socks4/5'], ['60.211.17.10', '6675', '山东德州', '高匿', 'socks4/5'], ['110.72.20.245', '6673', '广西贵港', '高匿', 'socks4/5'], ['110.73.33.207', '6673', '广西防城港', '高匿', 'socks4/5'], ['122.89.138.20', '6675', '江苏徐州', '高匿', 'socks4/5'], ['61.138.104.30', '1080', '内蒙古包头', '高匿', 'socks4/5']]
    # # tab_key = {
    # #     'ipport': '',
    # #     'ip': '',
    # #     'port': '',
    # #     'itype': '',
    # #     'c_time': '',
    # #     'l_time': '',
    # #     'isok': '',
    # #     'other': '',
    # #     'url': '',
    # #     ' port': '',
    # #     'user': '',
    # #     'pasd': '',
    # #     'src': '',
    # #     'key': '',
    # #     'json': '',
    # #     'otherconf': ''
    # # }
    # #
