from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, make_response

# get all alumni
def get_all_alumni(Alumni, id):
    try:
        alumni = Alumni.query.all()
        # returns a jsonified function inside a list comprehension lambda lingo
        return make_response(jsonify([item.json() for item in alumni]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting alumni'}), 500)

#
# get alumni by id
def get_alumni(Alumni, id):
    try:
        alumni = Alumni.query.filter_by(id=id).first()
        if alumni:
            return make_response(jsonify({'alumni': alumni.json()}), 200)
        return make_response(jsonify({'message': 'alumni not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting alumni'}), 500)

# update alumni
def update_alumni(Alumni, id):
    try:
        alumni = Alumni.query.filter_by(id=id).first()
        if alumni:
            data = request.get_json()
            alumni.username = data['username']
            alumni.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message': 'user updated'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error updating user'}), 50)

# delete alumni
def delete_alumni(Alumni, id):
    try:
        alumni = Alumni.query.filter_by(id=id).first()
        if alumni:
            db.session.delete(alumni)
            db.session.commit()
            return make_response(jsonify({'message': 'alumni deleted'}), 200)
        return make_response(jsonify({'message': 'alumni not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting alumni'}), 500)