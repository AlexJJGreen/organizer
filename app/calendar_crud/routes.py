from app import app
from calendar_crud import calendar_crud
from flask import render_template


@calendar_crud.route("/create")
def create():
    return "CREATE"

@calendar_crud.route("/read")
def read():
    return "READ"

@calendar_crud.route("/update")
def update():
    return "UPDATE"

@calendar_crud.route("/delete")
def delete():
    return "DELETE"