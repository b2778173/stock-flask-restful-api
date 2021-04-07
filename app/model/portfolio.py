
from bson.json_util import default
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import DateTimeField, EmbeddedDocumentListField, FloatField, IntField, StringField
from flask import jsonify
import json
from datetime import datetime
from mongoengine.queryset.visitor import Q



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
    market_price = FloatField(min_value=0, required=True)
    profit = FloatField(default=0)
    profit_percentage = FloatField(default=0)
    memo = StringField()
    user_id = StringField(required=True)

    meta = {'db_alias': 'good'}

    def find(user_id):
        all = []
        for p in Portfolio.objects(user_id=user_id):
            portfolioObj = json.loads(p.to_json())
            all.append(portfolioObj)
        return all

    def insert(self, symbol, company_name, history, trade_time, trade_price, market_price, memo, user_id):
        portfolio = Portfolio(symbol=symbol, company_name=company_name, history=history, trade_time=trade_time, trade_price=trade_price,
                              market_price=market_price, memo=memo, user_id=user_id)
        response = Portfolio.objects.insert(portfolio, load_bulk=False)
        return f'{response} add portfolio success'

    def delete(user_id, symbol):
        print('2222222222222', user_id, symbol)
        portfolio = Portfolio.objects(Q(user_id=user_id)& Q(symbol=symbol)).all()
        print('11111', portfolio)
        if not portfolio:
            return f'portfolio symbol: {symbol} not found'
        portfolio.delete()
        return f'delete_portfolio symbol: {symbol} success'
