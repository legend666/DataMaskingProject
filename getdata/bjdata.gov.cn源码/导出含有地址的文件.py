# -*- coding: utf-8 -*-

import shutil
import os
import xlrd

# # 文件夹内的所有文件名
# path = "E:\主题\文体娱乐（101）\“北京榜样”周榜人物"
# dirs = os.listdir( path )
# print(dirs)
# # 移动文件
# shutil.copy("E:\主题\文体娱乐（101）\“北京榜样”周榜人物\“北京榜样”周榜人物.csv","E:\主题\文体娱乐（101）\“北京榜样”周榜人物.cs

# with open('E:\主题\文体娱乐（101）\“北京榜样”周榜人物\“北京榜样”周榜人物.csv', 'r') as f:
#     a = f.readline()
#     print(a)
# if a.find("ha ") >= 0 :
#     shutil.copy("E:\主题\文体娱乐（101）\“北京榜样”周榜人物\“北京榜样”周榜人物.csv", "E:\主题\“北京榜样”周榜人物.csv")
#     print("复制成功")
#
# 判断是否存在
# if os.path.isfile("E:\主题\交通服务（34）\公共交通及客运出租小轿车\公共交通及客运出租小轿车.csv"):
#     print("有")


path = "E:\主题"
dirs = os.listdir(path)
# 列举文件夹内的名称
# print(dirs)
for catelog in dirs:
    catelog_path = path + "/" + catelog
    print(catelog_path)
    catelog_dirs = os.listdir(catelog_path)
    # print(catelog_dirs)
    for file in catelog_dirs:
        file_path = catelog_path + "/" + file
        print(file)
        # final_path = file_path + "/" + file + ".csv"
        # print(final_path)
        # if os.path.isfile(final_path):
        #     with open(final_path, 'r',encoding= 'gb18030') as f:
        #         first_line = ()
        #         first_line = f.readline()
        #         if first_line.find("地址") >= 0:
        #             shutil.copy(final_path,"E:\主题\地址文件\\" + file + ".csv")
        #             print(file + "复制成功")
        xls_path = file_path + '\\' + file + '.xls'
        if os.path.exists(xls_path):
            xls = xlrd.open_workbook(xls_path)
            booksheet = xls.sheet_by_index(0)
            row = booksheet.row_values(0)
            first = ','.join(row)
            if first.find("地址") >= 0:
                new_path = 'E:\主题\地址' + '\\' + file + ".xls"
                shutil.copy(xls_path, new_path)
                print(file + "复制成功")

