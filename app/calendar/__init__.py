from flask import Blueprint

calendar = Blueprint("calendar", __name__, static_folder="static", template_folder="templates")