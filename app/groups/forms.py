from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, length

class CreateGroupForm(FlaskForm):
    group_name = StringField("Group Name", validators=[DataRequired(), length(max=256)])
    group_members = SelectMultipleField("Group Members")
    submit = SubmitField("Start Group")


    # MAPPED FROM MODEL ------
    # class Group(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # group_name = db.Column(db.String(256), index=True, unique=True)
    # group_members = db.relationship("GroupMembers", backref="group", lazy="dynamic")