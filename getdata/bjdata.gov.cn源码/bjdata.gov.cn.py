from bs4 import BeautifulSoup#用于解析网页
import requests
import os, sys
from urllib import request



# def single_get_first(unicode1):
#     str1 = unicode1.encode('gbk')
#     try:
#         ord(str1)
#         return str1
#     except:
#         asc = str1[0] * 256 + str1[1] - 65536
#         if asc >= -20319 and asc <= -20284:
#             return 'a'
#         if asc >= -20283 and asc <= -19776:
#             return 'b'
#         if asc >= -19775 and asc <= -19219:
#             return 'c'
#         if asc >= -19218 and asc <= -18711:
#             return 'd'
#         if asc >= -18710 and asc <= -18527:
#             return 'e'
#         if asc >= -18526 and asc <= -18240:
#             return 'f'
#         if asc >= -18239 and asc <= -17923:
#             return 'g'
#         if asc >= -17922 and asc <= -17418:
#             return 'h'
#         if asc >= -17417 and asc <= -16475:
#             return 'j'
#         if asc >= -16474 and asc <= -16213:
#             return 'k'
#         if asc >= -16212 and asc <= -15641:
#             return 'l'
#         if asc >= -15640 and asc <= -15166:
#             return 'm'
#         if asc >= -15165 and asc <= -14923:
#             return 'n'
#         if asc >= -14922 and asc <= -14915:
#             return 'o'
#         if asc >= -14914 and asc <= -14631:
#             return 'p'
#         if asc >= -14630 and asc <= -14150:
#             return 'q'
#         if asc >= -14149 and asc <= -14091:
#             return 'r'
#         if asc >= -14090 and asc <= -13119:
#             return 's'
#         if asc >= -13118 and asc <= -12839:
#             return 't'
#         if asc >= -12838 and asc <= -12557:
#             return 'w'
#         if asc >= -12556 and asc <= -11848:
#             return 'x'
#         if asc >= -11847 and asc <= -11056:
#             return 'y'
#         if asc >= -11055 and asc <= -10247:
#             return 'z'
#         return ''
#
#
# def getPinyin(string):
#     if string == None:
#         return None
#     lst = list(string)
#     charLst = []
#     for l in lst:
#         charLst.append(single_get_first(l))
#     return ''.join(charLst)
#
# # 获取所有目录的网址中的id
# response = requests.get("http://www.bjdata.gov.cn/zyml/azt/jjjs/index.htm")
# soup = BeautifulSoup(response.content,"xml")
# li = soup.find(class_="data-menu-list")
# h3 = li.find_all('h3')
# # one_level = h3.get('a')
# for level in h3:
#     # href = level.get('href')
#     one_level = level.string
#     zimu = one_level.split("（")[0]
#     print(one_level)
#     # 各个目录的url
#     url = 'http://www.bjdata.gov.cn/zyml/azt/' + getPinyin(zimu) + '/index.htm'
#     response = requests.get(url,timeout = 60)
#     soup = BeautifulSoup(response.content, "xml")
#     scripts = soup.find_all("iframe")
#     print(scripts)
#     print(one_level)
    # 创建的目录
    # path = "/主题/经济建设（291）/"+ str(one_level)
    # os.makedirs(path, 0o777);
    # print("路径被创建")
# 经济建设（291）1042 信用服务（9）1073 财税金融（27）1072 旅游住宿（39）13 交通服务（34）14 餐饮美食（6）15 医疗健康（52）16
# 文体娱乐（101）17 消费购物（5）18 生活安全（7）19 宗教信仰（7）20 教育科研（78）21 社会保障（70）22 劳动就业（19）23
# 生活服务（43）24 房屋住宅（4）25 政府机构与社会团体（59）26 环境与资源保护（47）27 企业服务（71）28 农业农村（27）29



# 拼接口地址
def download(file_url_num):
    download_url = 'http://www.bjdata.gov.cn/cms/web/APIInterface/userApply.jsp?id=' + str(file_url_num) + '&key=1527743111511'
    return download_url

# 传入接口地址，返回下载文件地址、
def file_down_url(url_f):
    # response = requests.get(url_f,timeout = 500)
    # # result = response.content.decode('utf-8')
    # result = response.text
    response = request.urlopen(url_f, data = None, timeout = 500)
    result = response.read().decode('utf-8')
    re = result.split('"')
    # 防止对方服务器太水，出现‘远程主机强迫关闭一个现有连接’，每次open后close
    response.close()
    return re[-2]

# 获取该分类所有数据        # 目录和id已经获取到，网站不稳定，所以一个一个目录跑数据，手动改id和文件路径
url1 = "http://www.bjdata.gov.cn/cms/web/templateIndexList/indexList.jsp?currPage="
url2 = "&channelID=22&sortType=null&orderBy=null"
page = 1
url_list = []
downcsv_url = []
while page < 31:
    url = url1 + str(page) + url2
    # print(url)
    page = page + 1
    url_list.append(url)

for url3 in url_list:
    response = requests.get(url3)
    soup = BeautifulSoup(response.content,"html5lib")
    # print(soup)
    # 获取列表herf
    t1 = soup.find_all(class_ = "ztrit_box fn-clear " )
    # print(t1)
    for t2 in t1:
        t3 = t2.find('a')
        href = t3.get('href')
        # print(href)
        print(t3.string)
        file_name = t3.string
        # 目录和id已经获取到，网站不稳定，所以一个一个目录跑数据，手动改id和文件路径
        path = "/主题/社会保障（70）/" + file_name.strip()
        # print(path)
        os.makedirs(path, 0o777);
        print("文件夹被创建")
        response = requests.get(href)
        soup = BeautifulSoup(response.content, "html5lib")
        t1 = soup.find(class_='btn_sjdownload_small')
        # 如果没有接口跳过
        if '' == t1 or t1 is not None:
            interface_href = t1.get("href")
            interface_url = "http://www.bjdata.gov.cn" + interface_href
            print(interface_url)
            response = requests.get(interface_url)
            soup = BeautifulSoup(response.content, "lxml")
            file_num = soup.find_all("td")
            # print(file_num)
            # 分为文件格式
            doc_num = 0
            csv_num = 0
            xls_num = 0
            zip_num = 0
            len_file = len(file_num)

            for file in file_num:
                td_content = str(file)
                if td_content == '<td>csv</td>':
                    break
                csv_num += 1
            for file in file_num:
                td_content = str(file)
                if td_content == '<td>xls</td>':
                    break
                xls_num += 1
            for file in file_num:
                td_content = str(file)
                if td_content == '<td>zip</td>':
                    break
                zip_num += 1
            for file in file_num:
                td_content = str(file)
                if td_content == '<td>doc</td>':
                    break
                doc_num += 1
            if csv_num + 2 <= len_file:
                csv_file_num = str(file_num[csv_num + 2])
                # 接口页面
                url_f = download(csv_file_num[4:-5])
                print(url_f)
                # 接口内容中文件下载地址
                file_url = file_down_url(url_f)
                r = requests.get(file_url)
                name = path + "/" + file_name.strip() + ".csv"
                with open(name, "wb") as code:
                     code.write(r.content)
            if xls_num + 2 <= len_file:
                xls_file_num = str(file_num[xls_num + 2])
                # 接口页面
                url_f = download(xls_file_num[4:-5])
                # print(url_f)
                # 接口内容中文件下载地址
                file_url = file_down_url(url_f)
                r = requests.get(file_url)
                name = path + "/" + file_name.strip() + ".xls"
                with open(name, "wb") as code:
                     code.write(r.content)
            if zip_num + 2 <= len_file:
                zip_file_num = str(file_num[zip_num + 2])
                # 接口页面
                url_f = download(zip_file_num[4:-5])
                print(url_f)
                # 接口内容中文件下载地址
                file_url = file_down_url(url_f)
                r = requests.get(file_url)
                name = path + "/" + file_name.strip() + ".zip"
                with open(name, "wb") as code:
                     code.write(r.content)
            if doc_num + 2 <= len_file:
                doc_file_num = str(file_num[doc_num + 2])
                # 接口页面
                url_f = download(doc_file_num[4:-5])
                print(url_f)
                # 接口内容中文件下载地址
                file_url = file_down_url(url_f)
                r = requests.get(file_url)
                name = path + "/" + file_name.strip() + ".doc"
                with open(name, "wb") as code:
                     code.write(r.content)
            # print(doc_num,csv_num,xls_num,zip_num)
