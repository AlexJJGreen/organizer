from flask import render_template, redirect
from .models import Group
from .forms import CreateGroupForm


@groups.route("/create_group", methods=["GET", "POST"])
def create_group():
    form = CreateGroupForm()
    #create db session add new group
    # 
    return render_template("group.html", form=form)

@groups.route("edit_group", methods=["GET", "POST"])
def edit_group():
    form=CreateGroupForm()
    # query db for group info and populate form
    return render_template("edit_group.html", form=form)