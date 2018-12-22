from flask_restful import Resource, request
from scalio.util import requtil
from scalio.users.model import User


class AveragesListApi(Resource):

    def get(self):
        username = requtil.get_username_from_request(request)
        user = User.find_by_username(username)
        return user.get_weigh_in_averages_over_time(), 200
