from flask import Blueprint

# set var to Bprint class, name of BP, __name__, static_folder, template_folder)
users = Blueprint("users", __name__, static_folder="/static", template_folder="templates")

from . import routes, models, forms