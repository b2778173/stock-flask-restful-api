from flask import Flask, request, current_app, Blueprint
from flask.globals import current_app
from flask_restful import Resource
import requests
import finnhub
from datetime import datetime


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


class Stock(Resource):
    def get(self):
        API_KEY = current_app.config["API_KEY"]
        finnhub_client = finnhub.Client(api_key=API_KEY)
        symbol = (request.args.get('symbol'))
        r = finnhub_client.symbol_lookup(symbol)
        return r


class Stock_candle(Resource):
    def get(self):
        API_KEY = current_app.config["API_KEY"]
        finnhub_client = finnhub.Client(api_key=API_KEY)
        symbol = (request.args.get('symbol'))
        resolution = (request.args.get('resolution'))
        _from = (request.args.get('from'))
        to = (request.args.get('to'))
        response = finnhub_client.stock_candles(
            symbol, resolution, _from, to)
        if response['s'] == 'no_data':
            return None
        else:
            return self.formatResponse(t=response['t'], c=response['c'], o=response['o'], h=response['h'], l=response['l'], v=response['v'])

    def formatResponse(self, t, c, o, h, l, v):
        # print(t, c)
        result = []
        for idx, date in enumerate(t):
            format_date = datetime.utcfromtimestamp(
                date).strftime('%Y-%m-%d')
            result.append({
                'date': date * 1000,
                'open': o[idx],
                'height': h[idx],
                'volumn': v[idx],
                'close': c[idx]
            })
        return result


class Day_mover(Resource):
    def get(self):
        start = (request.args.get('start'))
        count = (request.args.get('count'))
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-movers"
        headers = {
            'x-rapidapi-key': "5e1711a842mshcdc573475e2a4f1p173affjsnee500c8bd126",
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        querystring = {"region":"US","lang":"en-US","start":start,"count":count}
        r = requests.get(url, headers=headers, params=querystring)
        return r.json()

class Quote(Resource):
    def get(self):
        API_KEY = current_app.config["API_KEY"]
        finnhub_client = finnhub.Client(api_key=API_KEY)
        symbol = (request.args.get('category'))
        r = finnhub_client.quote(symbol)
        return r
    def post(self):
        all = []
        API_KEY = current_app.config["API_KEY"]
        finnhub_client = finnhub.Client(api_key=API_KEY)
        symbols = request.get_json().get('symbols')
        for s in symbols:
            r = finnhub_client.quote(s)
            all.append(r)
        return all

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
        print(begin, end)
        r = finnhub_client.company_news(symbol, _from=begin, to=end)
        return r
