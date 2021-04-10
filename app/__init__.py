from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager

migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    # create blueprint databases
    with app.app_context():
        
        ### NB ### url prefix is passed to static url as well... FIND FIX OR ADD STATIC FOLDER TO CRUD!!! ###
        # calendar_crud modules
        from app.calendar_crud import calendar_crud
        from app.calendar_crud.models import db as calendar_crud_db
        app.register_blueprint(calendar_crud, url_prefix="/crud")
        
        # user modules
        from app.users import users
        from app.users.models import db as user_db
        app.register_blueprint(users, url_prefix="/users")

        # calendar modules
        from app.calendar import calendar
        app.register_blueprint(calendar, url_prefix="/calendar")

        # group modules
        from app.groups import groups
        from app.groups.models import db as group_db
        app.register_blueprint(groups, url_prefix="/groups")

        # init blueprint databases
        dbs = [user_db, calendar_crud_db, group_db]
        for db in dbs:
            db.init_app(app)
            migrate.init_app(app, db)
            db.create_all()

        #init login manager
        login.init_app(app)

        from app import routes

        #if not app.debug and not app.testing:
        return app