"""
blocklist implementation from the database

"""
from flask import Flask, jsonify
from datetime import timedelta
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
    JWTManager
)
import redis

from app.extensions import db

ACCESS_EXPIRES = timedelta(hours=1)



class TokenBlocklist(db.Model):
    """ blocklist representation """

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, unique=True)
    token_type = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    revoked = db.Column(db.Boolean, nullable=False)
    expires = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", lazy="joined")

    # dict to json
    def to_dict(self):
        return {
            "token_id": self.id,
            "jti": self.jti,
            "token_type": self.token_type,
            "user_identity": self.user_identity,
            "revoked": self.revoked,
            "expires": self.expires,
        }
