import os

import MysqlConfig
from pyspark import Row

## 路径改为本地py
os.environ["PYSPARK_PYTHON"] = r"C:\Users\61X\miniconda3\envs\py36\python.exe"
# 华北地区
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
sc = spark.sparkContext

## 记得改文件路径 ##
test_rdd = sc.textFile("hdfs://192.168.88.168:9000/house/ershoufang_price.txt")

## --------- spark数据分析 --------- ##




## ---------    分析结束   --------- ##

schema_demo = spark.createDataFrame(pair_rdd)
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER

schema_demo.write.jdbc(MysqlConfig.MYSQL_CONN, 'test', 'overwrite', conn_param)
print("执行完毕")