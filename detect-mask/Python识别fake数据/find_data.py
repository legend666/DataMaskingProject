#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:39
# @Author  : legend

import re
import csv
from stdnum import luhn
# 验证手机号是否正确
# 限定前三位
phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
# 匹配QQ号,QQ号必须大于5且小于11,看开头不为0
qq_pat = re.compile(r"^[1-9]\d{4,10}$")
# 匹配邮箱
#chlorine-finder 中的 \b[A-Z0-9._%+-]+@([A-Z0-9.-]+)\.([A-Z]{2,4})\b
email_pat = re.compile(r"([\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+)")
# 18位和15位的身份证
ssn18_pat = re.compile("^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$")
print(ssn18_pat)
ssn15_pat = re.compile(r" ^[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{2}$")
ipv4_pat = re.compile(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}")
# ('凤华', '内蒙古自治区汕尾市城北跋街E座 643459', '975975', '4804873990295103466','1988-11-26',
#  'tdong@kong.cn', '121.245.223.235', '81:7f:a3:44:f6:9a', '15516320959', '511826196804032135', '联通时科传媒有限公司')]

assert_list = []
with open("fake_data.csv", "r") as csvfile:
    datas = csv.reader(csvfile) # 读取csv文件，返回的是迭代类型
    for data in datas:
        # 记录一行的数据匹配情况
        temp_list = []
        for element in data:
            temp = str(element)
            #111111111111111111电话
            phone = re.search(phone_pat, temp)
            if phone:
                temp_list.append(1)
                continue
            #2222222222222222222邮箱
            email = re.search(email_pat, temp)
            if email:
                temp_list.append(2)
                continue
            # 1818818181818   18位身份证
            ssn18 = re.search(ssn18_pat,temp)
            if ssn18:
                temp_list.append(18)
                continue
            # 151515151515   15位身份证
            ssn15 = re.search(ssn15_pat,temp)
            if ssn18:
                temp_list.append(15)
                continue
            # 3333333333333333333333卡号
            credit_card_number = luhn.is_valid(temp)
            if credit_card_number:
                temp_list.append(3)
                continue
            ipv4 = re.search(ipv4_pat,temp)
            if ipv4:
                temp_list.append(4)
                continue
            # # QQ号表达式不明显，往后放
            # qq = re.search(qq_pat, temp)
            # if qq:
            #     temp_list.append(4)
            #     continue
            else:
                temp_list.append(0)
            assert_list.append(temp_list)
    print(assert_list)
            # print(element)
        # print(data)
csvfile.close()


