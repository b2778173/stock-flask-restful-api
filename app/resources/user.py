from flask import Flask, request, jsonify
from flask_restful import Resource
from app.model.profile import Profile
from flask_jwt import jwt_required


class getUsers(Resource):
    @jwt_required()
    def get(self):
        return Profile.getAll()


class CreateUser(Resource):
    def post(self):
        print(request.get_json())
        username = request.get_json().get('username')
        password = request.get_json().get('password')
        name = request.get_json().get('name')
        create_time = request.get_json().get('create_time')
        email = request.get_json().get('email')
        address = request.get_json().get('address')
        social_media = request.get_json().get('social_media')
        watchlist = request.get_json().get('watchlist')
        print(username, create_time, email, social_media)
        try:
            response = Profile.create_profile(self, username, password, name, create_time,
                                              email, address, social_media, watchlist)
            return response, 201
        except Exception as e:
            print(f'insert fail, error: {e}')
            return {'message': f'insert {username} fail, error: {e}'}, 403


class UpdateUser(Resource):
    @jwt_required()
    def post(self, username):
        print(request.get_json())
        name = request.get_json().get('name')
        create_time = request.get_json().get('create_time')
        email = request.get_json().get('email')
        address = request.get_json().get('address')
        social_media = request.get_json().get('social_media')
        watchlist = request.get_json().get('watchlist')
        print(username, name, email, social_media, watchlist)

        try:
            response = Profile.update_profile(self, username, name,
                                              email, address, social_media, watchlist)
            print(f'update {username} success')
            return response, 201
        except Exception as e:
            print(f'update fail, error: {e}')
            return {'message': f'update {username} fail, error: {e}'}, 403


class ChangePassword(Resource):
    @jwt_required()
    def post(self, username):
        print(self)
        print(request.get_json())
        password = request.get_json().get('password')
        print(username, password)

        try:
            response = Profile.change_password(self, username, password)
            print(f"change {username}'s password success")
            return response, 201
        except Exception as e:
            print(f'update fail, error: {e}')
            return {'message': f'change {username} password fail, error: {e}'}, 403