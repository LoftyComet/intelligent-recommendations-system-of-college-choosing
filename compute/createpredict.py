# -*- codeing = utf-8 -*-
# @Time :2022/6/27 17:19
# @Author:Voyage&恋秋轩
# @File : createpredict.py
# @Software: PyCharm

#将所求数据经过计算存入数据库
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
#理科
df = pd.read_excel(r"C:\Users\61X\MyUniverse\SourceCode\PythonProjects\practice\intelligent-recommendations-system-of-college-choosing\compute\data\predict\rankL_region.xlsx")
#文科
# df = pd.read_excel(r"C:\Users\61X\MyUniverse\SourceCode\PythonProjects\practice\intelligent-recommendations-system-of-college-choosing\compute\data\predict\rankW_region.xlsx")
col = ['min_section17','min_section18','min_section19','min_section20','min_section21','dc','ds']



df_spark_excel = spark.createDataFrame(df)  # 转换为spark格式
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
df_spark_excel.write.jdbc(MysqlConfig.MYSQL_CONN, 'predict_data', 'overwrite', conn_param)##第一次用下面的iverwrite之后用append
print("执行完毕")
