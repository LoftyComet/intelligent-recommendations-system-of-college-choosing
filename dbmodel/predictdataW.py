from config import db

class PredictDataW(db.Model):
    __tablename__ = "predict_data_W"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school_name = db.Column(db.String(50)) #学校名称
    local_batch_name = db.Column(db.String(50))  # 录取批次
    zslx_name = db.Column(db.String(50))  # 录取类型
    province = db.Column(db.String(50))
    type = db.Column(db.String(50)) #文理分科
    min_section17 = db.Column(db.Integer)
    min_section18 = db.Column(db.Integer)
    min_section19 = db.Column(db.Integer)
    min_section20 = db.Column(db.Integer)
    min_section21 = db.Column(db.Integer)
    RankAvg = db.Column(db.Float)
    RankMin = db.Column(db.Integer)
    dc = db.Column(db.Float)
    ds = db.Column(db.Float)
    region = db.Column(db.String(50)) #所在地区