from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(256), index=True, unique=True)
    group_members = db.relationship("GroupMembers", backref="group", lazy="dynamic")

class GroupMembers(db.Model):
    # 
    __table_args__ = (db.PrimaryKeyConstraint("group_id", "member_id"),)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))

