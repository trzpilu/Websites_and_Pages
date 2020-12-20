from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from config import Config
#alt: from users_base_app.config import Config

# Loading Flask
app = Flask(__name__)
# Loading config.py
app.config.from_object(Config)
# Defining database
db = SQLAlchemy(app)
# Setting up migration between app and database
migrate = Migrate(app, db)

# Importing routes and models
from app import routes, models

api = Api(app, doc='/')
api.add_namespace(routes.discs_namespace, '/discs')