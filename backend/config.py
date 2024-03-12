import os
basedir = os.path.abspath(os.path.dirname(__file__))

#class Config(object):
class Config:
    ROOT_PATH = basedir
    # below an example of a secret key. For the proof of concept,
    # this is used, but the best practice is to set environment
    # variables or secrets to handle these infos.
    SECRET_KEY = 'gV7S6iGV560ZikWik170'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL') or \
        'postgresql://' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_CONFIG_CLAIM = 431432


