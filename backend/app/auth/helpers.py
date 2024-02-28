"""
helpers for authentication/authorization blocklist inspired by
https://github.com/vimalloc/flask-jwt-extended/blob/master/examples/blocklist_database.py
"""

from datetime import datetime, timedelta, timezone
from flask_jwt_extended import decode_token

# Changed in version 1.4: This exception is now part of the sqlalchemy.exc
# module in Core, moved from the ORM. The symbol remains importable from
# sqlalchemy.orm.exc.
from sqlalchemy.exc import NoResultFound

from app.extensions import db
from app.models.blocklist import TokenBlocklist


def add_token_to_database(encoded_token, identity_claim):
    decoded_token = decode_token(encoded_token)
    jti = decoded_token["jti"]
    token_type = decoded_token("type")
    user_identity = decoded_token[identity_claim]
    expires = datetime.fromtimestamp(decoded_token["exp"])
    revoked = False

    db_token = TokenBlocklist(
            jti=jti,
            token_type=token_type,
            user_id=user_identity,
            expires=expires,
            revoked=revoked,
            )
    db.session.add(db_token)
    db.session.commit()

def is_token_revoked(jwt_payload):
    """ check if token is revoked. If token
    is present on database, it is not revoked. """
    jti = jwt_payload
    try:
        token = TokenBlocklist.query.filter(jti=jti).one()
        return token.revoked
    except NoResultFound:
        return True

def revoke_token(token_jti, user):
    """ revokes token """
    try:
        token = TokenBlocklist.query.filter_by(
                jti=token_jti,
                user_id=user
                ).one()
        token.revoked = True
        db.session.commit()
    except NoResultFound:
        raise Exception(f'could not find the token {token_jti}')

