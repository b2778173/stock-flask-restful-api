from flask import Flask, request, jsonify
from flask_restful import Resource
from app import db
from bson.json_util import loads, dumps

collection = db.tickers


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
        print(symbol)
        data = {'name': symbol, 'marketCap': 1, 'price': 1}
        try:
            collection.insert_one(data)
            print(f'insert {symbol} success')
            return {'message': f'insert {symbol} success'}, 200
        except:
            print(f'insert {symbol} fail')
            return {'message': f'insert {symbol} fail'}, 403


class RemoveWishList(Resource):
    def delete(self):
        try:
            collection.drop()
            print(f'drop success')
            return {'message': 'drop success'}, 200
        except:
            print(f'drop fail')
            return {'message': 'drop fail'}, 403
