# -*- codeing = utf-8 -*-
# @Time :2022/6/24 10:07
# @Author:Voyage
# @File : create_schoolid.py
# @Software: PyCharm
#学校与编号链接表
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
df = pd.read_excel("E:\\360MoveData\\Users\lenovo\Desktop\scoredata\specialdata\高校编号.xlsx")
df= df.astype(dtype={'sid':'int'})
df = df.replace(pd.NA,'')#空值替换
df_spark_excel = spark.createDataFrame(df)  # 转换为spark格式
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'school_id', 'overwrite', conn_param)
print("执行完毕")