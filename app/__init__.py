from flask import Flask
from config import Config
from app.users import users
from app.calendar_crud import calendar_crud
# figure out how and where to correctly init the db instance
# from app.calendar_crud.models import db
from flask_migrate import Migrate

app = Flask(__name__)
### NB ### url prefix is passed to static url as well... FIND FIX OR ADD STATIC FOLDER TO CRUD!!! ###
app.register_blueprint(calendar_crud, url_prefix="/crud")
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(calendar, url_prefix="calendar")

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


from app import routes