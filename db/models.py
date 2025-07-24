from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    transport = db.Column(db.String(20))
    energy = db.Column(db.String(20))
    diet = db.Column(db.String(20))
    score = db.Column(db.Integer)
    tip = db.Column(db.String(255))
    ecoluck = db.Column(db.String(255))
