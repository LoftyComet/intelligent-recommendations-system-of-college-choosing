import email
from config import db

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True) #
    username = db.Column(db.String(50)) #用户姓名
    gender = db.Column(db.String(50)) #性别
    household_registration = db.Column(db.String(50)) #户籍信息
    email = db.Column(db.String(50)) #邮箱