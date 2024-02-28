import os
from environs import Env
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
# change to debug mode if ENV is in development
DEBUG = ENV == "development"
DEBUG_TB_ENABLED = DEBUG

# SQLAlchemy ORM
SQLALCHEMY_DATABASE_URI = env.str("DB_URL") or \
        'postgresql://' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SECRET_KEY = env.str("SECRET_KEY")

# flask_jwt_extended for session management
JWT_SECRET_KEY = "super-secret"
ACCESS_EXPIRES = timedelta(hours=1)
JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
