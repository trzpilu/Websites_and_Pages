SHORT_STRING_SIZE = 128
LONG_STRING_SIZE = 2048

import os
import uuid

BASE_DIR = os.path.abspath(os.path.dirname(__file__))    # 1

class Config:
   SECRET_KEY = os.environ.get("SECRET_KEY", str(uuid.uuid4()))
   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), '..', 'db.sqlite')
   SQLALCHEMY_TRACK_MODIFICATIONS = False