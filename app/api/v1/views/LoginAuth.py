from flask_restful import Resource
import datetime
from flask import request, make_response, jsonify
import re
import jwt
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from functools import wraps
from passlib.hash import pbkdf2_sha256 as sha245

def auth_required(func):
    @wraps(func)
    def decorator_func(*args, **kwargs):
        token = None
        if 'x-access-token'in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({"message":"login to continue"}))
        try:
            data = jwt.decode(token, "secret")
            current_user = [user for user in users if user['user_id']==data['user_id']]
        except:
            return make_response(jsonify({"message": "token invalid"}),401)
        return func(current_user, *args, **kwargs)
    return decorator_func


class AccountCreation(Resource):

    def post(self):
        """ """
        data = request.get_json(force=True)
        User_id = len(users) + 1
        username = data["username"]
        email = data["email"]
        password = data["password"]
        role = data["role"]
        if not re.match('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])', request.json['password']):
            return make_response(jsonify{"message": "password invalid"}) 
        if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', request.json['email']:)
            return make_response(jsonify(jsonify({"message": "email no valid"}), 401)
        
        new_user_info = {"user_id": User_id,
        "username": username,
        "email": email,
        "password": sha245_crypt(password),
        "role": role}

        if request.json['email'] not in [user['email'] for user in users]:
            users.append(new_user_info)
            return make_response(jsonify(jsonify{"message": "successful account creation"}), 201)        
        return make_response(jsonify({"message": "{} already in system".format(request.json['email'])}),       
        409) 