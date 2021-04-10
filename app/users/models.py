
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app as app
from app import login

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), index=True, unique=True)
    email = db.Column(db.String(256), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    groups = db.relationship("GroupMembers", backref="user", lazy="dynamic")
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserProfile(db.Model):
    user_id = db.Column(db.ForeignKey("user.id"), primary_key=True)
    name = db.Column(db.String(256), index=True)
    age = db.Column(db.Integer)
    about_me = db.Column(db.String(256), index=True)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
