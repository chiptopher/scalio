from flask_restful import Resource, reqparse, request
from scalio.users.model import User
import bcrypt
from scalio.util.webtoken import build_token
from scalio.util import requtil

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        if User.find_by_username(data['username']):
            return {}, 400
        new_user = User(
            email=data['username'],
            password=bcrypt.hashpw(str.encode(data['password']), bcrypt.gensalt())
        )
        try:
            return {
                'token': build_token(data['username'])
            }
        except:
            return {}, 500


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
