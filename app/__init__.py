from flask import Flask
from config import Config
from app.calendar_crud import calendar_crud

app = Flask(__name__)
### NB ### url prefix is passed to static url as well... FIND FIX OR ADD STATIC FOLDER TO CRUD!!! ###
app.register_blueprint(calendar_crud, url_prefix="/calendar")
app.config.from_object(Config)

from app import routes