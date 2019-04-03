from scalio.util.webtoken import build_token
from test.setup.testcase import TestCase


class UserSettingsEdit(TestCase):

    def test_can_edit_user_settings(self):
        response = self.create_user('email@localhost')
        headers = {'Authorization': 'Bearer ' + build_token('email@localhost')}
        response = self.app.post('/api/user/settings', data=dict(
            rolling_average_days=4
        ), headers=headers)
        self.assertEqual(200, response.status_code)
        response = self.app.get('/api/user/settings', headers=headers)
        self.assertEqual(4, response.json['rolling_average_days'])

    def test_cannot_edit_settings_for_unregistered_user(self):
        headers = {'Authorization': 'Bearer ' + build_token('email@localhost')}
        response = self.app.post('/api/user/settings', data=dict(
            rolling_average_days=4
        ), headers=headers)
        self.assertEqual(404, response.status_code)


class UserSettingsGet(TestCase):

    def test_can_get_user_settings(self):
        self.create_user('email@localhost')
        headers = {'Authorization': 'Bearer ' + build_token('email@localhost')}
        response = self.app.get('/api/user/settings', headers=headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual(7, response.json['rolling_average_days'])

    def test_cannot_get_settings_for_unregistered_user(self):
        headers = {'Authorization': 'Bearer ' + build_token('email@localhost')}
        response = self.app.get('/api/user/settings', headers=headers)
        self.assertEqual(404, response.status_code)
