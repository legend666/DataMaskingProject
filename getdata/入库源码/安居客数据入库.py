#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 9:08
# @Author  : legend
# 凤凰城,朝阳,三元桥,曙光西里甲5号
# 花家地西里一区[0],朝阳[1],望京西[2],望京西路[3]
# 0属于小区名，1是区域，2属于地区，或者行政区划中的街道。3就是街道，有多少号的就截取一下
# 楼房地址信息:朝阳-望京西-望京西路
# 门牌号：null
# 街巷路名：望京西路，
# 楼房名称：花家地西里一区


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
    def read_txt(self,file):
        # (楼房地址信息,楼房地址所在行政区划编码,楼房地址类型ID,街路巷名,门牌号,楼房类型ID,楼房名称)
        date_list = []
        sql1 ="select t.行政区划代码 from 行政区划 t where t.行政区划名称 like '"
        sql2 = "%' and t.行政区划代码 like '11%' and t.[乡镇/街道级区划代码] = ''"
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                self.connect_db()
                self.cur.execute(sql1+ line.split(',')[1] + sql2)
                area_code = self.cur.fetchall()
                # lfdzxx楼房地址信息
                lfdzxx = '-'.join(line.strip().split(',')[1:])
                temp_list = []
                temp_list.append(lfdzxx)
                temp_list.append(area_code[0][0])
                temp_list.append('1')
                temp_list.append(line.strip().split(',')[3])
                temp_list.append('null')
                temp_list.append('2')
                temp_list.append(line.split(',')[0])
                print(temp_list)
                date_list.append(tuple(temp_list))
        print(date_list)
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
# 获取街路巷名含有门牌号的地址
    def getroad(self,end):
        sql = "select t.街路巷名 from 楼房地址数据 t  where t.街路巷名 like '" + end + "'"
        self.connect_db()
        try:
            self.cur.execute(sql)
        except Exception as e:
            print(e)
        datas = self.cur.fetchall()
        return datas

    # 把街路巷名和门牌号区分开，并录入到库中
    def part(self,datas):
        for data in datas:
            newdata = data[0].encode('latin-1').decode('gb18030')
            address = list(newdata)
            length = len(address)
            for i in range(length):
                if address[i].isdigit() == 1:
                    break
            road = ''.join(address[0:i])
            road_num = ''.join(address[i:])
            sql1 = "UPDATE [address_model].[dbo].楼房地址数据 SET 街路巷名 = '"
            sql = sql1 + road + "'" + ",门牌号 = '" + road_num + "'" + "where 街路巷名 = '" +newdata+ "'"
            print(sql)
            self.connect_db()
            self.cur.execute(sql)
            self.conn.commit()

    def change_address(self,end):
        datas = self.getroad(end)
        self.part(datas)

        # 获搜房网中含有门牌号的地址
    def getanjukeroad(self):
        sql = "select t.楼房地址信息 from 楼房地址数据 t where t.楼房地址信息 like '%号' and t.门牌号 is null"
        self.connect_db()
        try:
            self.cur.execute(sql)
        except Exception as e:
            print(e)
        datas = self.cur.fetchall()
        self.partanjuke(datas)
    def partanjuke(self,datas):
        for data in datas:
            newdata = data[0].encode('latin-1').decode('gb18030').split('-')
            address = list(newdata[-1])
            length = len(address)
            for i in range(length):
                if address[i].isdigit() == 1:
                    break
            road = ''.join(address[0:i])
            road_num = ''.join(address[i:])
            sql1 = "UPDATE [address_model].[dbo].楼房地址数据 SET 街路巷名 = '"
            sql = sql1 + road + "'" + ",门牌号 = '" + road_num + "'" + "where 楼房地址信息 = '" +data[0].encode('latin-1').decode('gb18030')+ "'"
            print(sql)
            self.connect_db()
            self.cur.execute(sql)
            self.conn.commit()


if __name__ == '__main__':
    host = "localhost"
    user = "sa"
    pwd = "123456"
    db = "address_model"
    table_name = "楼房地址数据"
    item = MSSQL_Interface(host, user, pwd, db,table_name)
    # 导入安居库的数据
    # item.import_file("C:\\Users\\legend\\Desktop\\community_bjl.txt")
    # 主要把安居客的地址中街道和门牌号分开
    # item.change_address("%号")
    item.getanjukeroad()