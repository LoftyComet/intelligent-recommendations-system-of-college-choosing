from config import db

class DivById(db.Model):
    __tablename__ = "div_by_id"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    school_name = db.Column(db.String(50)) #学校名称
    type_name = db.Column(db.String(50)) #分科类型
    province = db.Column(db.String(50)) #省市
    min1 = db.Column(db.Integer) #最低分
    max1 = db.Column(db.Integer) #最高分
    min_section = db.Column(db.Integer) #全省排名
    level1_name = db.Column(db.String(50)) #专业分级1
    level2_name = db.Column(db.String(50)) #专业分级2
    level3_name = db.Column(db.String(50)) #专业分级3
    spname = db.Column(db.String(50)) #专业名称
    local_batch_name = db.Column(db.String(50)) #招生批次