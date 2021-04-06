from flask import request, Flask, current_app
from flask_restful import Resource, reqparse
from app.model.profile import Profile as ProfileModel
from flask_jwt import jwt_required, current_identity
from flask_mail import Mail, Message
import logging
import json


logging.basicConfig(filename='example.log', level=logging.DEBUG)


class User(Resource):
    """ validation """
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name', type=str, required=True, help='name {error_msg}'
    )
    parser.add_argument(
        'password', min, type=str, required=True, help='password {error_msg}'
    )
    parser.add_argument(
        'email', type=str, required=True, help='email {error_msg}'
    )
    parser.add_argument(
        'create_time', required=False, help='create_time {error_msg}'
    )
    parser.add_argument(
        'address', required=False, help='address {error_msg}'
    )
    parser.add_argument(
        'social_media', required=False, help='social_media {error_msg}'
    )
    parser.add_argument(
        'watchlist', required=False, help='watchlist {error_msg}'
    )

    """ get user detail """

    def get(self, username):
        logging.debug('username', username)
        try:

            user = ProfileModel.get_by_username(username)
            if not user:
                return {'message': 'user not found'}, 404
            return {'result': user}, 200

        except Exception as e:
            return {'error': f'get {username} fail, error: {e}'}, 400

    """ create a user"""

    def post(self, username):
        logging.debug(request.get_json())

        data = User.parser.parse_args()
        data['address'] = data['address'].replace("'", '"')
        data['social_media'] = data['social_media'].replace("'", '"')
        data['watchlist'] = data['watchlist'].replace("'", '"')
        print('data55555555555555', data)

        password = data['password']
        name = data['name']
        create_time = data['create_time']
        email = data['email']
        # address = json.loads(data['address'])
        # social_media = json.loads(data['social_media'])
        # watchlist = json.loads(data['watchlist'])
        # password = request.get_json().get('password')
        # name = request.get_json().get('name')
        # create_time = request.get_json().get('create_time')
        # email = request.get_json().get('email')
        address = request.get_json().get('address')
        social_media = request.get_json().get('social_media')
        watchlist = request.get_json().get('watchlist')
        logging.debug('create a user params',username, create_time, email, social_media, watchlist)
        try:
            user = ProfileModel.get_by_username(username)
            if user:
                return {'error': 'user already exist'}, 404

            response = ProfileModel.create_profile(self, username, password, name, create_time,
                                                   email, address, social_media, watchlist)
            logging.debug(f'create {username} success')
            return response, 201
        except Exception as e:
            logging.debug(f'insert fail, error: {e}')
            return {'error': f'create {username} fail, error: {e}'}, 400

    """ update a user"""
    @jwt_required()
    def put(self, username):
        logging.debug(request.get_json())
        name = request.get_json().get('name')
        email = request.get_json().get('email')
        address = request.get_json().get('address')
        social_media = request.get_json().get('social_media')
        watchlist = request.get_json().get('watchlist')
        logging.debug(username, name, email, social_media, watchlist)

        try:
            user = ProfileModel.get_by_username(username)
            logging.debug(username, user)
            if not user:
                return {'error': 'user not found'}, 404

            response = ProfileModel.update_profile(self, username, name,
                                                   email, address, social_media, watchlist)

            logging.debug(f'update {username} success')
            return {'message': response}, 201
        except Exception as e:
            logging.debug(f'update fail, error: {e}')
            return {'error': f'update {username} fail, error: {e}'}, 400


class getUserList(Resource):
    @jwt_required()
    def get(self):
        return ProfileModel.getAll()


class getCurrentUser(Resource):
    @jwt_required()
    def get(self):
        profile: ProfileModel = current_identity
        return profile.get_current_profile()


class ChangePassword(Resource):
    @jwt_required()
    def post(self, username):
        logging.debug(self)
        logging.debug(request.get_json())
        password = request.get_json().get('password')
        logging.debug(username, password)

        try:
            response = ProfileModel.change_password(self, username, password)
            logging.debug(f"change {username}'s password success")
            return response, 201
        except Exception as e:
            logging.debug(f'update fail, error: {e}')
            return {'error': f'change {username} password fail, error: {e}'}, 400


class SendMail(Resource):
    @staticmethod
    def post(user):
        app = Flask(__name__)
        app.config.update(
            MAIL_SERVER='smtp.gmail.com',
            MAIL_PROT=587,
            MAIL_USE_TLS=True,
            MAIL_USERNAME=current_app.config["E_MAIL"],
            MAIL_PASSWORD=current_app.config["MAIL_APPLICATION_PASSWORD"]
        )
        #  記得先設置參數再做實作mail
        mail = Mail(app)
        #  主旨
        msg_title = 'Hello It is Flask-Mail'
        #  收件者，格式為list，否則報錯
        msg_recipients = [user]
        #  郵件內容
        msg_body = 'Hey, I am mail body!'
        #  也可以使用html
        #  msg_html = '<h1>Hey,Flask-mail Can Use HTML</h1>'
        msg = Message(msg_title, sender=user, recipients=msg_recipients)
        msg.body = msg_body
        #  msg.html = msg_html

        #  mail.send:寄出郵件
        with app.app_context():
            mail.send(msg)

        return 'You Send Mail by Flask-Mail Success!!'
