from mongoengine import Document
from mongoengine.fields import *
from datetime import datetime



class Comment(Document):
    company_name = StringField()
    create_time = DateTimeField(default=datetime.now)
    reply = StringField()
    emoji = StringField()
    views = IntField()


class Stock(Document):
    symbol = IntField(primary_key=True, require=True)
    company_name = StringField(require=True)
    comment = EmbeddedDocumentField(Comment, default=[])

    meta = {'db_alias': 'good'}
