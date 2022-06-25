# -*- codeing = utf-8 -*-
# @Time :2022/6/25 11:02
# @Author:Voyage
# @File : create_scoredata.py
# @Software: PyCharm
#将分析数据存入数据库
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

df = pd.read_excel(r"C:\Users\61X\MyUniverse\SourceCode\PythonProjects\practice\intelligent-recommendations-system-of-college-choosing\compute\data\specialdata\rankL.xlsx")
# df= df.astype(dtype={'f985':'int','f211':'int'})
# df = df.replace(pd.NA,'')#空值替换
df_spark_excel = spark.createDataFrame(df)  # 转换为spark格式
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'score_dataL', 'overwrite', conn_param)
print("执行完毕")