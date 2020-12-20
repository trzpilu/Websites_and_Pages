from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from users_base_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from users_base_app import routes, models

api = Api(app, doc='/')
api.add_namespace(routes.users_namespace, '/users')