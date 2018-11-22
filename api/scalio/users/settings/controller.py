from flask_restful import Resource, request, reqparse, marshal_with
from scalio.util import requtil
from scalio.users.model import User
from scalio.users.settings.model import UserSettings

edit_settings_parser = reqparse.RequestParser()
edit_settings_parser.add_argument('rolling_average_days', help='Cannot be empty', required=True)


class IndividualSettingsApi(Resource):

    def post(self):
        data = edit_settings_parser.parse_args()
        username = requtil.get_username_from_request(request)
        if not username:
            return None, 400
        user = User.find_by_username(username)
        if not user:
            return None, 404
        user.user_settings.rolling_average_days = data['rolling_average_days']
        return None, 200

    @marshal_with(UserSettings.resource_fields())
    def get(self):
        username = requtil.get_username_from_request(request)
        if not username:
            return None, 400
        user = User.find_by_username(username)
        if not user:
            return None, 404
        return user.user_settings
