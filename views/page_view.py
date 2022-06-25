# -*- coding:utf-8 -*-
from flask import Blueprint, render_template

"""
本视图专门用于处理页面
"""
page = Blueprint('page', __name__)


# @page.route('/', endpoint="index")
# def login():
#     return render_template("index.html")


@page.route('/')
def index():
    return render_template("index.html")

@page.route('/index')
def home():
    return index()
@page.route('/about')
def about():
    return render_template("about.html")

@page.route('/load')
def load():
    return render_template("load.html")

@page.route('/predict')
def predict():
    return render_template("predict.html")

@page.route('/pricing')
def pricing():
    return render_template("pricing.html")

@page.route('/services')
def services():
    return render_template("services.html")

@page.route('/test')
def test():
    return render_template("test.html")