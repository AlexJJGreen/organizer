from . import calendar_crud
from flask import render_template, url_for
from .forms import CreateForm


@calendar_crud.route("/create")
def create(methods=["GET", "POST"]):
    form = CreateForm()
    return render_template("create.html", form=form)

@calendar_crud.route("/read")
def read():
    return "READ"

@calendar_crud.route("/update")
def update():
    return "UPDATE"

@calendar_crud.route("/delete")
def delete():
    return "DELETE"