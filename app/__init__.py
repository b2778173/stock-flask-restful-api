from flask_cors import CORS
from app.resources.user import User, getUserList, ChangePassword, getCurrentUser, SendMail
from app.resources.watchlist import RemoveWatchlist, AddWatchlist, GetWatchlist
from app.resources.stock import CompanyNews, News, Stock, Stock_candle, Day_mover, Quote
from app.resources.portfolio import Portfolio
from flask import Flask
from flask_restful import Api
from app.config import config
from app.model.main import setup
from app.model.profile import Profile
from flask_jwt import JWT


jwt = JWT(None, Profile.authenticate, Profile.identity)


def create_app(config_name):
    print('config_name=', str(config_name))
    print('start successfully')
    app = Flask(__name__)
    api = Api(app)
    CORS(app)
    # Load the default configuration
    app.config.from_object(config[config_name])
    # print(f'app.config = {app.config}')
    jwt.init_app(app)
    # connect mongo
    setup(app.config['MONGODB_CONNECTION_STRING'])

    api.add_resource(Quote, '/quote')
    api.add_resource(Stock, '/stock')
    api.add_resource(Stock_candle, '/stock_candle')
    api.add_resource(Day_mover, '/day_mover')
    api.add_resource(News, '/news')
    api.add_resource(CompanyNews, '/company_news')
    api.add_resource(GetWatchlist, '/watchlist')
    api.add_resource(AddWatchlist, '/add_watchlist/<symbol>')
    api.add_resource(RemoveWatchlist, '/remove_watchlist/<symbol>')
    api.add_resource(getCurrentUser, '/get_current_user')
    api.add_resource(User, '/user/<username>')
    api.add_resource(getUserList, '/user/all')
    api.add_resource(ChangePassword, '/change_password/<username>')
    api.add_resource(Portfolio, '/portfolio')
    api.add_resource(SendMail, '/sendmail/<user>')

    return app
