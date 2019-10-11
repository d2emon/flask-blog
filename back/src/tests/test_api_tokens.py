import unittest
from tests import ApiTestCase


class ApiTokenCase(ApiTestCase):
    def test_get_token(self):
        with self.app.test_client() as client:
            headers = {
                'Authorization': self.basic_auth('user', 'password'),
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }

            response = client.post("/api/tokens", headers=headers)
            self.assertEqual(200, response.status_code)

            data = response.get_json()
            self.assertNotIn('error', data)

            self.assertIn('token', data)
            token = data['token']

            self.assertIsNotNone(token)
            headers["Authorization"] = self.bearer_auth(token)

            response = client.delete("/api/tokens", headers=headers)
            self.assertEqual(204, response.status_code)

            response = client.delete("/api/tokens", headers=headers)
            self.assertEqual(401, response.status_code)


if __name__ == "__main__":
    unittest.main(verbosity=2)
