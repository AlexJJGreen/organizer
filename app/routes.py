from app import app
from flask import render_template, url_for
from app.calendars import get_month, TODAY
from app.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    subtitle = "Home"
    today = TODAY.day
    month = get_month(TODAY)
    return render_template("index.html", subtitle=subtitle, month=month, today=today)