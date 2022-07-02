'''
Author: LoftyComet 1277173875@qq.com
Date: 2022-06-24 09:33:22
LastEditors: LoftyComet 1277173875@qq.com
LastEditTime: 2022-07-01 11:02:53
FilePath: \practice\intelligent-recommendations-system-of-college-choosing\views\page_view.py
Description: 

Copyright (c) 2022 by LoftyComet 1277173875@qq.com, All Rights Reserved. 
'''


# -*- coding:utf-8 -*-
from flask import Blueprint, render_template

"""
本视图专门用于处理页面
"""
page = Blueprint('page', __name__)



@page.route('/')
def index():
    return render_template("index.html")

@page.route('/index')
def home():
    return index()

# @page.route('/getMajorInfo')
# def major():
#     return index()

@page.route('/about')
def about():
    return render_template("about.html")

@page.route('/load')
def load():
    return render_template("load.html")

@page.route('/predict')
def predict():
    return render_template("predict.html")

@page.route('/team')
def pricing():
    return render_template("team.html")

@page.route('/services')
def services():
    return render_template("services.html",**{"school": "",
                                              "major_id":"0",
                                              "region_id":"0",
                                              "min_year_id":"2019",
                                              "max_year_id":"2021",
                                              "haslike":"true",
                                              "haswenke":"true"})

@page.route('/test')
def test():
    return render_template("test.html")

@page.route('/baidu')
def baidu():
    return render_template("baidu.html")

@page.route('/yuce')
def yuce():
    return render_template("yuce.html")

@page.route('/tuijian')
def tuijian():
    return render_template("tuijian.html")