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
