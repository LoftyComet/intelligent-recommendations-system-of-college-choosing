import email
from itertools import count
import json

from flask import Blueprint, jsonify, render_template, request

from config import db

from dbmodel.collegeinfo import Collegeinfo
from dbmodel.majorinfo import Majorinfo
from dbmodel.user import User

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
    return render_template("index.html",collegelast=college_data,majorlast=major_data)

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


    