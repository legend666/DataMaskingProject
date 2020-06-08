fangtianxia = open('fang.txt','r',encoding = 'utf-8')
xiaoqus = set()
for line in fangtianxia.readlines():
    xiaoqus.add(line)
# print(xiaoqus)
anxiaoqu = set()
anjuke  = open('community_bj.dict','r',encoding = 'utf-8')
for line in anjuke.readlines():
    anxiaoqu.add(line)

