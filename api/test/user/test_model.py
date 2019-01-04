from scalio.users.model import User
from test.setup.testcase import TestCase
from scalio.weighin.model import WeighIn
from scalio.util import timestamp
import datetime


class TestUser(TestCase):

    def test_user_created_with_user_settings_rolling_average_of_7(self):
        user = User(email='email@localhost', password='password')
        self.assertEqual(7, user.user_settings.rolling_average_days)

    def test_user_get_weigh_in_average_defaults_to_now(self):
        user = User(email='email@localhost', password='password')
        weigh_in_1 = WeighIn(weight=100.0, date=timestamp.time_in_millis())
        weigh_in_2 = WeighIn(weight=200.0, date=timestamp.time_in_millis())
        user.weighIns.append(weigh_in_1)
        user.weighIns.append(weigh_in_2)
        self.assertAlmostEqual(150.0, user.get_weigh_in_average(), .001)

    def test_get_weigh_in_average_ignores_dates_outside_of_rolling_average_range(self):
        user = User(email='email@localhost', password='password')
        weigh_in_1 = WeighIn(weight=100.0, date=timestamp.time_in_millis())
        weigh_in_2 = WeighIn(weight=200.0, date=timestamp.time_in_millis(
            delta=datetime.timedelta(days=user.user_settings.rolling_average_days + 1)))
        user.weighIns.append(weigh_in_1)
        user.weighIns.append(weigh_in_2)
        self.assertAlmostEqual(100.0, user.get_weigh_in_average(), .001)

    def test_get_weigh_in_average_can_be_calculated_from_a_given_date(self):
        user = User(email='email@localhost', password='password')
        weigh_in_1 = WeighIn(weight=100.0, date=timestamp.time_in_millis())
        weigh_in_2 = WeighIn(weight=200.0, date=timestamp.time_in_millis(
            delta=datetime.timedelta(days=8)))
        user.weighIns.append(weigh_in_1)
        user.weighIns.append(weigh_in_2)
        self.assertAlmostEqual(200.0, user.get_weigh_in_average(timestamp.time_in_millis(delta=datetime.timedelta(days=8))))
