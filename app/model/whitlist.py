import mongoengine


class WhishStock(mongoengine.Document):
    symbol = mongoengine.StringFiled(max_length=4, required=True)
    market_cap = mongoengine.IntField(min_value=0, required=True)
    price = mongoengine.IntField(min_value=0, required=True, default=0)
