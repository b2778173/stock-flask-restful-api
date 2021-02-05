from app.resources.user import CreateUser
from app.resources.user import getUsers
from app.resources.watchlist import RemoveWatchlist
from app.resources.watchlist import AddWatchlist
from app.resources.watchlist import GetWatchlist
from app.resources.stock import CompanyNews
from app.resources.stock import News
from app.resources.stock import Stock
from flask import Flask, request
from flask_restful import Resource, Api

from app.config import config
from app.model.main import setup
from app.model.watchlist import Watchlist


# connect mongo
setup()


def create_app(config_name):
    print('config_name=', str(config_name))
    app = Flask(__name__)
    api = Api(app)
    # Load the default configuration
    app.config.from_object(config[config_name])
    # print(f'app.config = {app.config}')
    api.add_resource(Stock, '/stock')
    api.add_resource(News, '/news')
    api.add_resource(CompanyNews, '/company-news')
    api.add_resource(GetWatchlist, '/watchlist')
    api.add_resource(AddWatchlist, '/add_watchlist/<symbol>')
    api.add_resource(RemoveWatchlist, '/remove_watchlist/<symbol>')
    api.add_resource(CreateUser, '/create_user')
    api.add_resource(getUsers, '/get_users')

    return app
