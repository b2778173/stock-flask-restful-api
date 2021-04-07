from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import DateTimeField, EmailField, EmbeddedDocumentField, EmbeddedDocumentListField, StringField
from app.model.watchlist import Watchlist
from datetime import datetime
from flask import jsonify
import json
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


class Address(EmbeddedDocument):
    city = StringField(required=True)
    zip_code = StringField(required=True)
    street = StringField(required=True)


class SocialMedia(EmbeddedDocument):
    facebook_id = StringField(default='fb_id')
    line_id = StringField(default='line_id')


class Watchlist(EmbeddedDocument):
    symbol = StringField(required=True)
    memo = StringField()


class Profile(Document):
    user_id = StringField(require=False)
    username = StringField(max_length=128, required=True)
    password_hash = StringField(max_length=128, required=True)
    name = StringField(default="???", required=True)
    create_time = DateTimeField(default=datetime.now)
    email = EmailField()
    social_media = EmbeddedDocumentField(SocialMedia, default={})
    address = EmbeddedDocumentField(Address, default={})
    watchlist = EmbeddedDocumentListField(Watchlist, default=[])

    meta = {'db_alias': 'good'}

    """to dict obj"""

    def to_dict(self):
        return {
            "_id": str(self.pk),
            "username": self.username,
            "password_hash": self.password_hash,
            "name": self.name,
            "create_time": self.create_time.timestamp(),
            "email": self.email,
            "social_media": self.social_media,
            "address": self.address,
            "watchlist": self.watchlist,
        }

    """json format """

    def json_format(self):
        profileJSON = json.loads(self.to_json())
        profileJSON['_id'] = str(self.pk)
        profileJSON['create_time'] = (self.create_time).timestamp()
        # del profileJSON['password_hash']
        return profileJSON

    def get_current_profile(self):
        return {
            "_id": str(self.pk),
            "username": self.username,
        }
    """get user list"""
    def getAll():
        # all = [json.loads(p.to_json()) for p in Profile.objects]
        all = []
        for p in Profile.objects:
            all.append(p.json_format())
        return all

    """create_profile"""

    def create_profile(self, username, password, name, create_time, email, address, social_media, watchlist):
        print(username, password, email,
              address, social_media, watchlist)
        password_hash = Profile.set_password(self, password)
        profile = Profile(username=username, password_hash=password_hash, name=name, create_time=create_time,
                          email=email, address=address, social_media=social_media, watchlist=watchlist)
        profile.save()
        return {'message': f'{username} create success'}

    """update profile"""

    def update_profile(self, username, name, email, address, social_media, watchlist):
        profile = Profile.objects(username=username).first()

        if name:
            profile.name = name
        if email:
            profile.email = email
        if address:
            profile.address = address
        if social_media:
            profile.social_media = social_media
        if watchlist:
            result = []
            for w in watchlist:
                w1 = Watchlist(symbol=w['symbol'], memo=w['memo'])
                result.append(w1)
                print('result=', result)
            profile.watchlist = result
        profile.save()
        return f'{username} update success'

    def change_password(self, username, password):
        profile: Profile = Profile.objects(username=username).first()
        profile.set_password(profile, password)
        profile.save()
        return 'change password success'

    @staticmethod
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        print('generate_password_hash=', generate_password_hash(password))
        return self.password_hash

    def check_password(self, password):
        return check_password_hash(self['password_hash'], password)

    @staticmethod
    def authenticate(username, password):
        user = Profile.objects(username=username).first()
        if user:
            if user.check_password(password):
                # 將mongo pk objectId type轉為string
                user.pk = str(user.pk)
                return user

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        # print('user_id', user_id)
        user = Profile.objects(id=user_id).first()
        # print('user identity', user)
        if user:
            user.pk = str(user.pk)
        return user

    @staticmethod
    def get_by_username(username):
        user: Profile = Profile.objects(username=username).first()
        print(user)
        if user:
            return (user.json_format())
        else:
            return user
