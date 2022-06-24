# -*- codeing = utf-8 -*-
# @Time :2022/6/23 9:39
# @Author:Voyage
# @File : schooldata.py
# @Software: PyCharm

from config import db
#学校数据数据表
#school_name	address	dual_class_name	school_site	f985	f211	school_type_name	type_name	province_name	city_name	town_name	school_nature_name

class EveryRegionsErshoufangCount(db.Model):
    __tablename__ = "school_intro"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #id
    school_name = db.Column(db.String(50)) #学校名称
    address = db.Column(db.String(50))  # 具体地址
    dual_class_name = db.Column(db.String(50))  # 双一流标签
    school_site = db.Column(db.String(50)) #学校网址
    f985 = db.Column(db.String(50))  #985
    f211 = db.Column(db.String(50))  #211
    school_type_name = db.Column(db.String(50)) #学校类型
    type_name  = db.Column(db.String(50)) #具体类型类型
    province_name = db.Column(db.String(50)) #省市
    city_name = db.Column(db.String(50)) #二级省市
    town_name = db.Column(db.String(50)) #区域
    school_nature_name = db.Column(db.String(50)) #民办/公办
