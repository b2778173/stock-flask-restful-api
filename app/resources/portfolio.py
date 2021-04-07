from datetime import datetime
from flask_restful import Resource, reqparse
from flask import request
from flask_jwt import jwt_required, current_identity
from app.model.portfolio import Portfolio as PortfolioModel
from app.model.profile import Profile as ProfileModel

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
        'history', type=str, required=True, help='history {error_msg}'
    )
    parser.add_argument(
        'trade_price', type=float, required=True, help='trade_price {error_msg}'
    )
    parser.add_argument(
        'market_price', required=False, help='market_price {error_msg}'
    )

    parser.add_argument(
        'memo', type=str, required=False, help='memo {error_msg}'
    )

    """ get portfolio by user id """
    @jwt_required()
    def get(self):
        try:
            user_id = get_user()
            print('user_id=', user_id)
            return {'result': PortfolioModel.find(user_id)}, 200

        except Exception as e:
            return {'message': f'get_portfolio_list fail, error: {e}'}, 400

    """create portfolio"""
    @jwt_required()
    def post(self):
        """args"""
        data = Portfolio.parser.parse_args()

        symbol = data['symbol']
        company_name = data['company_name']
        history = data['history']
        trade_price = data['trade_price']
        market_price = data['market_price']
        # profit = data['profit']
        # profit_percentage = data['profit_percentage']
        memo = data['memo']
        # current time
        trade_time = datetime.now
        user_id = get_user()
        print(symbol, company_name, history, trade_price, user_id)
        try:
            response = PortfolioModel.insert(
                self, symbol, company_name, history, trade_time, trade_price, market_price, memo, user_id)
            return {'message': response}, 201

        except Exception as e:
            print(f'insert fail, error: {e}')
            return {'message': f'insert {symbol} fail, error: {e}'}, 400
