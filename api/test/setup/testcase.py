import unittest

from scalio.app import app
from scalio.app import db


class TestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.app.get('/api')
        for tbl in reversed(db.metadata.sorted_tables):
            db.engine.execute(tbl.delete())

    def tearDown(self):
        for tbl in reversed(db.metadata.sorted_tables):
            db.engine.execute(tbl.delete())

    def create_user(self, username: str, password: str = 'password'):
        return self.app.post('/api/user/register', data=dict(
            username=username,
            password=password
        ))