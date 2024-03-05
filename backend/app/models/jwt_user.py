# from flask_login import UserMixin, not used by jwt
from app.database import Column, PkModel, db, reference_col, relationship

# logging timestamps
# import datetime as dt
from datetime import datetime

# database hybrid
from sqlalchemy.ext.hybrid import hybrid_property

# password hashing algorithm
from app.extensions import bcrypt

from sqlalchemy import (
        String,
        Column,
        Integer,
        DateTime,
        ForeignKey
        )
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.declarative import declared_attr

class User(db.Model):
    id = Column(Integer, primary_key = True)
    email = Column(String(250), nullable = False, unique = True)
    username = Column(String(250), nullable = False, unique = True)
    password = Column(String(250), unique = False)


class Session(db.Model):
    @declared_attr
    def __tablename__(cls):
        return 'session'

    id = Column(Integer, primary_key = True)
    user = db.relationship(User)
    user_id = Column(Integer, ForeignKey(User.id))

    jti_access = Column(String(36), nullable = False, index = True)
    jti_refresh = Column(String(36), nullable = False, index = True)

    created_at = Column(DateTime, default = datetime.now(), nullable = False)
