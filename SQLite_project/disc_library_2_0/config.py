SHORT_STRING_SIZE = 128
LONG_STRING_SIZE = 2048

import os
import uuid

# Set up base folder for databse
BASE_DIR = os.path.abspath(os.path.dirname(__file__))   

class Config:
   SECRET_KEY = os.environ.get("SECRET_KEY") or "wise_panda"
   
# Look for database config. If none, use SQLite   
   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), '..', 'db.sqlite')
   SQLALCHEMY_TRACK_MODIFICATIONS = False