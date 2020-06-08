#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 11:48
# @Author  : legend

# 同样参照java的DataBaseMetaData包，看看都实现那些功能，在用Python写一遍，但是我能看到的都是调用方法，没有看到方法的实现
# https://www.oschina.net/uploads/doc/javase-6-doc-api-zh_CN/java/sql/DatabaseMetaData.html
# getDataBaseInfo(); // 获取数据库信息：
# 数据库已知的用户# select * from master..syslogins；
# 数据库的系统函数的逗号分隔列表；数据库的时间和日期函数的逗号分隔列表；
# 数据库的字符串函数的逗号分隔列表；数据库供应商用于 'schema' 的首选术语；数据库URL，是否允许只读；
# 数据库的产品名称；数据库的版本；驱动程序的名称，驱动程序的版本；数据库中使用的表类型
# getSchemasInfo(); // 获取数据库所有Schema
# getTablesList(); // 获取某用户下所有的表
# 获取某库下的所有表
# SELECT * FROM [meta_data].INFORMATION_SCHEMA.TABLES
# getTablesInfo(); // 获取表信息
# getPrimaryKeysInfo(); // 获取表主键信息
# getIndexInfo(); // 获取表索引信息
# getColumnsInfo(); // 获取表中列值信息