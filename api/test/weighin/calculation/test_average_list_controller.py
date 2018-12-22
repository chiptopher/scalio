from test.setup.testcase import TestCase
from test.user import create_user
from test.weighin import create_weigh_in_for_user
from scalio.util.webtoken import build_token
from scalio.util.timestamp import time_in_millis

import datetime

class AverageListApiTest(TestCase):

    @create_user('email@localhost')
    @create_weigh_in_for_user(dict(
        weight='100.0',
        date=time_in_millis(),
    ), 'email@localhost')
    def test_list_of_rolling_averages_endpoint_exists(self):
        response = self.app.get('/api/weighin/calculation/list',
                                headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(200, response.status_code)

    @create_user('email@localhost')
    @create_weigh_in_for_user(dict(
        weight='100.0',
        date=time_in_millis(delta=datetime.timedelta(days=1))
    ), 'email@localhost')
    @create_weigh_in_for_user(dict(
        weight='200.0',
        date=time_in_millis(delta=datetime.timedelta(days=0))
    ), 'email@localhost')
    def test_list_of_averages_gets_all_of_them_over_time(self):
        response = self.app.get('/api/weighin/calculation/list',
                                headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(150.0, response.json[0].weight)
        self.assertEqual(time_in_millis(delta=datetime.timedelta(days=0)), response.json[0].date)
        self.assertEqual(100.0, response.json[1].weight)
        self.assertEqual(time_in_millis(delta=datetime.timedelta(days=1)), response.json[1].date)
