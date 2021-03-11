from mongoengine import Document
from flask import jsonify
import json
from mongoengine.fields import *

# 2021/03/11 deprecate
class Watchlist(Document):
    symbol = StringField(max_length=5, required=True,  primary_key=True)
    company_name = StringField(required=True)
    market_cap = IntField(min_value=0, required=False, default=0)
    price = IntField(min_value=0, required=False, default=0)

    meta = {'db_alias': 'good'}

    def get_wishlist():
        result = []
        for w in Watchlist.objects():
            print('w=', w)
            # mongoengine provide to_json()
            result.append(json.loads(w.to_json()))
            print('result=', result)
        return jsonify(result)

    def add_wishlist(symbol, market_cap, price):
        print(symbol, market_cap, price)
        # model insert need use kwargs*
        watchlist = Watchlist(
            symbol=symbol, market_cap=market_cap, price=price)
        watchlist.save()

    def remove_wishlist(symbol):
        print(f'remove_wishlist symbol = {symbol}')
        watchlist = Watchlist.objects.with_id(symbol)
        print('watchlist=', watchlist)
        if not (watchlist):
            print('watchlist not found')
            # raise Exception('watchlist not found')
        else:
            watchlist.delete()
