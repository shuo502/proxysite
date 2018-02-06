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
@file: proxydb.py
@time: 2018/1/25 20:03
"""

from peewee import *

db=SqliteDatabase("proxydb.db")

class tb_ip_p(Model):
    ipport=CharField(verbose_name="ip端口",null=False,max_length=22,unique=True)
    ip=CharField(verbose_name="ip",null=False,max_length=15,unique=False)
    port=CharField(verbose_name="端口",null=False,max_length=6,unique=False)
    itype=CharField(verbose_name="类型",null=True,max_length=22,unique=False)
    c_time=DateField(verbose_name="创建时间",null=True)
    l_time=DateField(verbose_name="最后时间",null=True)
    isok = DateField(verbose_name="可用", null=True)
    other=CharField(verbose_name="",null=True,unique=False)
    pass
    class Meta:
        database=db


class tb_http_p(Model):

    itype=CharField(verbose_name="",null=False,max_length=32,unique=False)
    url=CharField(verbose_name="URL",null=False,max_length=255,unique=True)
    port=CharField(verbose_name="端口",null=False,max_length=6,unique=False)
    user=CharField(verbose_name="",null=False,max_length=32,unique=False)
    pasd=CharField(verbose_name="",null=False,max_length=32,unique=False)
    c_time=DateField(verbose_name="创建时间",null=True)
    l_time=DateField(verbose_name="最后时间",null=True)
    isok = DateField(verbose_name="可用", null=True)
    other = CharField(verbose_name="", null=True, unique=False)
    class Meta:
        database=db

class tb_sso_p(Model):
    src=CharField(null=True,verbose_name="",unique=False)
    itype=CharField(null=True,verbose_name="",unique=True)
    key=CharField(null=True,verbose_name="",unique=True)
    json=CharField(null=True,verbose_name="",unique=True)
    otherconf=CharField(null=True,verbose_name="",unique=True)
    c_time=DateField(verbose_name="创建时间",null=True)
    l_time=DateField(verbose_name="最后时间",null=True)
    isok=DateField(verbose_name="可用",null=True)
    other = CharField(verbose_name="", null=True, unique=False)
    class Meta:
        database=db





class connect(Model):
    class   Meta:
        try:
            database=db
            db.connect()
        except:
            pass

class closes(Model):
    class Meta:
        try:
            database=db
            database.close()
        except:
            pass

try:tb_http_p.create_table()
except:pass
try:tb_ip_p.create_table()
except:pass
try:tb_sso_p.create_table()
except:pass

# def sq_insert():
#     pass
# def sq_delete():
#     pass
# def sq_select():
#     pass
# def sq_update():
#     pass
#

def update_check_ip_t(iplist):
    bdict = tb_ip_p.select(tb_ip_p.ipport)

    list_ipport=[]
    for temp_f_i in iplist:
        if temp_f_i:list_ipport.append(temp_f_i[0])
    print("iplist is :",list_ipport)

    temp_i=0
    for i in bdict:
        print(i.ipport)
        # if i in iplist:
        if str(i.ipport) in list_ipport:
            try:
                t=tb_ip_p.update(isok="1").where(tb_ip_p.ipport ==  i.ipport).execute()
                temp_i=temp_i+1
            except:
                print("update err")
                pass
            # print("updata is ok ",i.ipport)
        else:
            t=tb_ip_p.update(isok="0").where(tb_ip_p.ipport ==  i.ipport).execute()
        # t.save()
    print("update_check ok insert is ",temp_i)



def insert_ip_t(ix):
    print(type(ix))
    temp_i=0
    if isinstance(ix, list):
        for i in ix:

            if isinstance(i, dict):
                tdict={}
                y=dict(tdict,**i)
                try:

                    x = tb_ip_p.create(**y)
                    x.save()  # ????????buyao?
                    # print("insert ok -",i)
                    temp_i=temp_i+1
                except Exception as b:
                    print(b)
            else:
                print(i)

                print("Err _INSERT_IP_T 1 type Err")
    elif isinstance(ix,dict):
        try:
            x = tb_ip_p.create(**ix)
            x.save()  # ????????buyao?
            temp_i=temp_i+1
        except Exception as b:
            print(b)
    else:
        print(ix)
        print("Err _INSERT_IP_T 2 type Err")

    print("insert ip complete is :",temp_i)


tab_key={
    'ipport':'',
    'ip':'',
    'port':'',
    'itype':'',
    'c_time':'',
    'l_time':'',
    'isok':'',
    'other':'',
    'url':'',
   ' port':'',
    'user':'',
    'pasd':'',
    'src':'',
    'key':'',
    'json':'',
    'otherconf':''
}

def find_ispass_ip_t(isok="1"):
    #------return --list--[ipport type]
    temp_d_ip=tb_ip_p.select().where(tb_ip_p.isok==isok)
    return_ip_list=[]
    for i  in temp_d_ip:
        return_ip_list.append([i.ipport,i.itype])
    return return_ip_list

if __name__ == '__main__':
    #liplist[, , , , ]
    # update_check_ip_t(iplist)
    # insert_ip_t()

    pass
    # d=[{'address': '云南', 'other': '云南高匿', 'privacy': '高匿', 'itype': 'HTTP', 'ip': '116.248.160.415', 'port': '810', 'ipport': '116.248.1610.45:81'},]
    # insert_ip_t(d)
    a=tb_ip_p.select()
    print(len(a))
    for i in a:
        print(i.ipport,i.itype,i.other,i.isok)

        # print(i["ipport"])
        # for x in i:
        #     print(x)
            # print(i["ip"],i['port'])

# select
# companyid_arr= [str.format(i.companyid) for i in dbs.company_tb.select(dbs.company_tb.companyid)]

#create
# newdict = dict(data_dict, **n)
# 方法1
# StudentsInfo.create(student_name='amos', student_no=880)
# 方法2
# StudentsInfo.insert(student_name='lucy', student_no=881).execute()
#
# 删
# 单条删除
# st = StudentsInfo.get(student_name='hom')
# st.delete_instance()
# 等同于DELETE
# from student_info where
#
# student_name = 'hom'
#
# 多条删除
# StudentsInfo.delete().where(StudentsInfo.student_no < 883).execute()
# 等同于DELETE
# from student_info where
#
# student_no < 883
#
# 改
# 方法1指定数据
# StudentsInfo.update(student_no=890).where(StudentsInfo.student_name == 'baby').execute()
# 方法2依据原有数据自动更新
# StudentsInfo.update(student_no=StudentsInfo.student_no + 1).where(StudentsInfo.student_name == 'baby').execute()
# 方法3
# 多字段更新
# StudentsInfo.update(student_no=890, student_name='lady').where(StudentsInfo.student_name == 'baby').execute()
#
# 查
# 1.
# 一般查询
# st1 = StudentsInfo.select()
# 查询所有的记录并获取他们
# for i in st1:
#     print
#     i.student_no, i.student_name
#
# 2.
# 单条查询
# st2 = StudentsInfo.get(StudentsInfo.student_no == 883)
# print
# st2.student_no, st2.student_name
#
# 对比1和2个区别
# 先获取他们的类型
# print
# type(st1) == > <
#
#
# class 'peewee.SelectQuery'>
#
#
# Print
# type(st2) == > <
#
#
# class 'createDB.StudentsInfo'>
#
#
# st1是’SelectQuery
# '类型需要使用for循环逐条获取，而st2本身就是一个实例的对象可以直接获取它的属性
#
# 3.
# 查询部分字段
# st3 = StudentsInfo.select(StudentsInfo.student_no)
#
# 4.
# 有条件查询
# st4 = StudentsInfo.select().where(StudentsInfo.student_no == 883)
#
# 5.
# 随机查询
# 需要先引入fn
# from peewee import fn
#
# st5 = StudentsInfo.select().order_by(fn.Random()).limit(2)
#
# 6.
# 排序查询
# 正序
# st6 = StudentsInfo.select().order_by(StudentsInfo.student_no.asc())
# 反序
# st6 = StudentsInfo.select().order_by(StudentsInfo.student_no.desc())
#
# 7.
# Not
# in组合查询
# 简单举例，现有学生信息表student_info学生姓名student_name和学号student_no，学生成绩表score_table学号student_no和分数score
# st7 = StudentsInfo.select(StudentsInfo.student_no).where(StudentsInfo.student_no > 880)
# sc = StudentsScore.select().where(StudentsScore.student_no.not_in(st7))
# 8.
# 模糊查询
# 比如想要查询学生名字包含’ba’的学生以及学号
# % 符号就相当于sql里的like
# st8 = StudentsInfo.select().where(StudentsInfo.student_name % '%ba%')
# for i in st8:
#     print
#     i.student_no, i.student_name


# if n['xbmsg']: dbs.txErrsor(url=data_dict["ourl"], errtext=newdict['xbmsg'])
# try:
    # dbs.position.create(**newdict)
    #
    # def iplistfomatetbdict(iplist):
    #     pass
    #     ipdict={}
    #     for i in iplist:
    #         ipdict['ipport']=str(i[0])+":"+str(i[1])
    #         ipdict['ip']=i[0]
    #         ipdict['port']=i[1]
    #         ipdict['itype']=i[4]
    #         ipdict['other']=str(i[2])+str(i[3])
    #         # 'c_time': '',
    #         # 'l_time': '',
    #     return ipdict