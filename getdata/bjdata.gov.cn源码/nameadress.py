# coding=utf-8
import csv
import sys
import codecs
import pymssql

# reload(sys)
# sys.setdefaultencoding('utf-8')
# 'E:\地址文件\食品及相关产品许可证获证企业.csv'
# csv_filename = sys.argv[1]
csv_filename = 'E:\地址文件\食品及相关产品许可证获证企业.csv'
# database = sys.argv[2]
# table_name = sys.argv[3]
table_name = '北京市定点屠宰企业名单$'

file = codecs.open(csv_filename, 'r', 'gb18030')
reader = file.readline()
b = reader.split(',')
print(b)
colum = ''
for a in b:
    colum = colum + a + ' varchar(255),'
colum = colum[:-1]
print(colum)
create = 'create table if not exists ' + table_name + ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'
print(create)
data = 'LOAD DATA LOCAL INFILE \'' + csv_filename + '\' INTO TABLE ' + table_name + ' character set utf8 FIELDS TERMINATED BY \',\' ENCLOSED BY \'\"\' LINES TERMINATED BY \'' + r'\r\n' + '\' IGNORE 1 LINES;'
print(data)
# e = unicode(data, 'utf8')
server = "127.0.0.1"
user = "sa"
password = "123456"
database = "bjdatagov"

conn = pymssql.connect(server, user, password, database,charset='utf8')
cursor = conn.cursor()
# cursor.execute('SET NAMES utf8;')
# cursor.execute('SET character_set_connection=utf8;')
print(create)
cursor.execute(create)
# cursor.execute(e)
cursor.rowcount

conn.commit()
cursor.close()
print('OK')