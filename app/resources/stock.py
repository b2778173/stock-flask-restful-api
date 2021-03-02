from flask import Flask, request, current_app, Blueprint
from flask.globals import current_app
from flask_restful import Resource
import requests
import finnhub


# app = Flask(__name__)
# Load the default configuration
# print('app1', current_app)
# app.config.from_object(config['development'])
# print('stock app.config=', app.config["API_KEY"])
# API_KEY = (app.config["API_KEY"])
# FINNHUB_BASE_URL = (app.config["FINNHUB_BASE_URL"])


class Stock(Resource):
    def get(self):
        API_KEY = current_app.config["API_KEY"]
        finnhub_client = finnhub.Client(api_key=API_KEY)
        symbol = (request.args.get('symbol'))
        r = finnhub_client.symbol_lookup(symbol)
        return r


class News(Resource):
    def get(self):
        API_KEY = current_app.config["API_KEY"]
        finnhub_client = finnhub.Client(api_key=API_KEY)
        category = (request.args.get('category'))
        minId = (request.args.get('minId'))
        r = finnhub_client.general_news(category, minId)
        return r


class CompanyNews(Resource):
    def get(self):
        API_KEY = current_app.config["API_KEY"]
        finnhub_client = finnhub.Client(api_key=API_KEY)
        symbol = (request.args.get('symbol'))
        begin = (request.args.get('from'))
        end = (request.args.get('to'))
        print(begin,end)
        r = finnhub_client.company_news(symbol, _from=begin, to=end)
        return r
