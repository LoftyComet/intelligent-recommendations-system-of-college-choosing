from config import db

class EnrollmentPlan(db.Model):
    __tablename__ = "enrollment_plan"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(50)) #分科类型
    school_name = db.Column(db.String(50)) #学校名称   
    province = db.Column(db.String(50)) #省市
    num = db.Column(db.Integer) #招生数量
    spname = db.Column(db.String(50)) #专业名称