from flask import Flask, request
from flask_restful import Resource, Api

from pymongo import MongoClient
from app.config import config
from app.model.main import setup
from app.model.wishlist import  Wishlist

client = MongoClient(host='127.0.0.1', port=27017)
# connect mongo
client = MongoClient(vars(config['development'])['MONGODB_CONNECTION_STRING'])
db = client.test
collection = db.tickers

setup()
# Wishlist.add_wishlist('O')

# print(f'db.server_info: {db.server_info}')


from app.resources.stock import Stock
from app.resources.stock import News
from app.resources.stock import CompanyNews
from app.resources.wishlist import FindWishList
from app.resources.wishlist import AddWishList
from app.resources.wishlist import RemoveWishList





def create_app(config_name):
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
    api.add_resource(AddWishList, '/add_wishlist/<symbol>')
    api.add_resource(RemoveWishList, '/remove_wishlist/<symbol>')
    return app
