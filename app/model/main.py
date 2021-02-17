import mongoengine
from pymongo import ReadPreference


def azure():
    mongoengine.register_connection(
        alias='good',
        db='stock_flask_api_db',
        host='testapidb.mongo.cosmos.azure.com',
        port=10255,
        username='testapidb',
        password='XDKcnIL9dBEUVPecyyCeTPvdrtsuPMK1PFXQTe6iQx9FaoPzFqAgrWPUl9umCYfU3XStuTGXXBlY1oQyIFy7Mg==',
        ssl=True,
        retrywrites=False
    )


def setup():
    print('connection setup')
    mongoengine.connect(
        'stock_flask_api_db',
        alias='good',
        host='mongodb+srv://b2778173:a2765811@cluster0.4scm7.mongodb.net/stock_flask_api_db?retryWrites=true&w=majority'
    )
