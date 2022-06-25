from itertools import count
import json

from flask import Blueprint, jsonify, render_template, request

from config import db

from dbmodel.collegeinfo import Collegeinfo

"""
本视图专门用于处理ajax数据
"""
data = Blueprint('data', __name__)

@data.route('/getCollegeInfo', methods=['GET','POST'])
def get_college_info():
    if request.method == 'POST': # 判断用户请求是否是post请求
        school_name=request.form.get('school') #
        print(school_name)
        print("---------------------------")
        data = db.session.query(Collegeinfo).filter(Collegeinfo.school_name==school_name).all()
        
        print(data[0].school_name)
        print("---------------------------")
        # view_data = {}
        # view_data["series"] = []

        # def build_view_data(item):
        #     dic = {}
        #     dic["value"] = item.count
        #     dic["name"] = item.city
        #     view_data["series"].append([dic])

        # [build_view_data(item) for item in data]

        # return json.dumps(view_data, ensure_ascii=False)
    return render_template("services.html",collegelast=data)