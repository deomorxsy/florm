# -*- coding: utf-8 -*-
"""User models."""

from flask_login import UserMixin
from app.database import Column, PkModel, db, reference_col, relationship

# logging timestamps
import datetime as dt

# database hybrid
from sqlalchemy.ext.hybrid import hybrid_property

# password hashing algorithm and JWT on cookie with HttpOnly
from app.extensions import bcrypt

class Role(PkModel):
    """a role for a user"""

    __tablename__ = "roles"
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="roles")

    def __init__(self, name, **kwargs):
        """create instance"""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """represent instance as a unique string"""
        return f"<Role({self.name})>"


class User(UserMixin, PkModel):
    """a user of the app"""
    __tablename__ = "users"

    #id = db.Column(db.Integer, primary_key=True)
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    _password = Column("password", db.LargeBinary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_prof = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    # -*-  -*-
    @hybrid_property
    def password(self):
        """hashed password"""
        return self._password

    # -*- -*-
    @password.setter
    def password(self, value):
        """set password"""
        self._password = bcrypt.generate_password_hash(value)

    def check_password(self, value):
        """check password"""
        return bcrypt.check_password_hash(self._password, value)

    # -*-  -*-
    @property
    def full_name(self):
        """full user name"""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User({self.username!r})>"
