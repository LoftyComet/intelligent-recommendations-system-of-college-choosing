# -*- codeing = utf-8 -*-
# @Time :2022/6/29 15:09
# @Author:Voyage
# @File : createchart.py
# @Software: PyCharm

#一分一段表写入数据库
import os

from compute import MysqlConfig
from pyspark import Row
from pyspark.sql import SparkSession
import pandas as pd
os.environ["PYSPARK_PYTHON"] = r"D:\anaconda\envs\douban3.6\python.exe"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

#数据预处理

#使用上传的最新数据（不需要类型转换）
df = pd.read_excel("E:\\360MoveData\\Users\lenovo\Desktop\scoredata\\2022四川理科一分一段表数据.xlsx")
df = df.replace(pd.NA,'')#空值替换
# df = df.fillna(0)
# df = df.replace(pd.NA,'')#空值替换
# df= df.astype(dtype={'year_1':'int','year_2':'int','year_3':'int','job_rate_1':'float','job_rate_2':'float','job_rate_3':'float','job_rate_4':'float','job_rate_5':'float','job_rate_6':'float'})


df_spark_excel = spark.createDataFrame(df)  # 转换为spark格式
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
# df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'junior_intro', 'overwrite', conn_param)
df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'data', 'append', conn_param)
print("执行完毕")
