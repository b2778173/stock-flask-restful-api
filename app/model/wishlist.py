import mongoengine


class Wishlist(mongoengine.Document):
    symbol = mongoengine.StringField(max_length=5, required=True)
    market_cap = mongoengine.IntField(min_value=0, required=False, default=0)
    price = mongoengine.IntField(min_value=0, required=False, default=0)

    meta = {'db_alias': 'good'}

    def add_wishlist(symbol):
        wishlist = Wishlist(symbol=symbol)
        wishlist.save()

    def remove_wishlist(symbol):
        print(f'add_wishlist symbol = {symbol}')
        wishlist = Wishlist.objects(symbol=symbol)
        wishlist.delete()
