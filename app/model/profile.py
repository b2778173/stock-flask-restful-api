from mongoengine import *
from app.model.watchlist import Watchlist
from datetime import datetime
from flask import jsonify
import json


class Address(EmbeddedDocument):
    city = StringField(required=True)
    zip_code = StringField(required=True)
    street = StringField(required=True)


class SocialMedia(EmbeddedDocument):
    facebook_id = StringField(default='fb_id')
    line_id = StringField(default='line_id')


class Watchlist(EmbeddedDocument):
    symbol = StringField(required=True)
    # company_name = StringField(required=True)
    memo = StringField()


class Profile(Document):
    # user_id = StringField(require=False)
    name = StringField(default="???")
    create_time = DateTimeField(default=datetime.now)
    email = EmailField()
    social_media = EmbeddedDocumentField(SocialMedia)
    address = EmbeddedDocumentField(Address)
    watchlist = EmbeddedDocumentListField(Watchlist)

    meta = {'db_alias': 'good'}

    def getAll():
        all = [json.loads(p.to_json()) for p in Profile.objects]
        return jsonify(all)

    def add_profile(name, create_time, email, address, social_media, watchlist):
        print(name, create_time, email, address, social_media, watchlist)
        profile = Profile(name=name, create_time=create_time,
                          email=email, address=address, social_media=social_media, watchlist=watchlist)
        profile.save()
