from config import db

class Id2college(db.Model):
    __tablename__ = "school_id"
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    name = db.Column(db.String(50)) #学校名称