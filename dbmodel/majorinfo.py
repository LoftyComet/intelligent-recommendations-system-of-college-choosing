from config import db

class Majorinfo(db.Model):
    __tablename__ = "majorinfo"
    m_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    limit_year = db.Column(db.String(50))  #就读年份
    degree = db.Column(db.String(50)) #毕业学位名称
    name = db.Column(db.String(50)) #专业名称
    description = db.Column(db.String(50)) #专业介绍
    sel_adv = db.Column(db.String(50)) # 选择模式  3+3省份：不限&#13;&#10;3+1+2省份：首选不限，再选政治/化学/地理/生物
    year_1 = db.Column(db.Integer) #年份1
    rate_1 = db.Column(db.String(50)) #就业率1
    year_2 = db.Column(db.Integer) #年份2
    rate_2 = db.Column(db.String(50)) #就业率2
    year_3 = db.Column(db.Integer) #年份3
    rate_3 = db.Column(db.String(50)) #就业率3
    detail_pos_1 = db.Column(db.String(50)) #就业方向1
    job_rate_1 = db.Column(db.Float) #就业比例1
    detail_pos_2 = db.Column(db.String(50)) #就业方向2
    job_rate_2 = db.Column(db.Float) #就业比例2
    detail_pos_3 = db.Column(db.String(50)) #就业方向3
    job_rate_3 = db.Column(db.Float) #就业比例3
    detail_pos_4 = db.Column(db.String(50)) #就业方向4
    job_rate_4 = db.Column(db.Float) #就业比例4
    detail_pos_5 = db.Column(db.String(50)) #就业方向5
    job_rate_5 = db.Column(db.Float) #就业比例5
    detail_pos_6 = db.Column(db.String(50)) #就业方向6
    job_rate_6 = db.Column(db.Float) #就业比例6