from flask import Flask, request
from flask_restful import Resource, Api

from pymongo import MongoClient
from app.config import config

# client = MongoClient(host='127.0.0.1', port=27017)
# connect mongo
client = MongoClient(vars(config['development'])['MONGODB_CONNECTION_STRING'])
db = client.test
collection = db.tickers
# print(f'db.server_info: {db.server_info}')


from app.resources.stock import Stock
from app.resources.stock import News
from app.resources.stock import CompanyNews
from app.resources.wishlist import FindWishList



def create_app(config_name):
    config_name = 'development'
    print('config_name=' , str(config_name))
    app = Flask(__name__)
    api = Api(app)
    # Load the default configuration
    app.config.from_object(config[config_name])
    # print(f'app.config = {app.config}')
    api.add_resource(Stock, '/stock')
    api.add_resource(News, '/news')
    api.add_resource(CompanyNews, '/company-news')
    api.add_resource(FindWishList, '/wishlist')
    return app
