#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 14:52
# @Author  : legend


import pymssql
class MSSQL_Interface :
    # 数据库信息
    def __init__(self,host,user,pwd,dbname,table_name):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.dbname = dbname
        self.connect_db()
        self.table_name = table_name

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
    def read_txt(self,notinajk):
        # (楼房地址信息,楼房地址所在行政区划编码,楼房地址类型ID,街路巷名,门牌号,楼房类型ID,楼房名称)
        file = "E:\\Python-workspace-shenji\\fangtianxia\\二手房\\(已去重)北京小区.txt"
        date_list = []
        sql1 ="select t.行政区划代码 from 行政区划 t where t.行政区划名称 like '"
        sql2 = "%' and t.行政区划代码 like '11%' and t.[乡镇/街道级区划代码] = ''"
        with open(file, 'r', encoding='gb18030') as f:
            for line in f.readlines():
                if line.split("'")[3] in notinajk:
                    self.connect_db()
                    self.cur.execute(sql1+ line.split("'")[7] + sql2)
                    area_code = self.cur.fetchall()
                    # lfdzxx楼房地址信息
                    # print(line.strip().split("'")[11])
                    lfdzxx = line.split("'")[7]+"-"+line.strip().split("'")[11]
                    temp_list = []
                    temp_list.append(lfdzxx)
                    temp_list.append(area_code[0][0])
                    temp_list.append('1')
                    temp_list.append('null')
                    temp_list.append('null')
                    temp_list.append('2')
                    temp_list.append(line.split("'")[3])
                    print(temp_list)
                    date_list.append(tuple(temp_list))
        print(len(date_list))
        return date_list
    def import_list(self, data_list, table_name):  # 输入已经整理好的list格式
        q0 = "use " + self.dbname + ';'
        q1 = "insert into " + '[' +table_name+ ']' + " values("
        temp_q = ""
        for i in range(0, data_list[0].__len__()):
            temp_q = temp_q + "%s"
            if i < data_list[0].__len__() - 1:
                temp_q = temp_q + ','
        query = q0 + q1 + temp_q + ")"
        try:
            self.cur.executemany(query,data_list)
            self.conn.commit()
        except Exception as e:
            print("执行sql: % s时出错： % s" % (query, e))

    def import_file(self,file):
        date = self.read_txt(file)
        self.import_list(date,self.table_name)
if __name__ == '__main__':
    host = "localhost"
    user = "sa"
    pwd = "123456"
    db = "address_model"
    table_name = "楼房地址数据"
    item = MSSQL_Interface(host, user, pwd, db,table_name)
    file = "E:\\Python-workspace-shenji\\fangtianxia\\二手房\\(已去重)北京小区.txt"
    ftx = []
    ajk = []
    notinajk = []
    with open(file, 'r', encoding='gb18030') as f:
        for line in f.readlines():
            ftx.append(line.split("'")[3])
    with open("C:\\Users\\legend\\Desktop\\community_bjl.txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            ajk.append(line.split(",")[0])
    for xiaoqu in ftx:
         if xiaoqu not in ajk:
            notinajk.append(xiaoqu)
    item.import_file(notinajk)



