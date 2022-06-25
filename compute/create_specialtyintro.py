# -*- codeing = utf-8 -*-
# @Time :2022/6/23 15:40
# @Author:Voyage
# @File : create_specialtyintro.py
# @Software: PyCharm
#创建学科专业数据库

import os

import MysqlConfig
from pyspark import Row
from pyspark.sql import SparkSession
import pandas as pd
os.environ["PYSPARK_PYTHON"] = r"C:\Users\61X\miniconda3\envs\py36\python.exe"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

#数据预处理

#本科专业
df = pd.read_excel(r"C:\Users\61X\MyUniverse\SourceCode\PythonProjects\practice\intelligent-recommendations-system-of-college-choosing\compute\data\specialdata\本科专业数据.xlsx")
col = ['year_1','year_2','year_3','job_rate_1','job_rate_2','job_rate_3','job_rate_4','job_rate_5','job_rate_6']

df[col] = df[col].fillna(0)
df = df.replace(pd.NA,'')#空值替换
# df = df.fillna(0)
# df = df.replace(pd.NA,'')#空值替换
df= df.astype(dtype={'year_1':'int','year_2':'int','year_3':'int','job_rate_1':'float','job_rate_2':'float','job_rate_3':'float','job_rate_4':'float','job_rate_5':'float','job_rate_6':'float'})


df_spark_excel = spark.createDataFrame(df)  # 转换为spark格式
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
# df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'junior_intro', 'overwrite', conn_param)
df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'majorinfo', 'overwrite', conn_param)
print("执行完毕")
