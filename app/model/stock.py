import mongoengine

class Stock(mongoengine.Document):
    id = mongoengine.IntField()
    name = mongoengine.StringFiled()
    market_cap = mongoengine.IntField()

    meta = {'db_alias': 'good'}