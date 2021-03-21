from . import users
from flask import render_template, url_for
from .forms import LoginForm

@users.route("/login")
def login(methods=["GET", "POST"]):
    subtitle = "Login"
    form = LoginForm()
    return render_template("login.html", subtitle=subtitle, form=form)