#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/15 9:18
# @Author  : legend


f = open('重庆.txt', 'r',encoding= 'gb18030')
xiaoqu = set()
for line in f.readlines():
    xiaoqu_name = line.split("'")[3]
    if xiaoqu_name not in xiaoqu:
        xiaoqu.add(xiaoqu_name)
        file = open('重庆(去重).txt', 'a+', encoding='gb18030')
        file.write(line)
        file.close()
    # print(xiaoqu_name)
    # xiaoqu.append(xiaoqu_name)
f.close()

print(len(xiaoqu))