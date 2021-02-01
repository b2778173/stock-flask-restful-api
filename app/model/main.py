import mongoengine


def setup():
    mongoengine.register_connection(
        alias='good',
        db='test',
        host: "testapidb.mongo.cosmos.azure.com",
        port=10255
    )
