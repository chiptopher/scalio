import unittest
from scalio.util import webtoken
import jwt
import datetime
from datetime import timezone


def current_millis():
    return datetime.datetime.utcnow()


class WebtokenTest(unittest.TestCase):

    def test_build_token(self):
        token = webtoken.build_token('email@localhost')
        result = jwt.decode(token, verify=False)
        self.assertEqual('email@localhost', result['sub'])
        expected_datetime = (current_millis() + datetime.timedelta(days=2))
        self.assertAlmostEqual(expected_datetime.replace(tzinfo=timezone.utc).timestamp(), result['exp'], -2)

    def test_decode_token(self):
        self.assertEqual('email@localhost', webtoken.get_username_from_token(webtoken.build_token('email@localhost')))

    def test_get_username_from_token_wont_decode_expired_tokens(self):
        try:
            eight_days_ago = current_millis() - datetime.timedelta(days=8)
            token = webtoken.build_token('email@localhost', expiration_time=eight_days_ago)
            webtoken.get_username_from_token(token)
            self.fail("Shouldn't be able to parse jwt.")
        except webtoken.InvalidWebtokenError:
            pass
