# from flask_login import UserMixin, not used by jwt
from app.database import (
        Column, db,  # PkModel
        # reference_col, relationship
        )

# logging timestamps
# import datetime as dt
from datetime import datetime

# database hybrid
# from sqlalchemy.ext.hybrid import hybrid_property

# password hashing algorithm
from app.extensions import bcrypt

from sqlalchemy import (
        String,
        Column,
        Integer,
        DateTime,
        ForeignKey
        )
# from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.declarative import declared_attr


class User(db.Model):
    """an user of the app."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(db.String(80), unique=True, nullable=False)
    username = Column(db.String(250), unique=True, nullable=False)
    password = Column("password", db.LargeBinary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)

    def __repr__(self):
        """represent class"""
        return f'<User {self.username}>'

    # @property
    def full_name(self):
        """full user name"""
        return f"{self.first_name} {self.last_name}"

    def set_password(self, value):
        """set password"""
        self.password = bcrypt.generate_password_hash(value)

    def check_password(self, value):
        """check password"""
        return bcrypt.check_password_hash(self.password, value)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



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


