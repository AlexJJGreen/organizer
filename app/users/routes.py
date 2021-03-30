from . import users
from flask import render_template, url_for
from .forms import LoginForm
from .models import User
from flask_login import current_user, login_user, logout_user

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

@users.route("logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
