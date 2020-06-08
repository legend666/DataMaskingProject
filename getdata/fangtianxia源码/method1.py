#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import pymssql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#链接：https://www.zhihu.com/question/27973010/answer/75217495
def str2bin(strText):
    b = bytes((ord(i) for i in strText))
    return b
#codec can be 'gb2312','utf8','gb18030' etc
def getCode(strText,codec):
    b = bytes((ord(i) for i in strText))
    return b.decode(codec)

#参数为tuple类型
def FormatDataSet(tupleRows,codec):
    listRows = []
    for row in tupleRows:
        listRows.append(list(row))
    resList = []
    for row in listRows:
        for i in range(len(row)):
            if (isinstance(row[i], str)):
                row[i] = getCode(row[i], codec)
        resList.append(tuple(row));
    return(resList)

# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称
server = '192.9.95.138'
user = 'sa'
password = '123456'
database = 'shzhcw_ghk'

with open('sql1.txt', 'r',encoding="utf8") as f:
    sql = f.read()
#print(sql)

conn = pymssql.connect(server, user, password, database, charset = 'utf8')
df = pd.read_sql(sql,con=conn)
conn.close()

#print(df)

field = '缴款对象'
df[field] = (df[field].str.encode('latin-1')).str.decode('gb18030')
field = '执收单位名称'
df[field] = (df[field].str.encode('latin-1')).str.decode('gb18030')
field = '收费项目名称'
df[field] = (df[field].str.encode('latin-1')).str.decode('gb18030')
print(df[['执收单位名称','实收金额']])


# 绘图
TData = df[['缴款对象','实收金额']]
print(TData.describe())

import seaborn as sns
sns.distplot(TData['实收金额'], rug=True, hist=False)
plt.show()
