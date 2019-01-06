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
        daysFrom = request.args['days']

        username = requtil.get_username_from_request(request)
        user = User.find_by_username(username)

        if not user:
            return None, 400

        end_time = timestamp.time_in_millis(delta=datetime.timedelta(days=int(daysFrom)))

        return {'calculation': user.get_weigh_in_average() - user.get_weigh_in_average(end_time)}, 200