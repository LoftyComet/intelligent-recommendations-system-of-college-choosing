from itertools import count
import json

from flask import Blueprint, jsonify, request

from config import db

from dbmodel.collegeinfo import Collegeinfo

"""
本视图专门用于处理ajax数据
"""
data = Blueprint('data', __name__)

@data.route('/getCollegeInfo', methods=['GET'])
def get_college_info():
    print("---------------------------")
    data = db.session.query(Collegeinfo).filter(Collegeinfo.shool_name==18).all()
    print("---------------------------")
    print(data)
    view_data = {}
    view_data["series"] = []

    def build_view_data(item):
        dic = {}
        dic["value"] = item.count
        dic["name"] = item.city
        view_data["series"].append([dic])

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)