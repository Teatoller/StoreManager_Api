from flask_restful import Resource
from flask import request
from app.api.v1.models.users import UserModel, ListDatabase


class Registration(Resource):
    def get(self, user):
        """ Method to return a single user from USERS list """
        user = ListDatabase.get_user_id(id)
        if user:
            return {"status": "success", "user": user.resultant()}, 200
        return {"status": "Failed!", "msg": "user not found"}, 404


class Users(Resource):
    def post(self):
        """ Method for validating and adding user """
        data = request.get_json(force=True)
        if 'name' not in data:
            return {"msg": "please input name"}, 406
        if 'price' not in data:
            return {"msg": "please input price :"}, 406
        if 'quantity' not in data:
            return{"msg": "Stock is Nil"}, 406

        user = UserModel(
            data['username', help='This field is required', required=True, type=str]
            data['email', help='This field is required', required=True, type=str],
            data['password', help='This field is required', required=True, type=str])
        ListDatabase.USERS.append(user)
        response = user.resultant()
        return {"status": "success!", "user": response}, 201

    def get(self):
        """ Iterates and loop USERS list and returns all items in
         USERS  database"""
        user = [i.resultant() for i in ListDatabase.USERS]
        return {"status": "success!", "users": user}, 200