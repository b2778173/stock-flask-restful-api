from mongoengine import *


class Watchlist(Document):
    symbol = StringField(max_length=5, required=False)
    market_cap = IntField(min_value=0, required=False, default=0)
    price = IntField(min_value=0, required=False, default=0)

    meta = {'db_alias': 'good'}

    def add_wishlist(self, symbol):
        print(symbol)
        watchlist = Watchlist(symbol=symbol)
        watchlist.save()

    def remove_wishlist(self, symbol):
        print(f'remove_wishlist symbol = {symbol}')
        watchlist = Watchlist.objects(symbol)
        watchlist.delete()
