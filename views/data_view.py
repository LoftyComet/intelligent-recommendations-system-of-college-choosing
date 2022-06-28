import email
from itertools import count
import json

from flask import Blueprint, jsonify, render_template, request

from config import db

from dbmodel.collegeinfo import Collegeinfo
from dbmodel.majorinfo import Majorinfo
from dbmodel.user import User
from collegeRecommend import select50

"""
本视图专门用于处理ajax数据
"""
data = Blueprint('data', __name__)

@data.route('/getCollegeInfo', methods=['GET','POST'])
def get_college_info():
    if request.method == 'POST': # 判断用户请求是否是post请求
        college_data = []
        school_name=request.form.get('school') #
        print(school_name)
        print("---------------------------")
        college_data = db.session.query(Collegeinfo).filter(Collegeinfo.school_name==school_name).all()        
        for x in college_data:
            print("查询到的学校有：",x.school_name)
        print("---------------------------")
    return render_template("services.html",collegelast=college_data)
    # return render_template("services.html")

@data.route('/getMajorInfo', methods=['GET','POST'])
def get_major_info():
    if request.method == 'POST': # 判断用户请求是否是post请求
        

        majors = ["计算机科学与技术","新闻","金融","医学","数学","建筑","土木","机械","None"]
        major=request.form.get('major')
        print(major)
        college_name=request.form.get('college')
        major_name = majors[int(major)-1]
        print("college_name:",college_name)
        print(major_name)
        print("---------------------------")
        major_data = db.session.query(Majorinfo).filter(Majorinfo.name==major_name).all()        
        for x in major_data:
            print("查询到的专业有：",x.name)

        college_data = db.session.query(Collegeinfo).filter(Collegeinfo.school_name==college_name).all()        
        for x in college_data:
            print("查询到的学校有：",x.school_name)
        print("---------------------------")
        jsonlist = {}
        # # 处理就业率
        years = ["2019","2020","2021"]
        # rates_max = [float(major_data[0].rate_1),float(major_data[0].rate_1),float(major_data[0].rate_1)]
        rate1s = major_data[0].rate_1.split("-")
        rate2s = major_data[0].rate_2.split("-")
        rate3s = major_data[0].rate_3.split("-")
        rates_max = [int(rate1s[0][:-1]),int(rate2s[0][:-1]),int(rate3s[0][:-1])] #切片去掉百分号
        rates_min = [int(rate1s[1][:-1]),int(rate2s[1][:-1]),int(rate3s[1][:-1])]

        # # 添加年份就业率字典方便转换为json
        # for i in range(len(years)):
        #     ratesjson.update(years[i],rates[i])
        jsonlist["years"]=years
        jsonlist["rates_min"]=rates_min
        jsonlist["rates_max"]=rates_max
        jsonlist["college_name"]=college_name
        jsonlist["major_name"]=major_name
        jsonlist["description"]=major_data[0].description
        jsonlist["address"]=college_data[0].address
    return jsonify(json.dumps(jsonlist, ensure_ascii=False))
    # return render_template("index.html",collegelast=college_data,majorlast=major_data,years=years,rates=rates))

@data.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # 从前端获取数据
        username=request.form.get('username') 
        gender=request.form.get('gender') 
        household_registration=request.form.get('household_registration') 
        email=request.form.get('email') 
        # 创建对象
        user = User(username=username, gender=gender, household_registration=household_registration, email=email)
        # session记录对象任务
        db.session.add(user)
        # 提交任务到数据库
        db.session.commit()
    # 暂时先回到主页
    return render_template("index.html")

@data.route('/getPrediction', methods=['GET','POST'])
def get_prediction():
    if request.method == 'POST': # 判断用户请求是否是post请求
        provinces = ["山东","安徽","四川"]        
        province=provinces[request.form.get('province')]
        kind_names = ["综合","文科","理科"]        
        kind_name=kind_names[request.form.get('kind_name')]
        rank = request.form.get('rank')
        # 以下根据排名计算出推荐学校
        df1 = select50(rank=rank)
        
        jsonlist = {}
    return jsonify(json.dumps(jsonlist, ensure_ascii=False))

    