from flask import Blueprint, jsonify
from flask_cors import CORS, cross_origin

blueprint = Blueprint('ping', __name__)

CORS(blueprint)

@blueprint.route('/ping/', methods=['GET'])
def ping_pong():
    response = jsonify('pong!')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


#blueprint.route('/ping/', methods=['GET'])(ping_pong)

