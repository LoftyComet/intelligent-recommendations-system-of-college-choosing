#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/25  11:12
# @Author  : 恋秋轩 & voyage
# @File    : collegeRecommend.py
# @Software: PyCharm

import numpy as np
import pandas as pd

import os
import xlwt
from pandas.core.frame import DataFrame
from config import db
from dbmodel.predictdata import PredictData

# # Ldata = [515,426,150]
# # Wdata = [538,466,150]
# Linedata = [[74116,160852,268653],
#             [75149,165840,264617],
#             [77749,166864,259573],
#             [81375,171036,260431],
#             [82994,176326,258428]]
# line_list=[272187,269189,260034,260697,258770]#17 18 19 20 21
# lineW_list=[272187,269189,260034,260697,258770]#17 18 19 20 21
college_data = db.session.query(PredictData).order_by(PredictData.RankMin).all()
school_list=[]
banch_list=[]
zslx_list=[]
province_list=[]
type_list=[]
min17_list=[]
min18_list=[]
min19_list=[]
min20_list=[]
min21_list=[]
rankavg_list=[]
rankmin_list=[]
dc_list=[]
ds_list=[]
id_prilist=[]
region_list=[]

for x in college_data:
   school_list.append(x.school_name)
   banch_list.append(x.local_batch_name)
   zslx_list.append(x.zslx_name)
   province_list.append(x.province)
   type_list.append(x.type)
   min17_list.append(x.min_section17)
   min18_list.append(x.min_section18)
   min19_list.append(x.min_section19)
   min20_list.append(x.min_section20)
   min21_list.append(x.min_section21)
   rankavg_list.append(x.RankAvg)
   rankmin_list.append(x.RankMin)
   dc_list.append(x.dc)
   ds_list.append(x.ds)
   id_prilist.append(x.id)
   region_list.append(x.region)
df = pd.concat([DataFrame(school_list),DataFrame(banch_list),
                DataFrame(zslx_list),DataFrame(province_list),
                DataFrame(type_list),DataFrame(min17_list),
                DataFrame(min18_list),DataFrame(min19_list),
                DataFrame(min20_list),DataFrame(min21_list),
                DataFrame(rankavg_list),DataFrame(rankmin_list),
                DataFrame(dc_list),DataFrame(ds_list),DataFrame(id_prilist),
                DataFrame(region_list)],axis=1)
df.columns=['school_name','local_batch_name','zslx_name','province',
            'type','min_section17','min_section18','min_section19','min_section20',
            'min_section21','RankAvg','RankMin','dc','ds','id','region']
# print(df)
# print(global_list)
def select50(rank):
    cont=0
    # df1 = DataFrame()
    id_list=[]
    # df = pd.concat([school_list,banch_list,zslx_list,province_list,type_list,min17_list,min18_list,min19_list,min20_list,min21_list,rankavg_list,rankmin_list,dc_list,ds_list])
    # df = pd.read_excel(r'C:\Users\61X\MyUniverse\SourceCode\PythonProjects\practice\intelligent-recommendations-system-of-college-choosing\compute\data\predict\djj.xlsx')
    for i in range(0,2027):
        if df['RankMin'].at[i]>rank:
            id_list.append(i)
            cont+=1
            if cont >= 50:
                break
    df1 = df.loc[id_list]
    
    
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
    return df1


# rank = int(input("请输入排名："))

# select50(rank)