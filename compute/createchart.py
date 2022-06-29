# -*- codeing = utf-8 -*-
# @Time :2022/6/29 15:09
# @Author:Voyage
# @File : createchart.py
# @Software: PyCharm

#一分一段表写入数据库
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

#使用上传的最新数据（不需要类型转换）
df = pd.read_excel(r"C:\Users\61X\MyUniverse\SourceCode\PythonProjects\practice\intelligent-recommendations-system-of-college-choosing\compute\data\predict\2022四川文科一分一段表数据.xlsx")
# df = df.replace(pd.NA,'')#空值替换
# df = df.fillna(0)
# df = df.replace(pd.NA,'')#空值替换
df= df.astype(dtype={'score':'int','num':'int','total':'int','id':'float','lw':'int'})


df_spark_excel = spark.createDataFrame(df)  # 转换为spark格式
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
# df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'junior_intro', 'overwrite', conn_param)
df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'junior_intro', 'append', conn_param)
print("执行完毕")
