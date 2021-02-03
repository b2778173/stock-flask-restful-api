from flask import Flask, request, jsonify
from flask_restful import Resource
from app import db
from bson.json_util import loads, dumps
from app.model.wishlist import Wishlist

collection = db.wishlist


def beautify(val):
    val.pop('_id')
    return val


class FindWishList(Resource):
    def get(self):
        result = []
        for t in collection.find():
            print(t)
            result.append(beautify(t))
        return jsonify(result)


class AddWishList(Resource):
    def get(self, symbol):
        try:
            Wishlist.add_wishlist(symbol)
            print(f'insert {symbol} success')
            return {'message': f'insert {symbol} success'}, 200
        except Exception as e:
            print(f'drop fail, error: {e}')
            return {'message': f'insert {symbol} fail, error: {e}'}, 403


class RemoveWishList(Resource):
    def delete(self, symbol):
        try:
            Wishlist.remove_wishlist(symbol)
            print(f'drop success')
            return {'message': 'drop success'}, 200
        except Exception as e:
            print(f'drop fail, error: {e}')
            return {f'drop fail, error: {e}'}, 400
