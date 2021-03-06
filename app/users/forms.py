from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.fields.html5 import DecimalField
from wtforms.validators import DataRequired, optional, length, Email, EqualTo
from . import models

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

class CreateUserForm(FlaskForm):
    username = StringField("Userame", validators=[DataRequired(), length(max=256)])
    email = StringField("Email", validators=[DataRequired(), length(max=256), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])

class UserProfile(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), length(max=256)])
    age = DecimalField("Age", validators=[optional()])
    profile_pic = FileField("Profile Pic", validators=[optional()])
    about_me = TextAreaField("About Me", validators=[optional(), length(max=256)])
    submit = SubmitField("Register")

#delete user



