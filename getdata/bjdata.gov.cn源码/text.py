# 文件下载
# import requests
# image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
#
# r = requests.get(image_url) # create HTTP response object
# print(r)
# with open("python_logo.png",'wb') as f:
#     f.write(r.content)


# 读取csv
# import csv
# with open("20180527080228956279.csv","r") as csvfile:
#     reader = csv.reader(csvfile)
#     #这里不需要readlines
#     for line in reader:
#         print (line)

#
# list = [1,4,6,8134,7,83,2346,8,3]
# print(list.index(3))

import requests
print ("downloading with requests")
url = 'http://www.bjdata.gov.cn:80/docs/2018-05/20180527080228956279.csv'
r = requests.get(url)
name = "hehe"+".csv"
with open(name, "wb") as code:
     code.write(r.content)