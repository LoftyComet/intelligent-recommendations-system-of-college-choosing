from config import db

class Collegeinfo(db.Model):
    __tablename__ = "collegeinfo"
    id = db.Column(db.Integer, primary_key=True)
    shool_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    dual_class_name = db.Column(db.String(50))
    school_site = db.Column(db.String(50))
    f985 = db.Column(db.INTEGER)
    f211 = db.Column(db.INTEGER)
    school_type_name = db.Column(db.String(50))
    type_name = db.Column(db.String(50))
    province_name = db.Column(db.String(50))
    city_name = db.Column(db.String(50))
    town_name = db.Column(db.String(50))
    school_nature_name = db.Column(db.String(50))