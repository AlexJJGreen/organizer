from . import calendar_crud
from flask import render_template, url_for


@calendar_crud.route("/create")
def create():
    return render_template("base.html")

@calendar_crud.route("/read")
def read():
    return "READ"

@calendar_crud.route("/update")
def update():
    return "UPDATE"

@calendar_crud.route("/delete")
def delete():
    return "DELETE"