from . import users
from flask import render_template, url_for, flash, redirect
from .forms import LoginForm, CreateUserForm
from .models import User, UserProfile
from flask_login import current_user, login_user, logout_user
from flask_wtf.file import FileAllowed

@users.route("/login", methods=["GET", "POST"])
def login():
    subtitle = "Login"
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for("login"))
    return render_template("login.html", subtitle=subtitle, form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@users.route("/create_user", methods=["GET", "POST"])
def create_user():
    subtitle = "Create User"
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = CreateUserForm()
    if form.validate_on_submit():
        check_username = User.query.filter_by(username=form.username.data)
        if check_username:
            flash("Username already exists. Please use a different name")
        else:
           user = User()
           return redirect(url_for("login"))
    return render_template("create_user", subtitle=subtitle, form=form)

#add login rquired
@users.route("/profile", methods=["GET", "POST"])
def profile():
    subtitle = "Profile"
    #query database - get user profile
    # populate form with data


    #on submit
    # validate with FileAllowed, UploadSet https://flask-wtf.readthedocs.io/en/stable/api.html#flask_wtf.file.FileField
    # push changes to db
    return render_template("profile", subtitle=subtitle)


