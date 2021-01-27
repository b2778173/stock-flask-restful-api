from flask import Flask, request
from flask_restful import Resource, Api
import requests
from resources.stock import Stock
from resources.stock import News
from resources.stock import CompanyNews

app = Flask(__name__)
# Load the default configuration
app.config.from_object('config.dev')
api = Api(app)


api.add_resource(Stock, '/stock')
api.add_resource(News, '/news')
api.add_resource(CompanyNews, '/company-news')

if __name__ == '__main__':
    app.run()
