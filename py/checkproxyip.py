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
@file: checkproxyip.py
@time: 2018/1/25 17:54
"""
import requests
import threading
from py.proxydb import *

class MyThreadLine(threading.Thread):
    def __init__(self,http,pip,port,gethost):
        threading.Thread.__init__(self) #父类初始化
        self.port=port
        self.http=http
        if "s" in http:
            self.httptype="HTTPS"
        else:
            self.httptype = http
        self.proxyip=pip
        self.proxyipport=str(pip)+":"+str(self.port)
        self.gethost=gethost
        self.passip=[]

    def run(self):
        # s = requests.session()#长连接
        # s.proxies = {self.httptype:self.proxyipport}

        proxies={self.httptype:self.proxyipport}
        x=""
        y=""
        try:
            # x = s.get(self.gethost,proxies=proxies)
            url="http://github.com"
            # x = s.get(self.gethost)
            # x = requests.get(self.gethost, timeout=5, proxies=proxies)
            x = requests.get(url, timeout=5, proxies=proxies)
            # print(x)
            if "dns-prefetch" in x.text and x.status_code<400:
                # print("pas")
                # s=
                self.passip=[self.proxyipport,self.httptype]

        except Exception as a:
            y="--"
            print(a)
            # print(a)  # HTTPConnectionPool#ConnectTimeout

# if "ConnectTimeout"in x:
#             self.passip.append([self.proxyip, self.port, self.http])


def exErr():
    #链接超时，请求的url 存放到超时的列表
    #链接超时 代理ip测试后 从passiplist 列表pop出去。
    #重新发起链接
    pass

def check_Main(ipdict,pgethost=""):
    if pgethost=="":pgethost = "http://baidu.com"
    threadlist=[] #线程列表
    for  i  in ipdict:
        proxyip=i.ip
        pport=i.port
        phttp=i.itype

        # print(proxyip,pport,phttp)
        mythd=MyThreadLine( phttp,proxyip,pport,pgethost) #创建线程类对象
        mythd.start() #线程开始干活
        threadlist.append(mythd)#增加线程到线程列表
    for  mythd in threadlist:#遍历每一个线程
        mythd.join() #等待所有线程干完活
    passiplist=[]
    for  mythd in threadlist:
        # print("Threed ip is : ",mythd.passip)
        if mythd.passip:passiplist.append(mythd.passip)
    # print(passiplist)
    print("iplist check ip complete,and pass is  " ,len(passiplist))
    return passiplist



    # tb_.update(student_no=tb_.student_no + 1).where(tb_.student_name == 'baby').execute()

def select_ip_t():
    ips=tb_ip_p.select()
    # print(len(ips))
    return ips




if __name__ == '__main__':
    pass

    ipdistx=select_ip_t()#数据库中取出所有ip
    y=check_Main(ipdistx)#检查数据库中所有IP的存活情况
    if len(y):
        update_check_ip_t(y)
    print("..00")
