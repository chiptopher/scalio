import bcrypt
from flask_restful import Resource, reqparse, request
import re

from scalio.users.model import User
from scalio.util import requtil
from scalio.util.webtoken import build_token

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        email = data['username']
        if not self._is_email(email):
            return None, 400
        if User.find_by_username(email):
            return {}, 400
        new_user = User(
            email=email,
            password=bcrypt.hashpw(str.encode(data['password']), bcrypt.gensalt())
        )
        try:
            return {
                'token': build_token(email)
            }
        except:
            return {}, 500

    def _is_email(self, email: str):
        email_split_on_at = email.split('@')
        if len(email_split_on_at) == 2:
            domain = email_split_on_at[1]
            if domain == 'localhost':
                return True
            domain_split_on_period = domain.split('.')
            if len(domain_split_on_period) == 2:
                return True
            return False
        else:
            return False


class UserLogin(Resource):

    def convert_to_by_if_neccessary(self, password):
        if type(password) is not bytes:
            return password.encode('utf-8')
        else:
            return password

    def post(self):
        data = parser.parse_args()
        user = User.find_by_username(data['username'])
        if not user:
            return {}, 404
        if bcrypt.checkpw(data['password'].encode('utf-8'), self.convert_to_by_if_neccessary(user.password)):
            return {
                'token': build_token(data['username'])
            }
        else:
            return {}, 404


class UserAuthenticationApi(Resource):
    def get(self):
        username = requtil.get_username_from_request(request)
        if username is None or not User.find_by_username(username):
            return None, 401
        else:
            return None, 200
