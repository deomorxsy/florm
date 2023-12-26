# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from werkzeug.security import generate_password_hash, check_password_hash
# from werkzeug import security
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
