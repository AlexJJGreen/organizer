
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app as app
from app import login

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True)
    username = db.Column(db.String(256), index=True, unique=True)
    email = db.Column(db.String(256), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    age = db.Column(db.Integer)
    about_me = db.Column(db.String(256), index=True)
    group_member = db.relationship("GroupMembers", backref="group_member", lazy="dynamic")

    def __repr__(self):
        return "<User_id {} : Username {}>".format(self.id, self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(256), index=True, unique=True)
    group_members = db.relationship("GroupMembers", backref="group", lazy="dynamic")

class GroupMembers(db.Model):
    # 
    __table_args__ = (db.PrimaryKeyConstraint("group_id", "member_id"),)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))
