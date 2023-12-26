# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from app.extensions import bcrypt
from app.database import db, Column, relationship, PkModel, reference_col
#from werkzeug.security import generate_password_hash, check_password_hash
#from . import db

class Role(PkModel):
    ''' add role for user '''
    __tablename__ = 'roles'
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="roles")

    def __init__(self, name, kwargs):
        """ create instance """
        super().__init__(name=name, **kwargs)
    def __repr__(self):
        return f'<Role({self.name})>'


class User(UserMixin, db.Model):
    ''' app user '''

    __tablename__ = 'users'
    username = Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True)
    _password = Column("password", db.LargeBinary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, defautl=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    name = db.Column(db.String(1000))
    surname = db.Column(db.String(1000))
    id = db.Column(db.Integer, primary_key=True)

    @hybrid_property
    def password(self):
        ''' hash the password '''
        return self._password

    @password.setter
    def password(self, value):
        self._password = bcrypt.generate_password_hash(value)

    def set_password(self, password):
        # create password and hash it
        password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        # check hashed password
        return check_password_hash(self.password, password)


    def __repr__(self):
        return '<User {}>'.format(self.id)

