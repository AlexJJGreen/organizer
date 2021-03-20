from flask import Flask
from config import Config
from app.calendar_crud.calendar_crud import calendar_crud

app = Flask(__name__)
app.register_blueprint(calendar_crud, url_prefix="/calendar")
app.config.from_object(Config)

from app import routes
from calendar_crud import routes