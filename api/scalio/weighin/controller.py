from flask_restful import Resource, reqparse, marshal_with
from flask_restful import request

from scalio.users.model import User
from scalio.util import requtil
from scalio.weighin.model import WeighIn

weigh_in_create_reqparser = reqparse.RequestParser()
weigh_in_create_reqparser.add_argument('date', help='This field cannot be blank', required=True)
weigh_in_create_reqparser.add_argument('weight', help='This field cannot be blank', required=True)


class WeighInResource(Resource):

    @marshal_with(WeighIn.resource_fields())
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='This field cannot be blank', required=True)
        username = requtil.get_username_from_request(request)
        if not username:
            return None, 401
        user = User.find_by_username(username)
        return user.weighIns

    def post(self):
        args = weigh_in_create_reqparser.parse_args()
        username = requtil.get_username_from_request(request)
        if not username:
            return None, 401
        user = User.find_by_username(username)
        weighIn = WeighIn(weight=float(args['weight']), date=args['date'])
        user.weighIns.append(weighIn)
        return None, 201


class IndividualWeighIn(Resource):

    @marshal_with(WeighIn.resource_fields())
    def get(self, id):
        username = requtil.get_username_from_request(request)
        if not username:
            return {'error': 'Invalid token format'}, 401
        user = User.find_by_username(username)
        if not user:
            return None, 404
        result = next((weigh_in for weigh_in in user.weighIns if weigh_in.id == id), None)
        if result:
            return result, 200
        else:
            return result, 404

    def delete(self, id):
        username = requtil.get_username_from_request(request)
        if not username:
            return {'error': 'Invalid token format'}, 401
        user = User.find_by_username(username)
        result = next((weigh_in for weigh_in in user.weighIns if weigh_in.id == id), None)
        if result:
            result.remove()
            return None, 200
        else:
            return None, 404

    def post(self, id):
        args = weigh_in_create_reqparser.parse_args()
        username = requtil.get_username_from_request(request)
        if not username:
            return None, 401
        user = User.find_by_username(username)
        if not user:
            return None, 404
        timestamp = args['date']

        found_weigh_in = next((weigh_in for weigh_in in user.weighIns if weigh_in.id == id), None)

        if not found_weigh_in:
            return None, 404

        found_weigh_in.weight = args['weight']
        found_weigh_in.date = timestamp

        weigh_in = WeighIn(weight=args['weight'], date=timestamp)
        user.weighIns.append(weigh_in)
        return None, 200
