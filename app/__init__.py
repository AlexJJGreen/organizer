from flask import Flask
from config import Config
# user modules
from app.users import users
from app.users.models import db as user_db
# calendar_crud modules
from app.calendar_crud import calendar_crud
from app.calendar_crud.models import db as calendar_crud_db
# calendar modules
from app.calendar import calendar
from flask_sqlalchemy import SQLAlchemy
##### from flask_migrate import Migrate ####

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init blueprint databases
    user_db.init_app(app)
    calendar_crud_db.init_app(app)
    # create blueprint databases
    with app.app_context():
        user_db.create_all()
        calendar_crud_db.create_all()

    #migrate = Migrate(app, db) # <---- FIND MIGRATE FIX

    ### NB ### url prefix is passed to static url as well... FIND FIX OR ADD STATIC FOLDER TO CRUD!!! ###
    app.register_blueprint(calendar_crud, url_prefix="/crud")
    app.register_blueprint(users, url_prefix="/users")
    app.register_blueprint(calendar, url_prefix="/calendar")

    if not app.debug and not app.testing:
        # ... no changes to logging setup
        return app

from app import routes