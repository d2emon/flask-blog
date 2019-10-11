import unittest
import json
from tests import ApiTestCase


class AuthorizedApiCase(ApiTestCase):
    def test_get_users(self):
        with self.app.test_client() as client:
            response = client.get("/api/users")
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('username', data)
            self.assertEqual(data['username'], self.user.username)

    def test_get_followers(self):
        with self.app.test_client() as client:
            response = client.get("/api/users/{}/followers".format(self.user.user_id))
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('username', data)
            self.assertEqual(data['username'], self.user.username)

    def test_get_followed(self):
        with self.app.test_client() as client:
            response = client.get("/api/users/{}/followed".format(self.user.user_id))
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('username', data)
            self.assertEqual(data['username'], self.user.username)

    def test_create_user(self):
        with self.app.test_client() as client:
            response = client.post("/api/users", data=json.dumps({}))
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('username', data)
            self.assertEqual(data['username'], self.user.username)

    def test_update_user(self):
        with self.app.test_client() as client:
            response = client.put("/api/users/{}".format(self.user.user_id), data=json.dumps({}))
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('username', data)
            self.assertEqual(data['username'], self.user.username)

    def test_get_articles(self):
        with self.app.test_client() as client:
            response = client.get("/api/articles")
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('total', data)
            self.assertIn('articles', data)

    def test_get_categories(self):
        with self.app.test_client() as client:
            response = client.get("/api/categories")
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('total', data)
            self.assertIn('categories', data)

    def test_get_instagram(self):
        with self.app.test_client() as client:
            response = client.get("/api/instagram")
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('total', data)
            self.assertIn('instagram', data)

    def test_get_tests(self):
        with self.app.test_client() as client:
            response = client.get("/api/tags")
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('total', data)
            self.assertIn('tags', data)

    def test_get_notifications(self):
        with self.app.test_client() as client:
            response = client.get("/api/notifications")
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('total', data)
            self.assertIn('notifications', data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
