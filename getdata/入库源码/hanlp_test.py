#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/26 14:46
# @Author  : legend

#在线演示：http://hanlp.hankcs.com/
# HanLP主项目文档(java)：https://github.com/hankcs/HanLP/blob/master/README.md
# demo(java)：https://github.com/hankcs/pyhanlp/tree/master/tests/demos
# HanLP自然语言处理包开源 http://www.hankcs.com/nlp/hanlp.html
# hanlp的基本使用--python(自然语言处理)https://www.cnblogs.com/ybf-yyj/p/7801429.html
from pyhanlp import *
# 第一次运行hanlp的方法会自动下载相关配置包
print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
# [你好/vl, ，/w, 欢迎/v, 在/p, Python/nx, 中/f, 调用/v, HanLP/nx, 的/ude1, API/nx]
# 获取单词与词性
for term in HanLP.segment('下雨天地面积水'):
    print('{}\t{}'.format(term.word, term.nature))
    # 下雨天 n
    # 地面 n
    # 积水 n

document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
           "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
           "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
           "严格地进行水资源论证和取水许可的批准。"
# 关键词提取
print(HanLP.extractKeyword(document, 2))
# 自动摘要
print(HanLP.extractSummary(document, 3))
# 依存句法分析
print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))

# 感知机词法分析器
PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
analyzer = PerceptronLexicalAnalyzer()
print(analyzer.analyze("上海华安工业（集团）公司董事长谭旭光和秘书胡花蕊来到美国纽约现代艺术博物馆参观"))
testCase = {"武胜县新学乡政府大楼门前锣鼓喧天",
        "蓝翔给宁夏固原市彭阳县红河镇黑牛沟村捐赠了挖掘机",}
segment = HanLP.segment.enablePlaceRecognize('true')
for sentence in testCase:
    termList = segment.seg(sentence);
    print(termList)



