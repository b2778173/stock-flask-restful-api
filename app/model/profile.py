from mongoengine import *
from app.model.watchlist import Watchlist
from datetime import datetime
from flask import jsonify
import json




class Profile(Document):
    user_id = StringField(require=False, primary_key=True)
    name = StringField(default="???")
    create_time = DateTimeField(default=datetime.now)
    email = EmailField()
    facebook_id = StringField()
    line_id = StringField(default='line')
    # watchlist = EmbeddedDocumentField(Watchlist)

    meta = {'db_alias': 'good'}
    def getAll():
        all = [json.loads(p.to_json()) for p in Profile.objects]
        return jsonify(all)

    def add_profile( user_id, name, create_time, email, facebook_id, line_id):
        print(user_id, name, create_time, email, facebook_id, line_id)
        profile = Profile(user_id=user_id, name=name, create_time=create_time,
                          email=email, facebook_id=facebook_id, line_id=line_id)
        profile.save()
