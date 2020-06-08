# -*- coding: utf-8 -*-
import xlrd
import shutil
import csv
import pandas as pd
# import os
# # 移除
# os.remove('E:/地址文件副本/A级景区.csv')
# print('移除成功')



# xls = xlrd.open_workbook(r'E:\主题\餐饮美食（6）\北京市定点屠宰企业名单\北京市定点屠宰企业名单.xls')
# booksheet = xls.sheet_by_index(0)
# row = booksheet.row_values(0)
# first = ','.join(row)
# print(first.find('地址'))
# xls复制
# xls = "E:\主题\财税金融（27）\按行业分地区生产总值(2013-2016年)\按行业分地区生产总值(2013-2016年).xls"
# new_path = "E:\主题\地址\按行业分地区生产总值(2013-2016年).xls"
# shutil.copy(xls, new_path)
# print()

with open('E:\地址文件\A级景区.csv','r', encoding="gb18030") as csvfile:
    for d in csv.DictReader(csvfile):
        if '名称' in d and '地址' in d:
            print('douyou')
    # 读取csv的一列，名称循环，地址循环，写的时候循环，太浪费，
    reader = csv.DictReader(csvfile)
    column = [row['名称'] for row in reader]
    column2 = [row2['名称'] for row2 in reader]
    print(column2)
    # pd读取办法
    hlengh = len(csvfile.readline())
    data_name = pd.read_csv(filepath_or_buffer = 'E:\地址文件\保健食品生产单位证件信息.csv', sep = ',')["名称"].values
    print(data_name)


    # 写入csv
    for d in csv.DictReader(csvfile):
        name = d['名称'].split('/n')
        adress = d['地址'].split('/n')
        print(d)
        # newline ="" 防止有空行，我也不知道为啥。。。
        with open('E:/主题/名称地址.csv','a',newline= "") as write_file:
            w = csv.writer(write_file)
            w.writerows(zip(name,adress))
            print('写入成功')