from urllib.request import urlopen#用于获取网页\
from bs4 import BeautifulSoup#用于解析网页
import requests
def spider_1(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    courts = soup.select('dd > p:nth-of-type(3) > a')   # 小区
    adds = soup.select('dd > p:nth-of-type(3) > span')  # 地址
    for court, add in zip(courts, adds):
        data = {
            'court': court.get_text(),
            'add': add.get_text(),
        }
        fout = open("fangtianxia.txt", "a+",encoding='gb18030')
        print(data,file=fout)
        fout.close()



html = urlopen('http://esf.fang.com/')
bsObj = BeautifulSoup(html, 'html.parser')
t1 = bsObj.find(class_ = "qxName" )
t2 = t1.find_all('a')
list = []
for t3 in t2:
    t4 = t3.get('href')
    url = 'http://esf.fang.com' + str(t4)
    # print(url)
    list.append(url)
print(list[1:])