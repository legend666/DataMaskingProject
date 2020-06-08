#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 14:02
# @Author  : legend

# select t.行政区划代码,t.行政区划名称 from 行政区划 t where t.行政区划名称 like '
# 房山
# %' and t.行政区划代码 like '11%' and t.[乡镇/街道级区划代码] = ''
# a = {'court': '富力城A区', 'area': '朝阳', 'add': '双井-广渠门外大街1号院', 'danjia': '109847元/??O'}
# print(a.split("'")[3])

def SpliteUnit(lens, step, arr, index, results):
    if lens == 0:
        print (arr[:index])
        results.append(arr[:index])
    for i in range(step, lens + 1, 1):
        arr[index] = i
        SpliteUnit(lens - i, i, arr, index + 1, results)

num = 15
result = []
tmp_arr = [0] * num
SpliteUnit(num, 1, tmp_arr, 0, result)