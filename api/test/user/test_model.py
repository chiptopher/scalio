from scalio.users.model import User
from test.setup.testcase import TestCase


class TestUser(TestCase):

    def test_user_created_with_user_settings_rolling_average_of_7(self):
        user = User(email='email@localhost', password='password')
        self.assertEqual(7, user.user_settings.rolling_average_days)
