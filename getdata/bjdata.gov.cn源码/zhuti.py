from urllib.request import urlopen#用于获取网页\
from bs4 import BeautifulSoup#用于解析网页
import requests
from urllib import request
import html5lib
import csv
import re
import os
# 解析首页，获取左侧菜单
# response = requests.get("http://www.bjdata.gov.cn/zyml/azt/jjjs/index.htm")
# soup = BeautifulSoup(response.content,"xml")
# li = soup.find(class_="data-menu-list")
# h3 = li.find_all('h3')
# # one_level = h3.get('a')
# for level in h3:
#     one_level = level.string
#     print(one_level)
# 获取数据列表
# response = requests.get("http://www.bjdata.gov.cn/cms/web/templateIndexList/indexList.jsp?currPage=1&channelID=180&sortType=null&orderBy=null")
# soup = BeautifulSoup(response.content,"html5lib")
# # print(soup)
# # 获取列表herf
# t1 = soup.find_all(class_ = "ztrit_box fn-clear " )
# # print(t1)
# for t2 in t1:
#     t3 = t2.find('a')
#     href = t3.get('href')
#     print(href)
#     print(t3.string)
# 获取下载地址---无更多
# response = requests.get("http://www.bjdata.gov.cn/zyml/ajg/swhj/5583.htm")
# soup = BeautifulSoup(response.content,"html5lib")
# # print(soup)
# t1 = soup.find(class_ = 'zt_details_shuju fn-clear')
# print(t1)
# 下载文件（需要登录）
# cookie_str = r'JSESSIONID=8CDAECFA16D6C7EBA48747876801A26D'
# cookies = {}
# for line in cookie_str.split(';'):
#     key, value = line.split('=', 1)
#     cookies[key] = value
# print(cookies)
# headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
# url = "http://www.bjdata.gov.cn/cms/web/download/downloadWriteLog.jsp?type=5&attachmentID=12048"
# response = requests.get(url, headers = headers, cookies = cookies)
# with open('text.csv', 'wb') as csvfile:
#     spamwriter = csvfile.writer(csvfile, dialect='excel')
#     # 设置标题
#     spamwriter.writerow(response.content)
#
#
# 获取下载接口连接  zt_details_jiekou fn-clear
response = requests.get("http://www.bjdata.gov.cn/zyml/ajg/smzj/5049.htm")
soup = BeautifulSoup(response.content,"html5lib")
# print(soup)
t1 = soup.find(class_ = 'btn_sjdownload_small')
if '' == t1 or t1 is not  None:
    print("===not none====")
print("=====is none====")
    # href = t1.get("href")
    # print(href)

# /cms/web/APIInterface/dataDoc.jsp?contentID=9004

# 获取下载链接
# response = requests.get("http://www.bjdata.gov.cn/cms/web/APIInterface/dataDoc.jsp?contentID=9639")
# soup = BeautifulSoup(response.content,"lxml")
# file_num = soup.find_all("td")
# print(file_num)
# # # hehe = file_num[0]
# # # haha = '<td>按登记注册类型分从业人员年末人数(1978-2016年)主要统计指标解释_2018-05-28</td>'
# # # print(str(hehe) == haha)
# # # 找到cvs的对应位置，然后查到文件编号
# doc_num = 0
# csv_num = 0
# xls_num = 0
# zip_num = 0
# len_file = len(file_num)
#
# for file in file_num:
#     td_content = str(file)
#     if td_content == '<td>csv</td>':
#         break
#     csv_num += 1
# for file in file_num:
#     td_content = str(file)
#     if td_content == '<td>xls</td>':
#         break
#     xls_num += 1
# for file in file_num:
#     td_content = str(file)
#     if td_content == '<td>zip</td>':
#         break
#     zip_num += 1
# for file in file_num:
#     td_content = str(file)
#     if td_content == '<td>doc</td>':
#         break
#     doc_num += 1
# if csv_num + 2 <= len_file:
#     csv_file_num = str(file_num[csv_num + 2])
#     print(csv_file_num[4:-5])
# if xls_num + 2 <= len_file:
#     xls_file_num = str(file_num[xls_num + 2])
#     print(xls_file_num[4:-5])
# if zip_num + 2 <= len_file:
#     zip_file_num = str(file_num[zip_num + 2])
#     print(zip_file_num[4:-5])
# if doc_num + 2 <= len_file:
#     doc_file_num = str(file_num[doc_num + 2])
#     print(doc_file_num[4:-5])
# print(doc_num,csv_num,xls_num,zip_num)
# # out = re.search('<td>(.*)</td>',str(file_num[i+2])).groups()

# 获取接口中的文件下载链接
# response = requests.get("http://www.bjdata.gov.cn:80/cms/web/APIInterface/userApply.jsp?id=1203410973&key=1527229372554")
# result = response.content.decode('utf-8')
# re = result.split('"')
# print(re[-2])



# 登陆没弄好，之后在研究，改为调用接口,下载文件
# # http://www.bjdata.gov.cn:80/cms/web/APIInterface/userApply.jsp?id=1203410973&key=1527229372554
# from urllib import request
# import csv
# goog_url = "http://www.bjdata.gov.cn:80/docs/2018-05/20180527080228956279.csv"
# response = requests.get(goog_url)
# down_load = response.content.decode('gb18030')
# print(down_load)
# # response = request.urlopen(goog_url)
# # csv = response.read().decode('gb18030')
# # csv_str = str(csv)
# # print(csv)
# lines = down_load.split("\\n")
# fw = open('text.csv', "w")
# for line in lines:
#     fw.write(line+'\n')
# fw.close()
# print ("成功导出CSV文件！")


# 导出文件方法2.万能
# import requests
# print ("downloading with requests")
# url = 'http://www.bjdata.gov.cn:80/docs/2018-05/20180527080228956279.csv'
# r = requests.get(url)
# filename = 'zajiubuxing'
# path = "/主题/经济建设（291）/" + filename
# os.makedirs(path, 0o777);
# print("路径被创建")
# name = path +'/'+ filename+".csv"
# with open(name, "wb") as code:
#      code.write(r.content)

# response = requests.get('http://www.bjdata.gov.cn/cms/web/APIInterface/userApply.jsp?id=734847163&key=1527229372554', timeout=600)
# # result = response.content.decode('gb18030')
# res = response.text
# re = res.split('"')
# print(re[-2])
#
# response = request.urlopen('http://www.bjdata.gov.cn/cms/web/APIInterface/userApply.jsp?id=734847163&key=1527229372554', data=None, timeout=500)
# page = response.read().decode('utf-8')
# print(page)
