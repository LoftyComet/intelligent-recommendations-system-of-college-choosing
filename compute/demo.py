import os

import MysqlConfig
from pyspark import Row
from compute import MysqlConfig
from pyspark import Row
from pyspark.sql import SparkSession
import pandas as pd
## 路径改为本地py
os.environ["PYSPARK_PYTHON"] = r"C:\Users\61X\miniconda3\envs\py36\python.exe"
# 华北地区
# from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
sc = spark.sparkContext

## 记得改文件路径 ##
#本机文件地址
df = pd.read_excel("E:\\360MoveData\\Users\lenovo\Desktop\scoredata\specialdata\全国高校数据.xlsx")
df= df.astype(dtype={'f985':'int','f211':'int'}) #数据类型转换
df = df.replace(pd.NA,'')#空值替换
df_spark_excel = spark.createDataFrame(df)  #panda转化成spark

## --------- spark数据分析 --------- ##




## ---------    分析结束   --------- ##

# schema_demo = spark.createDataFrame(pair_rdd)
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER

df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'test', 'overwrite', conn_param)
print("执行完毕")