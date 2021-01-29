from flask import Flask, request
from flask_restful import Resource, Api
from resources.stock import Stock
from resources.stock import News
from resources.stock import CompanyNews
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)
client = MongoClient(host='127.0.0.1', port=27017)
db = client.demo

api.add_resource(Stock, '/stock')
api.add_resource(News, '/news')
api.add_resource(CompanyNews, '/company-news')

if __name__ == '__main__':
    app.run(debug=True)
