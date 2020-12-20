import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))                     

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "meme"         
    SQLALCHEMY_DATABASE_URI = (                                             
            os.environ.get('DATABASE_URL') or 
            'sqlite:///' + os.path.join(BASE_DIR, 'blog.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "me")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "meme")