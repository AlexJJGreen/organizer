
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True)
    username = db.Column(db.String(256), index=True, unique=True)
    email = db.Column(db.String(256), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    age = db.Column(db.Integer)
    about_me = db.Column(db.String(256), index=True)

    def __repr__(self):
        return "<User_id {} : Username {}>".format(self.id, self.username)
