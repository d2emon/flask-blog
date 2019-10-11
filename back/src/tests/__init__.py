import unittest
from base64 import b64encode
from app import create_app, db
from config.testing import TestingConfig
from fixtures.user import add_users


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.users = list(add_users())
        self.user = self.users[0]
        db.session.add_all(self.users)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @classmethod
    def basic_auth(cls, username, password):
        auth = username + ':' + password
        return "Basic {}".format(b64encode(auth.encode('utf-8')).decode('utf-8'))

    @classmethod
    def bearer_auth(cls, token):
        return "Bearer {}".format(token)
