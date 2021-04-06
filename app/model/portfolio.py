
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import DateTimeField, EmbeddedDocumentListField, FloatField, IntField, StringField
from flask import jsonify
import json
from datetime import datetime


class History(EmbeddedDocument):
    quantity = IntField(required=True)
    trade_time = DateTimeField(default=datetime.now)
    trade_price = FloatField(min_value=0, required=True)


class Portfolio(Document):
    symbol = StringField(required=True, primary_key=True)
    company_name = StringField(Required=True)
    history = EmbeddedDocumentListField(History, default=[])
    trade_time = DateTimeField(default=datetime.now)
    trade_price = FloatField(min_value=0, required=True)
    market_price = IntField(min_value=0, required=True)
    profit = IntField(required=True)
    profit_percentage = FloatField()
    memo = StringField()
    user_id = StringField(required=True)

    meta = {'db_alias': 'good'}

    def getPortfolioList(user_id):
        all = []
        for p in Portfolio.objects(user_id=user_id):
            portfolioObj = json.loads(p.to_json())
            print('portfolioObj', portfolioObj)
            all.append(portfolioObj)
        return all

    def insertPortfolio(self, symbol, company_name, history, trade_time, trade_price, market_price, profit, profit_percentage, memo, user_id):
        portfolio = Portfolio(symbol=symbol, company_name=company_name, history=history, trade_time=trade_time, trade_price=trade_price,
                              market_price=market_price, profit=profit, profit_percentage=profit_percentage, memo=memo, user_id=user_id)
        response = Portfolio.objects.insert(portfolio, load_bulk=False)
        return {'message': f'{response} add portfolio success'}
