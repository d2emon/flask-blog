import unittest
# import os
# import tempfile
import json
from flask import Response, appcontext_pushed, g, request
from contextlib import contextmanager
from app import create_app, db
from app.models import User
from config.testing import TestingConfig


@contextmanager
def user_set(app, user):
    def handler(sender, **kwargs):
        g.user = user
    with appcontext_pushed.connected_to(handler, app):
        yield


class BlogTestCase(unittest.TestCase):
    def setUp(self):
        # self.db, app.config['DATABASE'] = tempfile.mkstemp()
        # app.config['TESTING'] = True
        # self.app = app.test_client()
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        # os.close(self.db)
        # os.unlink(app.config['DATABASE'])
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self, username, password):
        return self.client.post(
            '/login',
            data={
                'username': username,
                'password': password,
            },
            follow_redirects=True,
        )

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_empty_db(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        assert 'Redirecting...' in str(response.data)

    def test_login_logout(self):
        response = self.login('admin', 'default')
        self.assertEqual(response.status_code, 200)
        assert 'You were logged in' in str(response.data)
        response = self.logout()
        self.assertEqual(response.status_code, 200)
        assert 'You were logged out' in str(response.data)
        response = self.login('adminx', 'default')
        self.assertEqual(response.status_code, 200)
        assert 'Invalid username' in str(response.data)
        response = self.login('admin', 'defaultx')
        self.assertEqual(response.status_code, 200)
        assert 'Invalid password' in str(response.data)

    def test_messages(self):
        self.login('admin', 'default')
        response = self.client.post(
            '/add',
            data={
                'title': "<Hello>",
                'text': "<strong>HTML</strong> allowed here",
            },
            follow_redirects=True,
        )
        assert 'No entries' in str(response.data)
        assert '&lt;Hello&gt;' in str(response.data)
        assert '<strong>HTML</strong> allowed here' in str(response.data)

    def test_context(self):
        with self.app.test_request_context('/?name=Peter'):
            self.app.preprocess_request()
            assert request.path == '/'
            assert request.args.get('name') == 'Peter'
            response = Response('...')
            response = self.app.process_response(response)

    def test_context_manager(self):
        user = User(username='susan')
        with user_set(self.app, user):
            with self.app.test_client() as client:
                response = client.get('/users/me')
                data = json.loads(response.data)
                self.assertEqual(user.username, data.get('username'))
                with client.session_transaction() as session:
                    session['key'] = 'value'


if __name__ == '__main__':
    unittest.main()
