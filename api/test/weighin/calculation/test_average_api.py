import datetime

from scalio.util.timestamp import time_in_millis
from scalio.util.webtoken import build_token
from test.setup.testcase import TestCase
from test.user import create_user
from test.weighin import create_weigh_in_for_user


class CalculationResourceApiTest(TestCase):

    @create_user('email@localhost')
    @create_weigh_in_for_user(dict(
        weight='100.0',
        date=time_in_millis()
    ), 'email@localhost')
    @create_weigh_in_for_user(dict(
        weight='200.0',
        date=time_in_millis()
    ), 'email@localhost')
    def test_calculate_average(self):
        response = self.app.get('/api/weighin/calculation/average',
                                headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(200, response.status_code)
        self.assertEqual(150.0, response.json['average'])

    @create_user('email@localhost')
    def test_calculate_average_handles_zero_weighins(self):
        response = self.app.get('/api/weighin/calculation/average',
                                headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json['average'])

    @create_user('email@localhost')
    @create_weigh_in_for_user(dict(
        weight='100.0',
        date=time_in_millis(delta=datetime.timedelta(days=8))
    ), 'email@localhost')
    def test_calculate_average_only_accounts_for_weigh_ins_in_users_timeframe(self):
        response = self.app.get('/api/weighin/calculation/average',
                                headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(0, response.json['average'])
