#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 10:22
# @Author  : legend

import jieba

# seg_list = jieba.cut("北京市朝阳区酒仙桥路2号798东街", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# import jieba
#
# seg_list = jieba.cut("慈云寺北里207号", cut_all=True, HMM=False)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# seg_list = jieba.cut("望京东", cut_all=False, HMM=True)
# print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

# seg_list = jieba.cut("望京东", HMM=False)
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("望京东", HMM=False)  # 搜索引擎模式
# print(", ".join(seg_list))


str = '月华北大街30号'
address = list(str)
length =len(address)
for i in range(length):
    if address[i].isdigit() == 1:
        break
print(''.join(address[0:i]))
print(''.join(address[i:]))