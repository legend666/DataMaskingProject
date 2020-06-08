from urllib.request import urlopen#用于获取网页\
from bs4 import BeautifulSoup#用于解析网页
import requests
# html = urlopen('http://esf.fang.com/')
# bsObj = BeautifulSoup(html, 'html.parser')
response = requests.get('http://esf.fang.com/')
bsObj = BeautifulSoup(response.content,'lxml',from_encoding='gb18030')
t1 = bsObj.find(class_ = "qxName" )
t2 = t1.find_all('a')
print(t2)
list = []
for t3 in t2:
    t4 = t3.get('href')
    url = 'http://esf.fang.com' + str(t4)
    list.append(url)
# print(list[1:])
for url1 in list[1:]:
    print(url1)