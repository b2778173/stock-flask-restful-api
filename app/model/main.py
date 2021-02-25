import mongoengine


def azure(password):
    mongoengine.register_connection(
        alias='good',
        db='stock_flask_api_db',
        host='testapidb.mongo.cosmos.azure.com',
        port=10255,
        username='testapidb',
        password=password,
        ssl=True,
        retrywrites=False
    )
# local db


def setup(host):
    mongoengine.connect(
        'stock_flask_api_db',
        alias='good',
        host=host
    )
