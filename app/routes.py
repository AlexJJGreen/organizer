from flask import render_template, url_for
from flask import current_app as app

@app.route("/index")
@app.route("/")
def index():
    subtitle = "Home"
    return render_template("base.html", subtitle=subtitle)