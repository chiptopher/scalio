from flask_restful import Resource, request, fields, marshal_with

from scalio.users.model import User
from scalio.util import requtil


class CalculationAverageResource(Resource):

    @marshal_with({
            'average': fields.Float
        })
    def get(self):
        username = requtil.get_username_from_request(request)
        user = User.find_by_username(username)
        return {'average': user.get_weigh_in_average()}, 200
