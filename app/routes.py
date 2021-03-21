from app import app
from flask import render_template, url_for

@app.route("/index")
@app.route("/")
def index():
    subtitle = "Home"
    today = TODAY.day
    month = get_month(TODAY)
    return render_template("index.html", subtitle=subtitle, month=month, today=today)