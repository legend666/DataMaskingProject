#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 10:34
# @Author  : legend

import pymysql
# 打开数据库连接
db = pymysql.connect("localhost","root","123456","taotao" )
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE ( 
         FIRST_NAME  CHAR(20) NOT NULL, 
         LAST_NAME  CHAR(20), 
         AGE INT,   
         SEX CHAR(1), 
         INCOME FLOAT )"""
cursor.execute(sql)
print("CREATE TABLE OK")
# 关闭数据库连接
db.close()