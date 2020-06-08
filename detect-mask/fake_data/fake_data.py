#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 9:16
# @Author  : legend

import csv
import pymssql
from faker import Factory



class Fake_data:
    # 数据库信息
    # def __init__(self,host,user,pwd,dbname,table_name):
    #     self.host = host
    #     self.user = user
    #     self.pwd = pwd
    #     self.dbname = dbname
    #     self.connect_db()
    #     self.table_name = table_name
    # # 链接数据库
    # def connect_db(self):
    #     try:
    #         self.conn = pymssql.connect(user=self.user,password=self.pwd,host=self.host,database=self.dbname,charset="utf8")
    #         self.cur = self.conn.cursor()
    #     except:
    #         print("ERROR:fail to connect mssql")
    # def __del__(self):
    #     self.cur.close()
    #     self.conn.close()
    def fake(self):
        fake = Factory.create('zh_CN')
        # # 名字，地址，邮编，信用卡号，日期，邮箱，ipv4，mac地址，电话号码，身份证号,公司
        data_list = []
        for i in range(10000):
            temp = []
            temp.append(fake.name())
            temp.append(fake.address())
            temp.append(fake.postcode())
            temp.append(fake.credit_card_number())
            temp.append(fake.date())
            temp.append(fake.email())
            temp.append(fake.ipv4())
            temp.append(fake.mac_address())
            temp.append(fake.phone_number())
            temp.append(fake.ssn())
            temp.append(fake.company())
            data_list.append(tuple(temp))
        # print(data_list)
        return data_list
    def write_csv(self,data_list):
        csvFile3 = open('fake_data.csv', 'w', newline='')
        writer2 = csv.writer(csvFile3)
        for data in data_list:
            writer2.writerow(data)
        csvFile3.close()


    def creat_table(self,data_list):
        create_sql = '''create table [fakers] (name varchar(100),adress varchar(100),
                    postcode varchar(100),card_number varchar(100),data varchar(100),
                    email varchar(100),ipv4 varchar(100),mac_add varchar(100),
                    phone_num varchar(100),ssn varchar(100),company varchar(100))'''
        try:
            self.connect_db()
            self.cur.execute(create_sql)
            self.conn.commit()
            print("=======faker创建成功")
        except Exception as e:
            print("=======创建table: % s时出错： % s" % ('faker', e))
        temp_q = ""
        for i in range(0, data_list[0].__len__()):
            temp_q = temp_q + "%s"
            if i < data_list[0].__len__() - 1:
                temp_q = temp_q + ','
        insert_sql = "use faker;insert into fakers values(" + temp_q + ")"
        try:
            self.cur.executemany(insert_sql,data_list)
            self.conn.commit()
        except Exception as e:
            print("执行sql: % s时出错： % s" % (insert_sql, e))
if __name__ == '__main__':
    host = "192.168.59.59"
    user = "sa"
    pwd = "123456"
    db = "faker"
    table_name = "faker"
    item = Fake_data()
    data_list = item.fake()
    item.write_csv(data_list)