from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ToDo(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(128), )
    date_time = db.Column(db.DateTime)
    details = db.Column(db.String(256))