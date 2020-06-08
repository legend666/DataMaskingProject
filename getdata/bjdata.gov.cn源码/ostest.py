#!/usr/bin/python3

# import os, sys
#
# # 创建的目录
# path = "/tmp/home/monthly/dai"
#
# os.makedirs( path, 0o777 );
#
# print ("路径被创建")
def download(file_url_num):
    download_url = 'http://www.bjdata.gov.cn/cms/web/APIInterface/userApply.jsp?id=' + str(file_url_num) + '&key=1527229372554'
    return download_url


heh = download(66666666)
print(heh)