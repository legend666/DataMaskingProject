#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 15:01
# @Author  : legend
import pymssql
class area_Interface :
    def __init__(self,host,user,pwd,dbname):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.dbname = dbname
        self.connect_db()
        # self.table_name = table_name

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
    # 算出上级代码
    def findsuperior(self,code, zero, datas):
        superior = []
        superiorcode = code[:-len(zero)] + zero
        superior.append(superiorcode)
        for data in datas:
            if data[0] == superiorcode:
                superior.append(data[1])
                continue
        return superior
    # 拼接出sql
    def creatsql(self,datas):
        for area in datas:
            zxs = (11, 12, 50, 31)
            sjcode = "省级区划代码='"
            sjname = ",省级区划名='"
            dscode = ",地级区划代码='"
            dsname = ",地级区划名='"
            xjcode = ",县级区划代码='"
            xjname = ",县级区划名='"
            xzcode = ",[乡镇/街道级区划代码]='"
            xzname = ",[乡镇/街道级区划名]='"
            sql1 = "UPDATE [address_model].[dbo].[行政区划] SET "
            sql2 = " WHERE [行政区划代码]='"
            # 省
            if area[0][-10:] == '0000000000':
                sql = sql1 + sjcode + area[0] + "'" + sjname + area[1].encode('latin-1').decode('gb18030') + "'" \
                    + sql2 + area[0] + "'"
                print(sql)
                self.connect_db()
                self.cur.execute(sql)
                self.conn.commit()
                continue
            # 市
            if area[0][-8:] == '00000000':
                superiorsj = self.findsuperior(area[0], '0000000000', datas)
                sql = sql1 + sjcode + superiorsj[0] + "'" + sjname + superiorsj[1].encode('latin-1').decode('gb18030') + "'" \
                           + dscode + area[0] + "'" + dsname + area[1].encode('latin-1').decode('gb18030') + "'" \
                           + sql2 + area[0] + "'"
                # print(sql)
                self.connect_db()
                self.cur.execute(sql)
                self.conn.commit()
                continue
            # 县
            if area[0][-6:] == '000000':
                superiorsj = self.findsuperior(area[0], '0000000000', datas)
                if int(area[0][:2]) in zxs:
                    superiords = superiorsj
                else:
                    superiords = self.findsuperior(area[0], '00000000', datas)
                if len(superiords)==1:
                    superiords=[area[0],area[1]]
                # print(superiords)
                sql = sql1 + sjcode + superiorsj[0] + "'" + sjname + superiorsj[1].encode('latin-1').decode('gb18030') + "'" \
                      + dscode + superiords[0] + "'" + dsname + superiords[1].encode('latin-1').decode('gb18030') + "'" \
                      + xjcode + area[0] + "'" + xjname + area[1].encode('latin-1').decode('gb18030') + "'" \
                      + sql2 + area[0] + "'"
                # print(sql)
                self.connect_db()
                self.cur.execute(sql)
                self.conn.commit()
                continue
            # 乡镇/街道
            else:
                superiorsj = self.findsuperior(area[0], '0000000000', datas)
                if int(area[0][:2]) in zxs:
                    superiords = superiorsj
                else:
                    superiords = self.findsuperior(area[0], '00000000', datas)
                if len(superiords) == 1:
                    superiords = self.findsuperior(area[0], '000000', datas)
                superiorxj = self.findsuperior(area[0], '000000', datas)
                sql = sql1 + sjcode + superiorsj[0] + "'" + sjname + superiorsj[1].encode('latin-1').decode('gb18030') + "'" \
                      + dscode + superiords[0] + "'" + dsname + superiords[1].encode('latin-1').decode('gb18030') + "'" \
                      + xjcode + superiorxj[0] + "'" + xjname + superiorxj[1].encode('latin-1').decode('gb18030') + "'" \
                      + xzcode + area[0] + "'" + xzname + area[1].encode('latin-1').decode('gb18030') + "'" \
                      + sql2 + area[0] + "'"
                # print(sql)
                self.connect_db()
                self.cur.execute(sql)
                self.conn.commit()
                continue
    def insert_data(self,sql):
        self.connect_db()
        self.cur.execute(sql)
        datas = self.cur.fetchall()
        self.creatsql(datas)

if __name__ == '__main__':
    host = "localhost"
    user = "sa"
    pwd = "123456"
    db = "address_model"
    item = area_Interface(host, user, pwd, db)
    # table= ['序号', '登记号', '名称', '通讯地址', '邮编', '电话']
    sql="""SELECT [行政区划代码]
      ,[行政区划名称]
      ,[省级区划代码]
      ,[省级区划名]
      ,[地级区划代码]
      ,[地级区划名]
      ,[县级区划代码]
      ,[县级区划名]
      ,[乡镇/街道级区划代码]
      ,[乡镇/街道级区划名]
      ,[曾用名]
      ,[flag]
  FROM [address_model].[dbo].[行政区划] """
    item.insert_data(sql)