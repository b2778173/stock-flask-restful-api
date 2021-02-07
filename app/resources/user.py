from flask import Flask, request, jsonify
from flask_restful import Resource
from app.model.profile import Profile


class getUsers(Resource):
    def get(self):
        return Profile.getAll()


class CreateUser(Resource):
    def post(self):
        print(request.get_json())
        name = request.get_json().get('name')
        create_time = request.get_json().get('create_time')
        email = request.get_json().get('email')
        address = request.get_json().get('address')
        social_media = request.get_json().get('social_media')
        watchlist = request.get_json().get('watchlist')
        print(name, create_time, email, social_media)
        try:
            Profile.add_profile(name, create_time,
                                email, address, social_media, watchlist)
            print(f'insert {name} success')
            return {'message': f'insert {name} success'}, 201
        except Exception as e:
            print(f'insert fail, error: {e}')
            return {'message': f'insert {name} fail, error: {e}'}, 403
