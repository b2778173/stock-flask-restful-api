from flask import Flask, request
from flask_restful import Resource
import requests
from app.config import config

app = Flask(__name__)
# Load the default configuration
app.config.from_object(config)
API_KEY = (app.config["API_KEY"])
FINNHUB_BASE_URL = (app.config["FINNHUB_BASE_URL"])


class Stock(Resource):
    def get(self):
        symbol = (request.args.get('symbol'))
        r = requests.get(
            f'{FINNHUB_BASE_URL}/search?q={symbol}&token={API_KEY}')
        return(r.json())


class News(Resource):
    def get(self):
        category = (request.args.get('category'))
        minId = (request.args.get('minId'))
        url = f'{FINNHUB_BASE_URL}/news?category={category}&token={API_KEY}'
        if minId != None:
            url += f"&{minId}"
        r = requests.get(url)
        return(r.json())


class CompanyNews(Resource):
    def get(self):
        symbol = (request.args.get('symbol'))
        begin = (request.args.get('from'))
        end = (request.args.get('to'))
        url = f'{FINNHUB_BASE_URL}/company-news?symbol={symbol}&from={begin}&to={end}&token={API_KEY}'
        print(url)
        r = requests.get(url)
        return(r.json())
