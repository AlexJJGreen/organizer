from app import app
from flask import render_template
from app.calendars import get_month, TODAY

@app.route("/index")
@app.route("/")
def index():
    today = TODAY.day
    month = get_month(TODAY)
    subtitle = "Home"
    return render_template("index.html", subtitle=subtitle, month=month, today=today)