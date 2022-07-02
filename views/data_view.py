'''
Author: LoftyComet 1277173875@qq.com
Date: 2022-06-24 09:32:58
LastEditors: LoftyComet 1277173875@qq.com
LastEditTime: 2022-07-01 16:59:32
FilePath: \practice\intelligent-recommendations-system-of-college-choosing\views\data_view.py
Description: 

Copyright (c) 2022 by LoftyComet 1277173875@qq.com, All Rights Reserved. 
'''
'''
 ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
 │Esc│   │ F1│ F2│ F3│ F4│ │ F5│ F6│ F7│ F8│ │ F9│F10│F11│F12│ │P/S│S L│P/B│  ┌┐    ┌┐    ┌┐
 └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘  └┘    └┘    └┘
 ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐ ┌───┬───┬───┬───┐
 │~ `│! 1│@ 2│# 3│$ 4│% 5│^ 6│& 7│* 8│( 9│) 0│_ -│+ =│ BacSp │ │Ins│Hom│PUp│ │N L│ / │ * │ - │
 ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤ ├───┼───┼───┼───┤
 │ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │{ [│} ]│ | \ │ │Del│End│PDn│ │ 7 │ 8 │ 9 │   │
 ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┤ └───┴───┴───┘ ├───┼───┼───┤ + │
 │ Caps │ A │ S │ D │ F │ G │ H │ J │ K │ L │: ;│" '│ Enter  │               │ 4 │ 5 │ 6 │   │
 ├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────────┤     ┌───┐     ├───┼───┼───┼───┤
 │ Shift  │ Z │ X │ C │ V │ B │ N │ M │< ,│> .│? /│  Shift   │     │ ↑ │     │ 1 │ 2 │ 3 │   │
 ├─────┬──┴─┬─┴──┬┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐ ├───┴───┼───┤ E││
 │ Ctrl│    │Alt │         Space         │ Alt│    │    │Ctrl│ │ ← │ ↓ │ → │ │   0   │ . │←─┘│
 └─────┴────┴────┴───────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘ └───────┴───┴───┘
'''


"""
本视图专门用于处理ajax数据
"""
import json
from operator import index
import numpy as np
from flask import Blueprint, jsonify, render_template, request
from config import db
from dbmodel.collegeinfo import Collegeinfo
from dbmodel.majorinfo import Majorinfo
from dbmodel.user import User
from dbmodel.divbymajor import DivByMajor
from dbmodel.juniorintro import JuniorIntro
from collegeRecommend import select50
from FractionalQueryPageGlobal import *
data = Blueprint('data', __name__)


@data.route('/getCollegeInfo', methods=['GET', 'POST'])
def get_college_info():
    if request.method == 'POST':  # 判断用户请求是否是post请求

        min_year_id=request.form.get('min_year')
        max_year_id=request.form.get('max_year')

        college_data = []
        iswenke = request.form.get('wenke')
        islike = request.form.get('like')
        print("is理科",islike,"iswenke",iswenke)
        school_name = request.form.get('school')
        major = request.form.get('major')
        region_id= int(request.form.get('region'))
        print("regin_id",type(region_id),region_id)
        if(region_id in pro_id_to_name):
            region_name = pro_id_to_name[region_id]
        else:
            region_name=""
        # regions = ["",
        #            "华东",
        #            "华南",
        #            "华中",
        #            "华北",
        #            "西南",
        #            "西北",
        #            "东北"]
        # region_name = regions[int(region_name)]
        majors = ["",
                  "机械类",
                  "海洋科学类",
                  "化工与制药类",
                  "计算机类",
                  "统计学类",
                  "海洋工程类",
                  "测绘类",
                  "电气类",
                  "环境科学与工程类",
                  "电子信息类",
                  "经济学类",
                  "食品科学与工程类",
                  "生物科学类",
                  "航空装备类",
                  "护理类",
                  "电子商务",
                  "旅游类",
                  "畜牧业类",
                  "医学技术类",
                  "财务会计类",
                  "汽车制造类",
                  "自动化类",
                  "农业类",
                  "航空运输类",
                  "教育类",
                  "金融学类",
                  "管理科学与工程类",
                  "药学类",
                  "数学类",
                  "材料类",
                  "环境科学与工程类",
                  "能源动力类",
                  "临床医学类",
                  "土木类",
                  "法学类",
                  "哲学类"]
        print(major)
        if major != "":
            major_name = majors[int(major)]
        else:
            major_name = ""
        print(school_name)
        print(major_name)
        print("11111111",region_name)
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
                            DivByMajor.school_name == school_name, DivByMajor.province_name == region_name, DivByMajor.level3_name == major_name, DivByMajor.type_name == type_name).all()
                    else:
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name, DivByMajor.province_name == region_name, DivByMajor.type_name == type_name).all()
                else:
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.province_name == region_name, DivByMajor.level3_name == major_name, DivByMajor.type_name == type_name).all()
                    else:
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.province_name == region_name, DivByMajor.type_name == type_name).all()
            else:
                if (school_name != ""):
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name, DivByMajor.level3_name == major_name, DivByMajor.type_name == type_name).all()
                    else:
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.school_name == school_name, DivByMajor.type_name == type_name).all()
                else:
                    if (major_name != ""):
                        college_data = db.session.query(DivByMajor).filter(
                            DivByMajor.level3_name == major_name, DivByMajor.type_name == type_name).all()
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

        haslike="false"
        haswenke="false"
        if islike:
            haslike="true"
        if iswenke:
            haswenke="true"
        return render_template("services.html",**{"school": school_name,
                                                  "major_id":major,
                                                  "region_id":region_id,
                                                  "collegelast":college_data,
                                                  "min_year_id":min_year_id,
                                                  "max_year_id":max_year_id,
                                                  "haslike":haslike,
                                                  "haswenke":haswenke})


@data.route('/getMajorInfo', methods=['GET', 'POST'])
def get_major_info():
    if request.method == 'POST':  # 判断用户请求是否是post请求
        majors = ["计算机科学与技术", "经济学", "公安管理学", "汉语言文学",
                  "柬埔寨语", "生物技术", "材料科学与工程", "电子信息工程", "None"]
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
        # 处理就业率
        years = ["2019", "2020", "2021"]
        # rates_max = [float(major_data[0].rate_1),float(major_data[0].rate_1),float(major_data[0].rate_1)]
        rate1s = major_data[0].rate_1.split("-")
        rate2s = major_data[0].rate_2.split("-")
        rate3s = major_data[0].rate_3.split("-")
        rates_max = [int(rate1s[0][:-1]), int(rate2s[0][:-1]),
                     int(rate3s[0][:-1])]  # 切片去掉百分号
        rates_min = [int(rate1s[1][:-1]), int(rate2s[1][:-1]),
                     int(rate3s[1][:-1])]

        # 处理学校简介
        college_description = ""
        college_description = college_name + "位于" + \
            college_data[0].address + ",是一所" + college_data[0].school_nature_name + \
            college_data[0].type_name + college_data[0].school_type_name
        if college_data[0].f985 == 1:
            college_description = college_description + ",是一所985高校"
        if college_data[0].f211 == 1:
            college_description = college_description + ",是一所211高校。"

        # 处理毕业去向
        detail_pos_0 = major_data[0].detail_pos_1
        job_rate_0 = major_data[0].job_rate_1
        detail_pos_1 = major_data[0].detail_pos_2
        job_rate_1 = major_data[0].job_rate_2
        detail_pos_2 = major_data[0].detail_pos_3
        job_rate_2 = major_data[0].job_rate_3
        detail_pos_3 = major_data[0].detail_pos_4
        job_rate_3 = major_data[0].job_rate_4
        detail_pos_4 = major_data[0].detail_pos_5
        job_rate_4 = major_data[0].job_rate_5
        detail_pos_5 = major_data[0].detail_pos_6
        job_rate_5 = major_data[0].job_rate_6
        datas = []
        temp1 = {}
        temp2 = {}
        temp3 = {}
        temp4 = {}
        temp5 = {}
        temp6 = {}
        temp1["name"] = detail_pos_0
        temp1["value"] = job_rate_0
        datas.append(temp1)
        temp2["name"] = detail_pos_1
        temp2["value"] = job_rate_1
        datas.append(temp2)
        temp3["name"] = detail_pos_2
        temp3["value"] = job_rate_2
        datas.append(temp3)
        temp4["name"] = detail_pos_3
        temp4["value"] = job_rate_3
        datas.append(temp4)
        temp5["name"] = detail_pos_4
        temp5["value"] = job_rate_4
        datas.append(temp5)
        temp6["name"] = detail_pos_5
        temp6["value"] = job_rate_5
        datas.append(temp6)

        jsonlist["years"] = years
        jsonlist["rates_min"] = rates_min
        jsonlist["rates_max"] = rates_max
        jsonlist["college_name"] = college_name
        jsonlist["major_name"] = major_name
        jsonlist["description"] = major_data[0].description
        jsonlist["address"] = college_description
        jsonlist["datas"] = datas
    return jsonify(json.dumps(jsonlist, ensure_ascii=False))


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
        region = request.form.get('region')
        regions = ["",
                   "华东",
                   "华南",
                   "华中",
                   "华北",
                   "西南",
                   "西北",
                   "东北"]
        region = regions[int(region)]
        kind_name = int(request.form.get('kind_name'))
        score = int(request.form.get('score'))
        print("score", score)
        # 通过一分一段表计算出2022年四川省排名
        rank = int(db.session.query(JuniorIntro).filter(
            JuniorIntro.score == score, JuniorIntro.lw == kind_name).all()[0].total)
        # 以下根据排名计算出推荐学校
        df1 = select50(rank, kind_name)
        # print(df1["school_name"])
        print("------------------")
        schools1 = np.array(df1["school_name"]).tolist()[::-1]
        predicted1 = np.array(df1["predict"]).tolist()[::-1]
        regions1 = np.array(df1["region"]).tolist()[::-1]
        regions = []
        schools = []
        predicted = []
        # 根据意向地区筛选学校
        if region != "":
            for i in range(len(regions1)):
                if regions1[i] == region:
                    regions.append(regions1[i])
                    schools.append(schools1[i])
                    predicted.append(predicted1[i])
        else:
            regions = regions1
            schools = schools1
            predicted = predicted1

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
        print(rush)
        attempt = attempt[:3]
        print(attempt)
        safe = safe[:3]
        print(safe)
        # selected = rush + attempt + safe
        # 根据推荐的学校名字调取专业信息,其中专业最低排名大于用户排名
        rush_majors = []
        attempt_majors = []
        safe_majors = []
        for college in rush:
            rush_majors = rush_majors + db.session.query(DivByMajor).filter(
                DivByMajor.school_name == college, DivByMajor.min_section > rank, DivByMajor.min_section - rank < 2000).all()
        for college in attempt:
            attempt_majors = attempt_majors + db.session.query(DivByMajor).filter(
                DivByMajor.school_name == college, DivByMajor.min_section > rank, DivByMajor.min_section - rank < 3500).all()
        for college in safe:
            safe_majors = safe_majors + db.session.query(DivByMajor).filter(
                DivByMajor.school_name == college, DivByMajor.min_section > rank, DivByMajor.min_section - rank < 5000).all()

    return render_template("test.html", rush=rush_majors, attempt=attempt_majors, safe=safe_majors)
