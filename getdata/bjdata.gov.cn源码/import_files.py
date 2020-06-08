from bs4 import BeautifulSoup#用于解析网页
import requests
import os, sys
from urllib import request

# 经济建设（291）1042
# 信用服务（9）1073
# 财税金融（27）1072
# 旅游住宿（39）13
# 交通服务（34）14
# 餐饮美食（6）15
# 医疗健康（52）16
# 文体娱乐（101）17
# 消费购物（5）18
# 生活安全（7）19
# 宗教信仰（7）20
# 教育科研（78）21
# 社会保障（70）22
# 劳动就业（19）23
# 生活服务（43）24
# 房屋住宅（4）25
# 政府机构与社会团体（59）26
# 环境与资源保护（47）27
# 企业服务（71）28
# 农业农村（27）29
def download(file_url_num):
    download_url = 'http://www.bjdata.gov.cn/cms/web/APIInterface/userApply.jsp?id=' + str(file_url_num) + '&key=1527743111511'
    return download_url

# 获取该分类所有数据
url1 = "http://www.bjdata.gov.cn/cms/web/templateIndexList/indexList.jsp?currPage="
url2 = "&channelID=29&sortType=null&orderBy=null"
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
        path = "/主题/农业农村（27）/" + file_name.strip()
        # print(path)
        os.makedirs(path, 0o777);
        print("文件夹被创建")
        response = requests.get(href)
        soup = BeautifulSoup(response.content, "html5lib")
        t1 = soup.find(class_='btn_sjdownload_small')
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
            # response = requests.get(url_f,timeout = 500)
            # # result = response.content.decode('utf-8')
            # result = response.text
            response = request.urlopen(url_f, data = None, timeout = 500)
            result = response.read().decode('utf-8')
            re = result.split('"')
            print(re[-2])
            r = requests.get(re[-2])
            name = path + "/" + file_name.strip() + ".csv"
            with open(name, "wb") as code:
                 code.write(r.content)
        if xls_num + 2 <= len_file:
            xls_file_num = str(file_num[xls_num + 2])
            # 接口页面
            url_f = download(xls_file_num[4:-5])
            # print(url_f)
            # 接口内容中文件下载地址
            # response = requests.get(url_f,timeout = 500)
            # # result = response.content.decode('utf-8')
            # result = response.text
            response = request.urlopen(url_f, data = None, timeout = 500)
            result = response.read().decode('utf-8')
            re = result.split('"')
            print(re[-2])
            r = requests.get(re[-2])
            name = path + "/" + file_name.strip() + ".xls"
            with open(name, "wb") as code:
                 code.write(r.content)
        if zip_num + 2 <= len_file:
            zip_file_num = str(file_num[zip_num + 2])
            # 接口页面
            url_f = download(zip_file_num[4:-5])
            print(url_f)
            # 接口内容中文件下载地址
            # response = requests.get(url_f,timeout = 500)
            # # result = response.content.decode('utf-8')
            # result = response.text
            response = request.urlopen(url_f, data = None, timeout = 500)
            result = response.read().decode('utf-8')
            re = result.split('"')
            print(re[-2])
            r = requests.get(re[-2])
            name = path + "/" + file_name.strip() + ".zip"
            with open(name, "wb") as code:
                 code.write(r.content)
        if doc_num + 2 <= len_file:
            doc_file_num = str(file_num[doc_num + 2])
            # 接口页面
            url_f = download(doc_file_num[4:-5])
            print(url_f)
            # 接口内容中文件下载地址
            # response = requests.get(url_f,timeout = 500)
            # # result = response.content.decode('utf-8')
            # result = response.text
            response = request.urlopen(url_f, data = None, timeout = 500)
            result = response.read().decode('utf-8')
            re = result.split('"')
            print(re[-2])
            r = requests.get(re[-2])
            name = path + "/" + file_name.strip() + ".doc"
            with open(name, "wb") as code:
                 code.write(r.content)
        # print(doc_num,csv_num,xls_num,zip_num)
