#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/25  11:12
# @Author  : 恋秋轩 & voyage
# @File    : collegeRecommend.py
# @Software: PyCharm

import numpy as np
import pandas as pd

# import requests
import os
import xlwt
from pandas.core.frame import DataFrame
# from compute import MysqlConfig
# from pyspark import Row
# from pyspark.sql import SparkSession
Ldata = [515,426,150]
Wdata = [538,466,150]
Linedata = [[74116,160852,268653],
            [75149,165840,264617],
            [77749,166864,259573],
            [81375,171036,260431],
            [82994,176326,258428]]
line_list=[272187,269189,260034,260697,258770]#17 18 19 20 21
# def recommendTable(score, rank, wen_li):
#     xScore=[]
#     xRank=[]
#     if (wen_li==1):
#         xI = 0
#         df = pd.read_excel('C:/Users/天涯霜雪霁寒宵/Desktop/sql/rankL.xlsx')
#         for i in range(3):
#             if score>=Ldata[i]:
#                 xI = score-Ldata[i]
#                 break
#         for i in range(0, 2027):
#             fxScore=0
#             fxRank = 0
#             if(xI>df['ScoreAvg'].at[i]):
#                 if(df['ScoreMax'].at[i] != df['ScoreAvg'].at[i]):
#                     fxScore = 2 * (xI - df['ScoreAvg'].at[i]) / (df['ScoreMax'].at[i] - df['ScoreAvg'].at[i]) + 0.5
#             else:
#                 if (df['ScoreAvg'].at[i] != df['ScoreMin'].at[i]):
#                     fxScore = 2 * (xI - df['ScoreMin'].at[i]) / (df['ScoreAvg'].at[i] - df['ScoreMin'].at[i]) - 0.5
#             xScore.append(fxScore)
#             if(rank > df['RankAvg'].at[i]):
#                 fxRank = 2 * (rank - df['RankAvg'].at[i]) / (df['RankMax'].at[i] - df['RankAvg'].at[i]) + 0.5
#             else:
#                 fxRank = 2 * (rank - df['RankMin'].at[i]) / (df['RankAvg'].at[i] - df['RankMin'].at[i]) - 0.5
#             xRank.append(fxRank)
#
#         df['f(xScore)'] = DataFrame(xScore)
#         df['f(xRank)'] = DataFrame(xRank)
#         df.to_excel('../dataProcess/rankL_xscore.xlsx')
#         print('---finish---')
#     else:
#         df = pd.read_excel('C:/Users/天涯霜雪霁寒宵/Desktop/sql/rankW.xlsx')
#     return

def select50(rank):
    cont=0
    df1 = DataFrame()
    id_list=[]
    df = pd.read_excel('E:\\360MoveData\\Users\lenovo\Desktop\scoredata\djj.xlsx')
    for i in range(0,2027):
        if df['RankMin'].at[i]>rank:
            id_list.append(i)
            cont+=1
            if cont >= 50:
                break
    df1 = df.loc[id_list]
    # print(df1)
    # df1['SR']=(abs(df1['f(xScore)']*0.5)+abs(df1['f(xRank)']*0.5))*0.1
    # df1['sum'] = df1['f(xScore)'] + df1['f(xRank)']
    # df1['SR'] = (df1['f(xScore)'] * 0.5 + df1['f(xRank)'] * 0.5) * 0.1
    # df1['rank']=df1['RankAvg']
    # srMax = df1['SR'].max()
    # srMin = df1['SR'].min()
    # df1['SR'] = (df1['SR'] - srMin)/(srMax - srMin)
    # print(df1['min_section17'])
    #计算p值
    p_list =[]
    for i in range(0,50):
        flag = 0
        id =  id_list[i]
        # print(df1['min_section17'].at[id])
        if df1['min_section17'].at[id] > rank:
            flag+=1
        if df1['min_section18'].at[id] > rank:
            flag+=1
        if df1['min_section19'].at[id] > rank:
            flag+=1
        if df1['min_section20'].at[id] > rank:
            flag+=1
        if df1['min_section21'].at[id] > rank:
            flag+=1
        p = float(flag/5)
        p_list.append(p)
    print(p_list)
    df1["p"]=p_list
    # print(df1)
    # print(((df1['min_section17']-rank)/rank)**2)
    #计算高校对应省排名与目标排名距离离散度dt
    d1_sum = ((df1['min_section17']-rank)/rank)**2+((df1['min_section18']-rank)/rank)**2\
             +((df1['min_section19']-rank)/rank)**2+((df1['min_section20']-rank)/rank)**2\
             +((df1['min_section21']-rank)/rank)**2
    d1_res = pow(d1_sum,0.5)/5.0
    df1["dt"] = d1_res
    #归一化处理
    dsMax = df1['ds'].max()
    dsMin = df1['ds'].min()
    df1['ds'] = (df1['ds']-dsMin)/(dsMax-dsMin)
    dtMax = df1['dt'].max()
    dtMin = df1['dt'].min()
    df1['dt'] = (df1['dt']-dtMin)/(dtMax-dtMin)
    dcMax = df1['dc'].max()
    dcMin = df1['dc'].min()
    df1['dc'] = (df1['dc']-dcMin)/(dcMax-dcMin)

    pre = df1['p']*0.69+(1-df1['dt'])*0.13+(1-df1['dc'])*0.09+(1-df1['ds'])*0.09

    df1['predict'] = pre
    df1 = df1.sort_values(by='predict')
    print(df1)




    # 计算高校对应省排名与省控线距对应排名距离dc





    # df_p = pd.read_excel('E:\\360MoveData\\Users\lenovo\Desktop\scoredata\\rankL1.xlsx')



    # df1.to_excel('../dataProcess/rankSR.xlsx')
    # df1 = pd.concat([df1, df.loc[i]])
    # df1.append(df.at[i])
    # print(df1)


# def compute_ds():
#
#     # rate_list=[[0.272298089,0.590961361,0.987016279],[0.279168168,0.616072722,0.983015651],
#     #            [0.298995516,0.641700701,0.998227155],[0.312143983,0.656071992,0.998979658],
#     #            [0.320724968,0.681400471,0.998678363]] #17 18 19 20 21 投档线排名/理科总人数
#     # score_list = [[74116,160852,268653], [75149,165840,264617],
#     #              [77749,166864,259573], [81375,171036,260431],
#     #              [82994,176326,258428]]  # 17 18 19 20 21 投档线对应的排名
#     # #
#     # #
#     # #
#     # # df2 = pd.read_excel('E:\\360MoveData\\Users\lenovo\Desktop\scoredata\djjl.xlsx')
#     # # for i in range(0,2027):
#     # #
#     # #     for j in range(0,5):
#
#
#
#
#     #计算该校投档线对应省排名在理科考生的占比平均值f
#     df3 = pd.read_excel('E:\\360MoveData\\Users\lenovo\Desktop\scoredata\djjl.xlsx')
#     #计算占比ci
#     c1 = df3['min_section17']/line_list[0]
#     c2 = df3['min_section18'] / line_list[1]
#     c3 = df3['min_section19'] / line_list[2]
#     c4 = df3['min_section20'] / line_list[3]
#     c5 = df3['min_section21'] / line_list[4]
#     # 求解均值f
#     f = (c1+c2+c3+c4+c5)/5.0
#     # print(f)
#     df3_sum = ((c1 - f)** 2+(c2- f)** 2+(c3- f) ** 2+(c4- f)** 2+(c5- f) ** 2)/5.0
#     ds_res = pow(df3_sum, 0.5)
#     df3["ds"] = ds_res
#     print('---ds_get finish---')
#     df3.to_excel('E:\\360MoveData\\Users\lenovo\Desktop\scoredata\djjl1.xlsx')
#
#
#
# # 五因素之dc获取
# def dc_get():
#     df = pd.read_excel('E:\\360MoveData\\Users\lenovo\Desktop\scoredata\djjl.xlsx')
#     # df_line = pd.read_excel('../dataProcess/scoreline_sichuan.xlsx')
#     year_list=['17','18','19','20','21']
#     dc_list=[]
#     for i in range(0,2027):
#         u_list=[]
#         for j in range(5):
#             province_line=0
#             for k in range(3):
#                 if df['min_section' + year_list[j]].at[i] <= Linedata[j][k]:
#                     province_line = Linedata[j][k]
#                     break
#             u_list.append(df['min_section' + year_list[j]].at[i] - province_line)
#         u_avg=float(sum(u_list))/5.0
#         u_sum=0
#         for e in u_list:
#             u_sum=u_sum+(e-u_avg)**2
#         u_sqrt = pow(u_sum*0.2,0.5)
#         dc_list.append(u_sqrt)
#
#     # print(dc_list)
#     df['dc']=dc_list
#     print('---dc_get finish---')
#     # 计算占比ci
#     c1 = df['min_section17'] / line_list[0]
#     c2 = df['min_section18'] / line_list[1]
#     c3 = df['min_section19'] / line_list[2]
#     c4 = df['min_section20'] / line_list[3]
#     c5 = df['min_section21'] / line_list[4]
#     # 求解均值f
#     f = (c1 + c2 + c3 + c4 + c5) / 5.0
#     # print(f)
#     df3_sum = ((c1 - f) ** 2 + (c2 - f) ** 2 + (c3 - f) ** 2 + (c4 - f) ** 2 + (c5 - f) ** 2) / 5.0
#     ds_res = pow(df3_sum, 0.5)
#     df["ds"] = ds_res
#     print('---ds_get finish---')
#     df.to_excel('E:\\360MoveData\\Users\lenovo\Desktop\scoredata\djj.xlsx')






# dc_get()

# score = int(input("请输入分数："))
rank = int(input("请输入排名："))
# wen_li = int(input("请输入分科："))
# recommendTable(score, rank, wen_li)
# compute_ds()
select50(rank)