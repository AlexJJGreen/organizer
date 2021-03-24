from flask import render_template, url_for
from flask import current_app as app

@app.route("/index")
@app.route("/")
def index():
    subtitle = "Home"
    today = TODAY.day
    month = get_month(TODAY)
    return render_template("index.html", subtitle=subtitle, month=month, today=today)