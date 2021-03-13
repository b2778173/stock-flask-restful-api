from datetime import datetime
from flask_restful import Resource
from flask import Flask, request, jsonify, make_response
from flask_jwt import jwt_required, current_identity
from app.model.portfolio import Portfolio as PortfolioModel
from app.model.profile import Profile as ProfileModel

# get from jwt
def get_user():
    profile: ProfileModel = current_identity
    user_id = profile.get_current_profile().get('_id')
    return user_id

class add_portfolio(Resource):
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
        print(symbol, company_name, history, trade_price, user_id)
        try:
            response = PortfolioModel.insertPortfolio(
                self, symbol, company_name, history, trade_time, trade_price, market_price, profit, profit_percentage, memo, user_id)
            return response, 201

        except Exception as e:
            print(f'insert fail, error: {e}')
            return {'message': f'insert {symbol} fail, error: {e}'}, 400


class get_portfolio_list(Resource):
    @jwt_required()
    def get(self):
        try:
            user_id = get_user()
            return PortfolioModel.getPortfolioList(user_id)
            
        except Exception as e:
            return {'message': f'get_portfolio_list fail, error: {e}'}, 400
