from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, optional, length


class CreateForm(FlaskForm):
    task_name = StringField("Task", validators=[DataRequired()])
    date_time = DateTimeLocalField("Date & Time", validators=[DataRequired()])
    details = TextAreaField("Details", validators=[optional(), length(max=200)])
    create = SubmitField("Create")
