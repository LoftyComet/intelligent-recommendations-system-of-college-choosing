# -*- codeing = utf-8 -*-
# @Time :2022/6/27 9:46
# @Author:Voyage
# @File : creatstudentnum.py
# @Software: PyCharm
# 将招生计划写入数据库、
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
# sc = spark.sparkContext

#将文件上传
df = pd.read_excel(r"C:\Users\61X\MyUniverse\SourceCode\PythonProjects\practice\intelligent-recommendations-system-of-college-choosing\compute\data\EnrollmentPlan\2021四川理科高校招生计划数据.xlsx")
df["year"]=2021 #pandas新增一列，加在最后
col = ['num']
df[col] = df[col].fillna(0.0)
df = df.replace(pd.NA,'')#空值替换
df = df.replace('-',0)#空值替换
# df = df.fillna(0)
# df = df.replace(pd.NA,'')#空值替换
df= df.astype(dtype={'num':'int'})


df_spark_excel = spark.createDataFrame(df)  # 转换为spark格式
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'enrollment_plan', 'append', conn_param)##第一次用下面的iverwrite之后用append
# df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'enrollment_plan', 'overwrite', conn_param)
print("执行完毕")