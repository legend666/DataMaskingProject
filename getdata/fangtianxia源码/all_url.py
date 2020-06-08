from urllib.request import urlopen#用于获取网页\
from bs4 import BeautifulSoup#用于解析网页
import requests

def spider_1(url,area):
    try:
        response = requests.get(url,timeout = 1000)
    except:
        print(url + "访问失败")
    soup = BeautifulSoup(response.text,'lxml')
    danjias = soup.select('dd > div.moreInfo > p.danjia.alignR.mt5')  # 单价
    courts = soup.select('dd > p:nth-of-type(3) > a')   # 小区
    adds = soup.select('dd > p:nth-of-type(3) > span')  # 地址
    for court, add,danjia in zip(courts, adds,danjias):
        # print(area)
        data = {
            'court': court.get_text(),
            'area': area,
            'add': add.get_text(),
            'danjia': danjia.get_text(),
        }
        fout = open("重庆.txt", "a+",encoding='gb18030')
        print(data,file=fout)
        fout.close()

res = requests.get("http://esf.cq.fang.com/",timeout = 600)
res.encoding = 'gb18030'
soup = BeautifulSoup(res.text,'lxml')
# html = urlopen('http://esf.fang.com/')
# bsObj = BeautifulSoup(html, 'html.parser')
t1 = soup.find(class_ = "qxName" )
t2 = t1.find_all('a')
list = []
area_list = []
# 获取区域如朝阳，海淀，丰台
for t3 in t2:
    t4 = t3.get('href')
    url = 'http://esf.cq.fang.com/' + str(t4)
    area = t3.string
            # ).encode('latin-1').decode('gb18030')
    area_list.append(area)
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
for url2,area1 in zip(list[1:],area_list[1:]):
    print(url2)
    print(area1)
    # j340是保证每页显示40条数据
    spider_1(url2 + 'j340',area1)
    page = 1
    while page < 99:
        url3 = url2 + 'i3' + str(page) + '-j340/'
        print(url3)
        spider_1(url3,area1)
        page = page + 1



