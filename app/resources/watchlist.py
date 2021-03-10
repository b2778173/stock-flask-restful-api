from flask import Flask, request, jsonify
from flask_restful import Resource
from bson.json_util import loads, dumps
from app.model.watchlist import Watchlist


def beautify(val):
    val.pop('_id')
    return val


class FindWatchlist(Resource):
    def get(self):
        result = []
        # for t in collection.find():
        #     print(t)
        #     result.append(beautify(t))
        return jsonify(result)


class GetWatchlist(Resource):
    def get(self):
        return Watchlist.get_wishlist()


class AddWatchlist(Resource):
    def get(self, symbol):
        market_cap = request.args.get('market_cap ')
        price = request.args.get('price')
        try:
            Watchlist.add_wishlist(symbol, market_cap, price)
            print(f'insert {symbol} success')
            return {'message': f'insert {symbol} success'}, 200
        except Exception as e:
            print(f'insert fail, error: {e}')
            return {'message': f'insert {symbol} fail, error: {e}'}, 403


class RemoveWatchlist(Resource):
    def delete(self, symbol):
        try:
            Watchlist.remove_wishlist(symbol)
            print(f'drop success')
            return {'message': 'drop success'}, 200
        except Exception as e:
            print(f'drop fail, error: {e}')
            return {f'drop fail, error: {e}'}, 400
