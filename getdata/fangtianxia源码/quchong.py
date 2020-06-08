# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
def spider_1(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    courts = soup.select('dd > p:nth-of-type(3) > a')   # 小区
    data = set()
    for court in courts:
        data.add(court.get_text())
    return data
    # print(data)
    # fout = open("fangtianxia.txt", "a+",encoding='gb18030')
    # print(data,file=fout)
    # fout.close()
url2 = 'http://esf.fang.com/house-a01-b02324/'
spider_1(url2 + 'j340')
page = 1
xiaoquming = set()
while page < 3:
    url = url2 + 'i3' +str(page) + '-j340/'
    print(url)
    s = spider_1(url)
    xiaoquming = xiaoquming | s
    page = page + 1
print(xiaoquming)
fout = open("fangtianxia.txt", "a+",encoding='gb18030')
print(xiaoquming,file=fout)
fout.close()