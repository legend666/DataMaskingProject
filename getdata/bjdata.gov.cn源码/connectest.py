#!/usr/bin/python
#coding=utf-8
#-------------------------------------------------------------------------------
# Name: datamapper.py
# Purpose: using pyodbc library to operate database
#
# Author: huamin.zhang
#
# Created: 20/04/2013
#-------------------------------------------------------------------------------
import pyodbc
import time
class ODBC_MS:
  ''''' 对pyodbc库的操作进行简单封装
  pyodbc库的下载地址:http://code.google.com/p/pyodbc/downloads/list
  使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启
  此类完成对数据库DB的连接/查询/执行操作
  正确的连接方式如下:
  cnxn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=ZHANGHUAMIN\MSSQLSERVER_ZHM;DATABASE=AdventureWorks2008;UID=sa;PWD=wa1234')
  cnxn = pyodbc.connect(DRIVER='{SQL SERVER}',SERVER=r'ZHANGHUAMIN\MSSQLSERVER_ZHM',DATABASE='AdventureWorks2008',UID='sa',PWD='wa1234',charset="utf-8")
  '''
  def __init__(self, DRIVER,SERVER, DATABASE, UID, PWD):
    ''''' initialization '''
    self.DRIVER = DRIVER
    self.SERVER = SERVER
    self.DATABASE = DATABASE
    self.UID = UID
    self.PWD = PWD
  def __GetConnect(self):
    ''''' Connect to the DB '''
    if not self.DATABASE:
      raise(NameError,"no setting db info")
    self.conn = pyodbc.connect(DRIVER=self.DRIVER, SERVER=self.SERVER, DATABASE=self.DATABASE, UID=self.UID, PWD=self.PWD, charset="UTF-8")
    #self.conn = pyodbc.connect(DRIVER=self.DRIVER, SERVER=self.SERVER, DATABASE=self.DATABASE, UID=self.UID, PWD=self.PWD)
    cur = self.conn.cursor()
    if not cur:
      raise(NameError,"connected failed!")
    else:
      return cur
  def ExecQuery(self, sql):
    ''''' Perform one Sql statement '''
    cur = self.__GetConnect() #建立链接并创建数据库操作指针
    cur.execute(sql)#通过指针来执行sql指令
    ret = cur.fetchall()#通过指针来获取sql指令响应数据
    cur.close()#游标指标关闭
    self.conn.close()#关闭数据库连接
    return ret
  def ExecNoQuery(self,sql):
    ''''' Person one Sql statement like write data, or create table, database and so on'''
    cur = self.__GetConnect()
    cur.execute(sql)
    self.conn.commit()#连接句柄来提交
    cur.close()
    self.conn.close()
def main():
  ms = ODBC_MS('{SQL SERVER}', "127.0.0.1", "bjdatagov", 'sa', '123456')#zhm_db数据库是在sql server 终端里先创建好的
  #ms.ExecNoQuery("drop table Customers_test")
  sql = '''''CREATE TABLE Customers_test
  (
    CustomerNo   int       IDENTITY   NOT NULL,
    CustomerName  varchar(30)         NOT NULL,
    Address1    nvarchar(30)         NOT NULL ,
    Address2    nvarchar(30)         NOT NULL,
    City      nvarchar(20)         NOT NULL,
    State     nchar(20)          NOT NULL,
    Zip      varchar(10)         NOT NULL,
    Contact    varchar(25)         NOT NULL,
    Phone     char(15)           NOT NULL,
    FedIDNo    varchar(9)          NOT NULL,
    DateInSystem  smalldatetime        NOT NULL
  );'''
  ms.ExecNoQuery(sql)
  #注意:在进行插入操作时,自增长度不能够写入
  sql = u'''''insert into Customers_test
  (
    CustomerName,
    Address1,
    Address2,
    City,
    State,
    Zip,
    Contact,
    Phone,
    FedIDNo,
    DateInSystem
  )
  VALUES
  (
    'zhm', '北京市朝阳区', '北京市朝阳区', '北京', '哈哈','3625514', '18001226509', '010-88765879', '21', '2012-09-09'
  );
  '''
  ms.ExecNoQuery(sql)
if __name__ == '__main__':
  main()
