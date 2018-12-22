import datetime
import unittest

from scalio.util import timestamp


class TimestampTest(unittest.TestCase):

    def test_convert_date_to_timestamp_covnerts_yyyy_mm_dd_to_millis_from_epoch(self):
        self.assertEqual(1514764800000, timestamp.convert_date_to_timestamp('2018-01-01'))

    def test_time_in_millis_gets_the_time_from_the_given_date(self):
        date = datetime.datetime(year=2018, month=1, day=2)
        delta = datetime.timedelta(days=1)
        self.assertEqual(1514782800000, timestamp.time_in_millis(date, delta))
