from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

import os 

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config["SECRET_KEY"] = SECRET_KEY

db = SQLAlchemy(app)

from application import routes
