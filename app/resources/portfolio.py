from datetime import datetime
from flask_restful import Resource, reqparse
from flask import request, jsonify, make_response
from flask_jwt import jwt_required, current_identity
from app.model.portfolio import Portfolio as PortfolioModel
from app.model.profile import Profile as ProfileModel
import logging

# get from jwt


def get_user():
    profile: ProfileModel = current_identity
    user_id = profile.get_current_profile().get('_id')
    return user_id


class Portfolio(Resource):
    """ validation """
    parser = reqparse.RequestParser()
    parser.add_argument(
        'symbol', type=str, required=True, help='symbol {error_msg}'
    )
    parser.add_argument(
        'company_name', min, type=str, required=True, help='company_name {error_msg}'
    )
    parser.add_argument(
        'trade_price', type=int, required=True, help='email {error_msg}'
    )
    parser.add_argument(
        'create_time', required=False, help='create_time {error_msg}'
    )
    parser.add_argument(
        'history', required=False, help='history {error_msg}'
    )
    parser.add_argument(
        'social_media', required=False, help='social_media {error_msg}'
    )
    parser.add_argument(
        'watchlist', required=False, help='watchlist {error_msg}'
    )
    """get portfolio list"""
    @jwt_required()
    def get(self):
        user_id = get_user()
        try:
            user_id = get_user()
            return {'result': PortfolioModel.getPortfolioList(user_id)}, 200
        except Exception as e:
            return {'error': f'get_portfolio_list fail, error: {e}'}, 400

    """add portfolio"""
    @jwt_required()
    def post(self):
        symbol = request.get_json()['symbol']
        company_name = request.get_json().get('company_name')
        history = request.get_json().get('history')
        trade_price = request.get_json().get('trade_price')
        market_price = request.get_json().get('market_price')
        profit = request.get_json().get('profit')
        profit_percentage = request.get_json().get('profit_percentage')
        memo = request.get_json().get('memo')
        # current time
        trade_time = datetime.now
        user_id = get_user()
        logging.debug(symbol, company_name, history, trade_price, user_id)
        try:
            response = PortfolioModel.insertPortfolio(
                self, symbol, company_name, history, trade_time, trade_price, market_price, profit, profit_percentage, memo, user_id)
            return response, 201

        except Exception as e:
            logging.debug(f'insert fail, error: {e}')
            return {'error': f'insert {symbol} fail, error: {e}'}, 400
