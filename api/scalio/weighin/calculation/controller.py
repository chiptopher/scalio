from flask_restful import Resource, request, fields, marshal_with, reqparse
import datetime

from scalio.users.model import User
from scalio.util import requtil, timestamp


class CalculationAverageResource(Resource):

    @marshal_with({
            'average': fields.Float
        })
    def get(self):
        username = requtil.get_username_from_request(request)
        user = User.find_by_username(username)
        return {'average': user.get_weigh_in_average()}, 200


class CalculationOverTimeResource(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('days', required=True)
        args = parser.parse_args()

        username = requtil.get_username_from_request(request)
        user = User.find_by_username(username)

        end_time = timestamp.time_in_millis(delta=datetime.timedelta(days=int(args.days)))

        return {'calculation': user.get_weigh_in_average() - user.get_weigh_in_average(end_time)}, 200