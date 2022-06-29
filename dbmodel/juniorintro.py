from config import db

class JuniorIntro(db.Model):
    __tablename__ = "junior_intro"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    score = db.Column(db.Integer) # 分数
    num = db.Column(db.Integer) # 当前分数同分人数
    total = db.Column(db.Integer) # 总排名
    lw = db.Column(db.Integer) # 文理分科 1->理科 0->文科