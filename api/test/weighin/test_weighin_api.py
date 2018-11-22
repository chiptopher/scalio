from math import isclose
from decimal import Decimal
import datetime

from test.setup.testcase import TestCase
from test.user import create_user
from scalio.weighin.model import WeighIn
from scalio.util.webtoken import build_token
from scalio.users.model import User
from test.weighin import create_weigh_in_for_user


class WeighInCreate(TestCase):

    @create_user('email@localhost', 'password')
    def test_create_for_user(self):
        headers = {'Authorization': 'Bearer ' + build_token('email@localhost')}

        response = self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers=headers)

        self.assertEqual(201, response.status_code)
        created_weighin = WeighIn.query.all()[0]
        self.assertTrue(isclose(Decimal(201.1), created_weighin.weight))
        self.assertEqual(1514869200000, created_weighin.date)
        self.assertEqual('email@localhost', created_weighin.user.email)

    @create_user('email@localhost')
    def test_cannot_create_weighin_without_token(self):
        headers = {}

        response = self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers=headers)

        self.assertEqual(401, response.status_code)


class AllWeighInsForUser(TestCase):

    @create_user('email@localhost')
    @create_user('email2@localhost')
    @create_weigh_in_for_user(dict(
        weight='201.1',
        date=1514869200000
    ), 'email@localhost')
    def test_get_all_weigh_ins_get_only_weigh_ins_for_user(self):
        # self.app.post('/api/weighin', data=dict(
        #     weight='201.1',
        #     date='2018-01-01'
        # ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email2@localhost')})
        response = self.app.get('/api/weighin', headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json))

    @create_user('email@localhost')
    def test_expired_tokens_are_rejected(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        expiration_time = datetime.datetime.utcnow() - datetime.timedelta(days=4)
        response = self.app.get('/api/weighin')
        self.assertEqual(401, response.status_code)


class GetUserWeighIn(TestCase):

    @create_user('email@localhost')
    def test_can_get_user_weighin(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        created_weigh_in_id = WeighIn.query.all()[0].id
        response = self.app.get('/api/weighin/{}'.format(created_weigh_in_id), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(200, response.status_code)
        self.assertTrue(isclose(Decimal(201.1), response.json['weight']))
        self.assertEqual(1514869200000, response.json['date'])

    @create_user('email@localhost')
    def test_cannot_get_user_weighin_belonging_to_different_user(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        response = self.app.get('/api/weighin/1',
                                headers={'Authorization': 'Bearer ' + build_token('email2@localhost')})
        self.assertEqual(404, response.status_code)

    def test_cannot_make_request_with_malformed_token(self):
        response = self.app.get('/api/weighin/1', headers={'Authorization': 'Bearer ' + 'bad_token'})
        self.assertEqual(401, response.status_code)

    def test_cannot_make_request_with_no_token(self):
        response = self.app.get('/api/weighin/1')
        self.assertEqual(401, response.status_code)

    @create_user('email@localhost')
    def test_cannot_get_weighin_when_user_does_not_exist(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        response = self.app.get('/api/weighin/1',
                                headers={'Authorization': 'Bearer ' + build_token('email2@localhost')})
        self.assertEqual(404, response.status_code)

    @create_user('email@localhost')
    def test_expired_tokens_are_rejected(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        expiration_time = datetime.datetime.utcnow() - datetime.timedelta(days=4)
        response = self.app.get('/api/weighin/1', headers={
            'Authorization': 'Bearer ' + build_token('email@localhost', expiration_time=expiration_time)
        })
        self.assertEqual(401, response.status_code)


class DeleteWeighIn(TestCase):

    @create_user('email@localhost')
    def test_can_delete_user_weighin(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        created_weigh_in_id = WeighIn.query.all()[0].id
        response = self.app.delete('/api/weighin/{}'.format(created_weigh_in_id),
                                   headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(200, response.status_code)
        self.assertEqual(None, WeighIn.find_by_id(1))

    def test_cannot_make_request_with_malformed_token(self):
        response = self.app.delete('/api/weighin/1', headers={'Authorization': 'Bearer ' + 'bad_token'})
        self.assertEqual(401, response.status_code)

    def test_cannot_make_request_with_no_token(self):
        response = self.app.delete('/api/weighin/1')
        self.assertEqual(401, response.status_code)

    @create_user('email@localhost')
    def test_cannot_delete_user_weighin_belonging_to_different_user(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.create_user('email2@localhost')
        response = self.app.delete('/api/weighin/1',
                                   headers={'Authorization': 'Bearer ' + build_token('email2@localhost')})
        self.assertEqual(404, response.status_code)

    @create_user('email@localhost')
    def test_expired_tokens_are_rejected(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        expiration_time = datetime.datetime.utcnow() - datetime.timedelta(days=4)
        response = self.app.delete('/api/weighin/1', headers={
            'Authorization': 'Bearer ' + build_token('email@localhost', expiration_time=expiration_time)
        })
        self.assertEqual(401, response.status_code)


class EditWeighIn(TestCase):

    @create_user('email@localhost')
    def test_can_edit_user_weighin(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        created_weigh_in_id = WeighIn.query.all()[0].id
        response = self.app.post('/api/weighin/{}'.format(created_weigh_in_id), data=dict(
            weight='202.2',
            date=1514869200001
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(200, response.status_code)
        response = self.app.get('/api/weighin/{}'.format(created_weigh_in_id),
                                headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(200, response.status_code)
        self.assertTrue(isclose(Decimal(202.2), response.json['weight']))
        self.assertEqual(1514869200001, response.json['date'])

    def test_cannot_make_request_with_malformed_token(self):
        response = self.app.post('/api/weighin/1', data=dict(
            weight='202.2',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + 'bad_token'})
        self.assertEqual(401, response.status_code)

    def test_cannot_make_request_with_no_token(self):
        response = self.app.post('/api/weighin/1', data=dict(
            weight='202.2',
            date=1514869200000
        ))
        self.assertEqual(401, response.status_code)

    def test_cannot_edit_weighin_when_user_dosent_exist(self):
        response = self.app.post('/api/weighin/1', data=dict(
            weight='202.2',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email2@localhost')})
        self.assertEqual(404, response.status_code)

    def test_cannot_edit_weigh_in_belonging_to_different_user(self):
        self.create_user('email@localhost')
        self.create_user('email2@localhost')
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514782800000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        response = self.app.post('/api/weighin/1', data=dict(
            weight='202.2',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email2@localhost')})
        self.assertEqual(404, response.status_code)
        created_weigh_in_id = WeighIn.query.all()[0].id
        response = self.app.get('/api/weighin/{}'.format(created_weigh_in_id),
                                headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        self.assertEqual(200, response.status_code)
        self.assertTrue(isclose(Decimal(201.1), response.json['weight']))
        self.assertEqual(1514782800000, response.json['date'])

    @create_user('email@localhost')
    def test_expired_tokens_are_rejected(self):
        self.app.post('/api/weighin', data=dict(
            weight='201.1',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost')})
        expiration_time = datetime.datetime.utcnow() - datetime.timedelta(days=4)
        response = self.app.post('/api/weighin/1', data=dict(
            weight='202.2',
            date=1514869200000
        ), headers={'Authorization': 'Bearer ' + build_token('email@localhost', expiration_time=expiration_time)})
        self.assertEqual(401, response.status_code)
