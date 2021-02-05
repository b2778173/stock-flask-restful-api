import mongoengine



def setup():
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



