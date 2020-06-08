#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 15:18
# @Author  : legend
import re
import csv
from xml.dom.minidom import parse
from stdnum import luhn
import numpy as np
import datetime
starttime = datetime.datetime.now()
assert_list = []
# 读取xml配置文件路径
dom = parse("finders_default.xml")
# 获取文件元素对象
document = dom.documentElement
# 读取配置文件中ipinfo数据
finder_list = document.getElementsByTagName("finder")
with open("fake_data.csv", "r") as csvfile:
    datas = csv.reader(csvfile)
    for data in datas:
        # 记录一行的数据匹配情况
        temp_list = []
        for element in data:
            temp = str(element)
            # print(temp)
            len_old = len(temp_list)
            for finder in finder_list:
                # 取到xml中的正则表达式
                pattern_list = finder.getElementsByTagName("pattern")
                # 取到xml中表达式对应的name
                name_list = finder.getElementsByTagName("name")
                if not pattern_list == []:
                    # 获取pattern中的值
                    pattern = pattern_list[0].childNodes[0].data.strip()
                    # 进行正则匹配
                    finder_pat = re.compile(pattern)
                    find = re.search(finder_pat, temp)
                    if find:
                        # 如果匹配成功，就添加正则对应的name
                        name = name_list[0].childNodes[0].data.strip()
                        temp_list.append(name)
                        break
            # 如果xml中的正则表达式匹配到数据，就跳出循环，继续下一个数据，没匹配到就继续下面的方法在判断
            if len_old < len(temp_list):
                continue
            # 银行卡号匹配
            credit_card_number = luhn.is_valid(temp)
            if credit_card_number:
                temp_list.append('credit_card')
                continue
            else:
                temp_list.append("unknown")
        # print(temp_list)
        assert_list.append(temp_list)
csvfile.close()
# print(assert_list)
ar=np.array(assert_list)
# 用np和两层循环获取一列的值时间差不多。。。
for i in range(len(assert_list[0])):
    column = ar[:, i]
    d = {}
    for i in set(column):
        d[i] = 0
    # print(d)
    # 循环列中的元素，如果相同就加一（就是计数，看看每个元素有多少）
    for i in column:
        for key in d:
            if str(i) == str(key):
                d[key] = d[key]+1
    print(d)
# for i in range(len(assert_list[0])):
#     # 每一列的元素
#     column = []
#     for list in assert_list:
#         column.append(list[i])
#     # print(column)
#     # 把每列的元素去重，然后建成字典，元素为key，值为0
#     d = {}
#     for i in set(column):
#         d[i] = 0
#     # print(d)
#     # 循环列中的元素，如果相同就加一（就是计数，看看每个元素有多少）
#     for i in column:
#         for key in d:
#             if str(i) == str(key):
#                 d[key] = d[key]+1
#     print(d)
endtime = datetime.datetime.now()
print(endtime - starttime)
