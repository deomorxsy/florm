from flask_cors import CORS
from flask import (
        request, jsonify,
        redirect, url_for,
        flash, Blueprint,
        current_app as app
        )
from flask_jwt_extended import (
    create_access_token, # make JSON Web Tokens
    create_refresh_token,
    jwt_required, # protect routes
    get_jwt_identity, # get identity of JWT in a protected route
    get_jwt, #
)
from app.models.jwt_user import User
# replace by swagger
# from app.extensions import bcrypt,jwt, apispec
from app.extensions import bcrypt, jwt
from app.auth.helpers import (
        revoke_token,
        is_token_revoked,
        add_token_to_database,
        )


blueprint = Blueprint('auth', __name__, url_prefix='/auth')
CORS(blueprint)

@blueprint.route("/register", methods=["POST"])
def register():
    """register new user"""

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username or not password:
        return jsonify({"msg": "case 1: Missing username or password"}), 400

    user = User.get_by_username(username=username)
    if user is not None:
        return jsonify({"error": "user already exists. :("}), 409

    # user schema, hashing and commit logic goes into models.jwt_user
    new_user = User(username=username, email=email)
    new_user.set_password(value=password)
    new_user.save()

    response = jsonify({"msg": "user created! :D"})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@blueprint.route("/login", methods=["POST"])
def login():
    """ login route for connection with frontend """

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    if user is None or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"msg": "bad credentials"}), 400

    if not request.is_json:
        return jsonify({"msg": "Missing username or password"}), 400

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    add_token_to_database(access_token, app.config["JWT_IDENTITY_CLAIM"])
    add_token_to_database(refresh_token, app.config["JWT_IDENTITY_CLAIM"])

    # returns the access_token and the refresh token
    ret = {"access_token": access_token, "refresh_token": refresh_token}
    return jsonify(ret), 200


@blueprint.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    ret = {"access_token": access_token}
    add_token_to_database(access_token, app.config["JWT_IDENTITY_CLAIM"])
    return jsonify(ret), 200


@blueprint.route("/revoke_access", methods=["DELETE"])
@jwt_required
def revoke_access():
    jti = get_jwt()["jti"]
    user_identity = get_jwt_identity()
    revoke_token(jti, user_identity)
    return jsonify({"message": "token revoked"}), 200


@blueprint.route("/revoke_refresh", methods=["DELETE"])
@jwt_required(refresh=True)
def revoke_refresh():
    jti = get_jwt()["jti"]
    user_identity = get_jwt_identity()
    revoke_token(jti, user_identity)
    return jsonify({"message": "token revoked"}), 200


@jwt.user_lookup_loader
def user_loader_callback(jwt_headers, jwt_payload):
    identity = jwt_payload["sub"]
    return User.query.get(identity)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_headers, jwt_payload):
    return is_token_revoked(jwt_payload)

# adjust last one to swagger instead of api
