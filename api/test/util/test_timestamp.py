import unittest
from scalio.util import timestamp


class TimestampTest(unittest.TestCase):

    def test_convert_date_to_timestamp_covnerts_yyyy_mm_dd_to_millis_from_epoch(self):
        self.assertEqual(1514782800000, timestamp.convert_date_to_timestamp('2018-01-01'))