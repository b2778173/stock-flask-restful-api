from app import db


class Stock(db.model):
    id = db.Clolumn(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
