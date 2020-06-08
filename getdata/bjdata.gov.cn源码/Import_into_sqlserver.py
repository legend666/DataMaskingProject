#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 15:34
# @Author  : legend
import os
import pymssql
import csv

class MSSQL_Interface :
    # 数据库信息
    def __init__(self,host,user,pwd,dbname):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.dbname = dbname
        self.connect_db()

    # 链接数据库
    def connect_db(self):
        try:
            self.conn = pymssql.connect(user=self.user,password=self.pwd,host=self.host,database=self.dbname,charset="utf8")
            self.cur = self.conn.cursor()
        except:
            print("ERROR:fail to connect mssql")
    def __del__(self):
        self.cur.close()
        self.conn.close()
    # 读取文件夹内的文件(必须都为csv文件)
    def read_folder(self,csv_path):
        self.csv_path = csv_path
        file_list = os.listdir(csv_path)
        file_name_list = []
        for file_name in file_list:
            file_name_list.append(file_name)
        self.file_name_list = file_name_list
        return file_name_list

    # 读csv文件
    def read_csv(self,csv_path,table_col):
        file = csv.reader(open(csv_path,'r',encoding="gb18030"))
        # for line in file:
        #     print(line)
        data_list = []
        num = 0
        for row in file:
            if num == 0:
                del_blank = ','.join(row).replace(' ', '').split(',')
                # 遇到第一行有空字段,空字段加”null“+num
                firstline_list = []
                i = 0
                for field in del_blank:
                    if field == '':
                        null_field = "null" + str(i)
                        firstline_list.append(null_field)
                        i = i + 1
                        continue
                    # 防止有重复字段
                    if field in firstline_list:
                        firstline_list.append(field + str(i))
                        continue
                    firstline_list.append(field)
                file_col = firstline_list
                mapping_array = [-1] * table_col.__len__()
                for i in range(0, table_col.__len__()):
                    try:
                        temp_index = file_col.index(table_col[i])
                        mapping_array[i] = temp_index  # mapping_arry[i]记录表中第i列的数据在待导入文件的第几列
                    except:
                        pass
            else:
                temp_new = []
                for i in range(0, table_col.__len__()):
                    if i > len(row)-1:
                        temp_new.append("''")
                        break;
                    if mapping_array[i] >= 0:
                        temp_new.append(row[mapping_array[i]])
                    else:
                        temp_new.append("''")
                data_list.append(tuple(temp_new))
            num = num + 1
        # print(data_list)
        return data_list

    # 创建数据库
    def creat_db(self,csv_name):
        table_name = csv_name[:-4]
        csv_file_path = self.csv_path + '\\' + csv_name
        with open(csv_file_path,'r',encoding='gb18030') as csvfile:
            # replace(' ','')去除所有的空格；[:-1]每行最后一个都有一个/n 得截下去,ps：/n算一个字符
            # rstrip(',')去掉末尾的逗号，split(',')划分成列表
            firstline  = csvfile.readline().replace(' ','')[:-1].rstrip(',').split(',')
            firstline_list = []
            # 遇到第一行有空字段,空字段加”null“+num
            i = 0
            for field in firstline:
                if field == '':
                    null_field = "null" + str(i)
                    firstline_list.append(null_field)
                    i = i + 1
                    continue
                # 防止有重复字段
                if field in firstline_list:
                    firstline_list.append(field + str(i))
                    continue
                firstline_list.append(field)
            fields = ''
            # 每个字段加上数据类型
            for field in firstline_list:
                fields = fields + '[' + field + ']' + ' varchar(4000),'
            # 去掉末尾的逗号
            fields = fields[:-1]
        create_sql = 'create table ' + '[' + table_name + ']' + ' (' + fields +')'
        try:
            self.connect_db()
            self.cur.execute(create_sql)
            self.conn.commit()
            print("======="+ table_name +"创建成功")
        except Exception as e:
            print("=======创建table: % s时出错： % s" % (table_name, e))

    # 获取表中的字段
    def get_col_name(self,table_name):
        q1 = "use " + self.dbname + ';'
        q2 = "select name from syscolumns where id = object_id(N'" + table_name + "')"
        query = q1 + q2
        self.cur.execute(query)
        col_pre_name = self.cur.fetchall()
        col_num = col_pre_name.__len__()
        col_name = []
        for item in col_pre_name:
            col_name.append(item[0])
        return col_name

    def import_list_weak(self, data_list, table_name,csv_file_path):  # 输入已经整理好的list格式
        q0 = "use " + self.dbname + ';'
        q1 = "insert into " + '[' +table_name+ ']' + " values("
        temp_q = ""
        for i in range(0, data_list[0].__len__()):
            temp_q = temp_q + "%s"
            if i < data_list[0].__len__() - 1:
                temp_q = temp_q + ','
        query = q0 + q1 + temp_q + ")"
        print(data_list)
        try:
            self.cur.executemany(query,data_list)
            self.conn.commit()
            # 导入后删除文件，导入之前做好备份
            if os.path.exists(csv_file_path):
                os.remove(csv_file_path)
        except Exception as e:
            print("执行sql: % s时出错： % s" % (query, e))

    def import_file(self,csv_path):
        file_name = self.read_folder(csv_path)
        for file in file_name:
            table_name = file[:-4]
            self.creat_db(file)
            table_col = self.get_col_name(table_name)
            temp_data_list = []
            csv_file_path = csv_path +'\\'+ file
            temp_data_list = self.read_csv(csv_file_path,table_col)
            try:
                self.import_list_weak(temp_data_list,table_name,csv_file_path)
                print(table_name + " insert success, " + str(temp_data_list.__len__()) + " lines is influenced")
            except:
                print("--------------------------------------------------ERROR: "+table_name+" insert fail--------------------------------------------------")


if __name__ == '__main__':
    host = "localhost"
    user = "sa"
    pwd = "123456"
    db = "bjdatagov"
    item = MSSQL_Interface(host, user, pwd, db)
    # table= ['序号', '登记号', '名称', '通讯地址', '邮编', '电话']
    item.import_file('E:\地址文件')
# conn = pymssql.connect(server, user, password, database)
# cursor = conn.cursor()
# cursor.execute(create_sql)
# conn.commit()
# print(file + '成功建立')
# cursor.close()