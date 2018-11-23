import datetime

from scalio.util import webtoken
from test.setup.testcase import TestCase


class UserRegistrationTestCase(TestCase):

    def test_resgister_user(self):
        response = self.app.post('/api/user/register', data=dict(
            username='email@localhost',
            password='password'
        ))
        self.assertEqual(200, response.status_code)
        self.assertEqual('email@localhost', webtoken.get_username_from_token(response.json['token']))

    def test_cannot_register_same_user_twice(self):
        self.app.post('/api/user/register', data=dict(
            username='email@localhost',
            password='password'
        ))
        response = self.app.post('/api/user/register', data=dict(
            username='email@localhost',
            password='password'
        ))
        self.assertEqual(400, response.status_code)


class UserLoginTestCase(TestCase):

    def test_can_login_to_registered_user_with_correct_password(self):
        self.app.post('/api/user/register', data=dict(
            username='email@localhost',
            password='password'
        ))
        response = self.app.post('/api/user/login', data=dict(
            username='email@localhost',
            password='password'
        ))
        self.assertEqual(200, response.status_code)
        self.assertEqual('email@localhost', webtoken.get_username_from_token(response.json['token']))

    def test_cannot_log_into_registered_user_with_incorrect_password(self):
        self.app.post('/api/user/register', data=dict(
            username='email@localhost',
            password='password'
        ))
        response = self.app.post('/api/user/login', data=dict(
            username='email@localhost',
            password='badpassword'
        ))
        self.assertEqual(404, response.status_code)

    def test_cannot_log_into_user_that_is_not_registered(self):
        response = self.app.post('/api/user/login', data=dict(
            username='email@localhost',
            password='password'
        ))
        self.assertEqual(404, response.status_code)


class UserAuthenticatedApiTest(TestCase):

    def test_user_is_authenticated_when_given_a_valid_token(self):
        response = self.app.post('/api/user/register', data=dict(
            username='email@localhost',
            password='password'
        ))
        response = self.app.get('/api/user/authenticated',
                                headers={'Authorization': 'Bearer ' + response.json['token']})
        self.assertEqual(200, response.status_code)

    def test_user_is_non_authenticated_when_given_expired_token(self):
        self.app.post('/api/user/registration', data=dict(
            username='email@localhost',
            password='password'
        ))
        expired_token = webtoken.build_token('email@localhost', datetime.datetime.utcnow() - datetime.timedelta(days=3))
        response = self.app.get('/api/user/authenticated',
                                headers={'Authorization': 'Bearer ' + expired_token})
        self.assertEqual(401, response.status_code)

    def test_user_is_not_authenticated_when_given_a_valid_token_for_a_user_that_does_not_exist(self):
        response = self.app.get('/api/user/authenticated', headers={'Authorization': 'Bearer ' +
                                                                                     webtoken.build_token(
                                                                                         'email@localhost',
                                                                                         datetime.datetime.utcnow())})
        self.assertEqual(401, response.status_code)
