from scalio.users.model import User
from scalio.weighin.model import WeighIn
from test.setup.testcase import TestCase
from scalio.util.timestamp import convert_date_to_timestamp, time_in_millis

import datetime


class TestUser(TestCase):

    def test_user_created_with_user_settings_rolling_average_of_7(self):
        user = User(email='email@localhost', password='password')
        self.assertEqual(7, user.user_settings.rolling_average_days)

    def test_user_get_weigh_in_average_calculates_the_average_from_the_current_time(self):
        user = User(email='email@localhost', password='password')
        weighIn1 = WeighIn(weight=float(100), date=time_in_millis())
        weighIn2 = WeighIn(weight=float(200), date=time_in_millis(delta=datetime.timedelta(days=6)))
        user.weighIns.append(weighIn1)
        user.weighIns.append(weighIn2)
        self.assertEqual(150.0, user.get_weigh_in_average())

    def test_user_get_weigh_in_average_calculates_the_average_from_a_given_time(self):
        user = User(email='email@localhost', password='password')
        weighIn1 = WeighIn(weight=float(100), date=convert_date_to_timestamp('2018-01-01'))
        weighIn2 = WeighIn(weight=float(200), date=convert_date_to_timestamp('2018-01-07'))
        weighIn3 = WeighIn(weight=float(300), date=time_in_millis())
        user.weighIns.append(weighIn1)
        user.weighIns.append(weighIn2)
        user.weighIns.append(weighIn3)
        self.assertEqual(150.0, user.get_weigh_in_average(convert_date_to_timestamp('2018-01-07')))

    def test_get_weigh_in_averages_over_time_from_given_date_to_the_beginning_of_time(self):
        user = User(email='email@localhost', password='password')
        weighIn1 = WeighIn(weight=float(100), date=convert_date_to_timestamp('2018-01-01'))
        weighIn2 = WeighIn(weight=float(200), date=convert_date_to_timestamp('2018-01-07'))
        weighIn3 = WeighIn(weight=float(300), date=convert_date_to_timestamp('2018-01-20'))
        user.weighIns.append(weighIn1)
        user.weighIns.append(weighIn2)
        user.weighIns.append(weighIn3)
        expected = [
            dict(weight=300.0, date=convert_date_to_timestamp('2018-01-20')),
            dict(weight=0, date=convert_date_to_timestamp('2018-01-19')),
            dict(weight=0, date=convert_date_to_timestamp('2018-01-18')),
            dict(weight=0, date=convert_date_to_timestamp('2018-01-17')),
            dict(weight=0, date=convert_date_to_timestamp('2018-01-16')),
            dict(weight=0, date=convert_date_to_timestamp('2018-01-15')),
            dict(weight=0, date=convert_date_to_timestamp('2018-01-14')),
            dict(weight=200.0, date=convert_date_to_timestamp('2018-01-13')),
            dict(weight=200.0, date=convert_date_to_timestamp('2018-01-12')),
            dict(weight=200.0, date=convert_date_to_timestamp('2018-01-11')),
            dict(weight=200.0, date=convert_date_to_timestamp('2018-01-10')),
            dict(weight=200.0, date=convert_date_to_timestamp('2018-01-9')),
            dict(weight=200.0, date=convert_date_to_timestamp('2018-01-8')),
            dict(weight=150.0, date=convert_date_to_timestamp('2018-01-7')),
            dict(weight=100.0, date=convert_date_to_timestamp('2018-01-6')),
            dict(weight=100.0, date=convert_date_to_timestamp('2018-01-5')),
            dict(weight=100.0, date=convert_date_to_timestamp('2018-01-4')),
            dict(weight=100.0, date=convert_date_to_timestamp('2018-01-3')),
            dict(weight=100.0, date=convert_date_to_timestamp('2018-01-2')),
            dict(weight=100.0, date=convert_date_to_timestamp('2018-01-1')),
        ]
        result = user.get_weigh_in_averages_over_time(convert_date_to_timestamp('2018-01-20'))
        self.assertListEqual(expected, result)
