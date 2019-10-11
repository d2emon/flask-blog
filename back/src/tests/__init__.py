import unittest
import rq
from base64 import b64encode
from app import create_app, db
from config.testing import TestingConfig
from fixtures.category import add_categories
from fixtures.user import add_users
from unittest import mock


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        redis_mock = mock.MagicMock()
        self.app.redis = redis_mock
        self.app.task_queue = rq.Queue('blog-tasks', connection=self.app.redis)

        self.users = list(add_users())
        self.user = self.users[0]
        db.session.add_all(self.users)

        self.categories = list(add_categories())
        db.session.add_all(self.categories)

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
