import unittest
from app import create_app, db
from app.models import User, Post
from config.testing import TestingConfig
from fixtures.user import add_users


class ApiCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.users = list(add_users())
        db.session.add_all(self.users)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_user(self):
        with self.app.test_client() as client:
            user = self.users[0]

            response = client.get("/api/users/{}".format(user.user_id))
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('username', data)
            self.assertEqual(data['username'], user.username)

    def test_get_no_user(self):
        with self.app.test_client() as client:
            response = client.get("/api/users/{}".format(len(self.users) + 1))
            self.assertEqual(404, response.status_code)

            data = response.get_json()
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Not Found')


if __name__ == "__main__":
    unittest.main(verbosity=2)
