from mongoengine import *
from app.model.watchlist import Watchlist
from datetime import datetime
from flask import jsonify
import json
from bson.objectid import ObjectId


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
        # all = [json.loads(p.to_json()) for p in Profile.objects]
        all = []
        for p in Profile.objects:
            profileJSON = json.loads(p.to_json())
            objectId = (profileJSON['_id'])['$oid'] 
            profileJSON['_id'] = str(ObjectId(objectId))
            # print(ObjectId(objectId))
            all.append(profileJSON)
            # print(json.loads(p.to_json())['_id']['$oid'])
            # print(ObjectId("543b591d91b9e510a06a42e2"))

        return jsonify(all)

    def add_profile(name, create_time, email, address, social_media, watchlist):
        print(name, create_time, email, address, social_media, watchlist)
        profile = Profile(name=name, create_time=create_time,
                          email=email, address=address, social_media=social_media, watchlist=watchlist)
        profile.save()
