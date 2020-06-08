from urllib.request import urlopen#用于获取网页\
from bs4 import BeautifulSoup#用于解析网页
import requests

# def spider_1(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text,'lxml')
#     courts = soup.select('dd > p:nth-of-type(3) > a')   # 小区
#     adds = soup.select('dd > p:nth-of-type(3) > span')  # 地址
#     for court, add in zip(courts, adds):
#         data = {
#             'court': court.get_text(),
#             'add': add.get_text(),
#         }
#         fout = open("fangtianxia.txt", "a+",encoding='gb18030')
#         print(data,file=fout)
#         fout.close()
def spider_1(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    courts = soup.select('dd > p:nth-of-type(3) > a')   # 小区
    data = set()
    for court in courts:
        data.add(court.get_text())
    return data


html = urlopen('http://esf.fang.com/')
bsObj = BeautifulSoup(html, 'html.parser')
t1 = bsObj.find(class_ = "qxName" )
t2 = t1.find_all('a')
list = []
# 获取区域如朝阳，海淀，丰台
for t3 in t2:
    t4 = t3.get('href')
    url = 'http://esf.fang.com' + str(t4)
    # print(url)
    list.append(url)
# print(list[1:])
# 获取的url中第一个包含当前区域的url，选择区域时，数据超过100页。所以需要获取区域下的url
# for url1 in list[1:]:
#     response = requests.get(url1)
#     bsObj = BeautifulSoup(response.content, 'lxml', from_encoding='gb18030')
#     t1 = bsObj.find(class_="contain")
#     t2 = t1.find_all('a')
#     # print(t2)
#     list2 = []
#     for t3 in t2:
#         t4 = t3.get('href')
#         url = 'http://esf.fang.com' + str(t4)
#         list2.append(url)
#     # 取到最终区域下的地点的url
xiaoquming = set()
print(list[1:])
for url2 in list[1:]:
    # j340是保证每页显示40条数据
    s = spider_1(url2 + 'j340')
    xiaoquming = xiaoquming | s
    page = 1
    while page < 100:
        url3 = url2 + 'i3' + str(page) + '-j340/'
        print(url3)
        s_1 = spider_1(url3)
        xiaoquming = xiaoquming | s_1
        # print(xiaoquming)
        # spider_1(url3)
        page = page + 1
fout = open("fangtianxia.txt", "a+",encoding='gb18030')
print(xiaoquming,file=fout)
fout.close()
