import email
from itertools import count
import json
import numpy as np
from flask import Blueprint, jsonify, render_template, request

from config import db

from dbmodel.collegeinfo import Collegeinfo
from dbmodel.majorinfo import Majorinfo
from dbmodel.user import User
from dbmodel.divbymajor import DivByMajor
from dbmodel.juniorintro import JuniorIntro
from collegeRecommend import select50

"""
本视图专门用于处理ajax数据
"""
data = Blueprint('data', __name__)


@data.route('/getCollegeInfo', methods=['GET', 'POST'])
def get_college_info():
    if request.method == 'POST':  # 判断用户请求是否是post请求
        college_data = []
        iswenke = request.form.get('wenke')
        islike = request.form.get('like')
        school_name = request.form.get('school')
        major = request.form.get('major')
        region_name = request.form.get('region')
        majors = ["",
                  "机械类",
                  "海洋科学类",
                  "化工与制药类",
                  "计算机类",
                  "统计学类",
                  "海洋工程类",
                  "测绘类",
                  "电气类",
                  "环境科学与工程类"]
        print(major)
        if major != "":
            major_name = majors[int(major)]
        else:
            major_name = ""
        print(school_name)
        print(major_name)
        print(region_name)
        #!此段代码为三流程序员所写
        # 子查询文理科
        if (islike and not iswenke) or (not islike and iswenke):
            if islike and not iswenke:
                type_name = "理科"
            else:
                type_name = "文科"
            
            if (region_name != ""):
                if (school_name != ""):
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name, DivByMajor.province_name == region_name, DivByMajor.level3_name == major_name,DivByMajor.type_name==type_name).all()
                    else:
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name, DivByMajor.province_name == region_name,DivByMajor.type_name==type_name).all()
                else:
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.province_name == region_name, DivByMajor.level3_name == major_name,DivByMajor.type_name==type_name).all()
                    else:
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.province_name == region_name,DivByMajor.type_name==type_name).all()
            else:
                if (school_name != ""):
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name, DivByMajor.level3_name == major_name,DivByMajor.type_name==type_name).all()
                    else:
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name,DivByMajor.type_name==type_name).all()
                else:
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.level3_name == major_name,DivByMajor.type_name==type_name).all()
                    else:
                        college_data = []
        else:
            if (region_name != ""):
                if (school_name != ""):
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name, DivByMajor.province_name == region_name, DivByMajor.level3_name == major_name).all()
                    else:
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name, DivByMajor.province_name == region_name).all()
                else:
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.province_name == region_name, DivByMajor.level3_name == major_name).all()
                    else:
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.province_name == region_name).all()
            else:
                if (school_name != ""):
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name, DivByMajor.level3_name == major_name).all()
                    else:
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name).all()
                else:
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.level3_name == major_name).all()
                    else:
                        college_data = []
        



        for x in college_data:
            print("查询到的学校有：", x.school_name)
        print("---------------------------")
    return render_template("services.html", collegelast=college_data)


@data.route('/getMajorInfo', methods=['GET', 'POST'])
def get_major_info():
    if request.method == 'POST':  # 判断用户请求是否是post请求

        majors = ["计算机科学与技术", "新闻", "金融", "医学", "数学", "建筑", "土木", "机械", "None"]
        major = request.form.get('major')
        print(major)
        college_name = request.form.get('college')
        major_name = majors[int(major)-1]
        print("college_name:", college_name)
        print(major_name)
        print("---------------------------")
        major_data = db.session.query(Majorinfo).filter(
            Majorinfo.name == major_name).all()
        for x in major_data:
            print("查询到的专业有：", x.name)

        college_data = db.session.query(Collegeinfo).filter(
            Collegeinfo.school_name == college_name).all()
        for x in college_data:
            print("查询到的学校有：", x.school_name)
        print("---------------------------")
        jsonlist = {}
        # # 处理就业率
        years = ["2019", "2020", "2021"]
        # rates_max = [float(major_data[0].rate_1),float(major_data[0].rate_1),float(major_data[0].rate_1)]
        rate1s = major_data[0].rate_1.split("-")
        rate2s = major_data[0].rate_2.split("-")
        rate3s = major_data[0].rate_3.split("-")
        rates_max = [int(rate1s[0][:-1]), int(rate2s[0][:-1]),
                     int(rate3s[0][:-1])]  # 切片去掉百分号
        rates_min = [int(rate1s[1][:-1]), int(rate2s[1][:-1]),
                     int(rate3s[1][:-1])]

        # # 添加年份就业率字典方便转换为json
        # for i in range(len(years)):
        #     ratesjson.update(years[i],rates[i])
        jsonlist["years"] = years
        jsonlist["rates_min"] = rates_min
        jsonlist["rates_max"] = rates_max
        jsonlist["college_name"] = college_name
        jsonlist["major_name"] = major_name
        jsonlist["description"] = major_data[0].description
        jsonlist["address"] = college_data[0].address
    return jsonify(json.dumps(jsonlist, ensure_ascii=False))
    # return render_template("index.html",collegelast=college_data,majorlast=major_data,years=years,rates=rates))


@data.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 从前端获取数据
        username = request.form.get('username')
        gender = request.form.get('gender')
        household_registration = request.form.get('household_registration')
        email = request.form.get('email')
        # 创建对象
        user = User(username=username, gender=gender,
                    household_registration=household_registration, email=email)
        # session记录对象任务
        db.session.add(user)
        # 提交任务到数据库
        db.session.commit()
    # 暂时先回到主页
    return render_template("index.html")


@data.route('/getPrediction', methods=['GET', 'POST'])
def get_prediction():
    if request.method == 'POST':  # 判断用户请求是否是post请求

        kind_name = int(request.form.get('kind_name'))
        score = int(request.form.get('score'))
        # 通过一分一段表计算出2022年四川省排名
        rank = int(db.session.query(JuniorIntro).filter(
            JuniorIntro.score == score, JuniorIntro.lw == kind_name).all()[0])
        # 以下根据排名计算出推荐学校
        df1 = select50(rank, kind_name)
        # print(df1["school_name"])
        print("------------------")
        schools = np.array(df1["school_name"]).tolist()
        predicted = np.array(df1["predict"]).tolist()
        # 根据0.6 0.8 划分稳 冲 保
        rush = []  # 冲吖~
        attempt = []  # 稳一稳
        safe = []  # 摆烂
        for i in range(len(predicted)):
            if float(predicted[i]) < 0.6:
                rush.append(schools[i])
            elif float(predicted[i]) > 0.6 and float(predicted[i]) < 0.8:
                attempt.append(schools[i])
            else:
                safe.append(schools[i])
        # 选出前三甲
        rush = rush[:3]
        attempt = attempt[:3]
        safe = safe[:3]
        selected = rush + attempt + safe
        # 根据推荐的学校名字调取专业信息,其中专业最低排名大于用户排名
        for college in selected:
            majors = db.session.query(DivByMajor).filter(
                DivByMajor.school_name == college, DivByMajor.min_section > rank).all()

    return render_template("predict.html", predictlist=schools)
