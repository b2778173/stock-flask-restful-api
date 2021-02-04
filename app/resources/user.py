from flask import Flask, request, jsonify
from flask_restful import Resource
from app.model.profile import Profile


class CreateUser(Resource):
    def post(self):
        print(request.get_json())
        user_id = request.get_json().get('user_id')
        name = request.get_json().get('name')
        create_time = request.get_json().get('create_time')
        email = request.get_json().get('email')
        facebook_id = request.get_json().get('facebook_id')
        line_id = request.get_json().get('line_id')
        print(user_id, name, create_time, email, facebook_id, line_id)
        try:
            Profile.add_profile(self, user_id, name, create_time,
                                email, facebook_id, line_id)
            print(f'insert {name} success')
            return {'message': f'insert {name} success'}, 201
        except Exception as e:
            print(f'insert fail, error: {e}')
            return {'message': f'insert {name} fail, error: {e}'}, 403
