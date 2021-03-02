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
        FINNHUB_BASE_URL = current_app.config["FINNHUB_BASE_URL"]
        API_KEY = current_app.config["API_KEY"]
        finnhub_client = finnhub.Client(api_key=API_KEY)
        symbol = (request.args.get('symbol'))
        # r = requests.get(
        #     f'{FINNHUB_BASE_URL}/search?q={symbol}&token={API_KEY}')
        r = finnhub_client.symbol_lookup(symbol)
        return(r)


class News(Resource):

    def get(self):
        FINNHUB_BASE_URL = current_app.config["FINNHUB_BASE_URL"]
        API_KEY = current_app.config["API_KEY"]
        category = (request.args.get('category'))
        minId = (request.args.get('minId'))
        url = f'{FINNHUB_BASE_URL}/news?category={category}&token={API_KEY}'
        if minId != None:
            url += f"&{minId}"
        r = requests.get(url)
        return(r.json())


class CompanyNews(Resource):
    def get():
        FINNHUB_BASE_URL = current_app.config["FINNHUB_BASE_URL"]
        API_KEY = current_app.config["API_KEY"]
        symbol = (request.args.get('symbol'))
        begin = (request.args.get('from'))
        end = (request.args.get('to'))
        url = f'{FINNHUB_BASE_URL}/company-news?symbol={symbol}&from={begin}&to={end}&token={API_KEY}'
        print(url)
        r = requests.get(url)
        return(r.json())
