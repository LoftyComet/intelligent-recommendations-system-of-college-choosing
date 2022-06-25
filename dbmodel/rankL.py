from config import db

class RankL(db.Model):
    __tablename__ = "score_dataL"
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    school_name = db.Column(db.String(50)) #专业名称
    local_batch_name = db.Column(db.String(50)) #录取批次
    zslx_name = db.Column(db.String(50)) #录取类型 eg. 中外合作办学
    province = db.Column(db.String(50)) #生源地
    subject_type = db.Column(db.String(50)) #文理科
    RankAvg = db.Column(db.Float) #平均排名
    RankMin = db.Column(db.Integer) #最小排名
    RankMax = db.Column(db.Integer) #最大排名
    ScoreAvg = db.Column(db.Float) #历年超过一本线平均分
    ScoreMin = db.Column(db.Integer) 
    ScoreMax = db.Column(db.Integer) 