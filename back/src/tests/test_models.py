import unittest
from datetime import datetime, timedelta
from app import db
from app.models import Message, Post, Task, User
from app.models.user import load_user
from tests import ApiTestCase


def user_factory():
    yield User(
        username='john',
        email='john@example.com',
    )
    yield User(
        username='susan',
        email='susan@example.com',
    )


class UserModelCase(ApiTestCase):
    def test_get_id(self):
        user_generator = user_factory()
        users = [next(user_generator) for _ in range(2)]
        db.session.add_all(users)
        db.session.commit()

        self.assertNotEqual(users[0].get_id(), users[1].get_id())

    def test_load_user(self):
        user_generator = user_factory()
        user = next(user_generator)
        db.session.add(user)
        db.session.commit()

        self.assertEqual(user, load_user(str(user.user_id)))

    def test_password_hashing(self):
        user = User(username='susan')
        user.set_password('cat')
        self.assertFalse(user.check_password('dog'))
        self.assertTrue(user.check_password('cat'))

    def test_password_reset(self):
        user_generator = user_factory()
        user = next(user_generator)
        db.session.add(user)
        db.session.commit()

        token = user.get_reset_password_token()
        self.assertIsInstance(token, str)
        self.assertEqual(user, User.verify_reset_password_token(token))

        wrong_user = User.verify_reset_password_token('wrong token')
        self.assertEqual(None, wrong_user)

    def test_avatar(self):
        user = User(
            username='john',
            email='john@example.com',
        )
        self.assertEqual(
            user.avatar(128),
            'https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=identicon&s=128',
        )

    def test_follow(self):
        user1 = User(
            username='john',
            email='john@example.com',
        )
        user2 = User(
            username='susan',
            email='susan@example.com',
        )
        db.session.add_all([
            user1,
            user2,
        ])
        db.session.commit()
        self.assertEqual(user1.followed.all(), [])
        self.assertEqual(user2.followers.all(), [])

        user1.follow(user2)
        db.session.commit()
        self.assertTrue(user1.is_following(user2))
        self.assertEqual(user1.followed.count(), 1)
        self.assertEqual(user1.followed.first().username, 'susan')
        self.assertEqual(user2.followers.count(), 1)
        self.assertEqual(user2.followers.first().username, 'john')

        user1.follow(user2)
        db.session.commit()
        self.assertTrue(user1.is_following(user2))
        self.assertEqual(user1.followed.count(), 1)
        self.assertEqual(user1.followed.first().username, 'susan')
        self.assertEqual(user2.followers.count(), 1)
        self.assertEqual(user2.followers.first().username, 'john')

        user1.unfollow(user2)
        db.session.commit()
        self.assertFalse(user1.is_following(user2))
        self.assertEqual(user1.followed.count(), 0)
        self.assertEqual(user2.followers.count(), 0)

        user1.unfollow(user2)
        db.session.commit()
        self.assertFalse(user1.is_following(user2))
        self.assertEqual(user1.followed.count(), 0)
        self.assertEqual(user2.followers.count(), 0)

    def test_follow_posts(self):
        user1 = User(
            username='john',
            email='john@example.com',
        )
        user2 = User(
            username='susan',
            email='susan@example.com',
        )
        user3 = User(
            username='mary',
            email='mary@example.com',
        )
        user4 = User(
            username='david',
            email='david@example.com',
        )
        db.session.add_all([
            user1,
            user2,
            user3,
            user4,
        ])

        # create posts
        now = datetime.utcnow()
        post1 = Post(
            body="post from john",
            author=user1,
            timestamp=now + timedelta(seconds=1),
        )
        post2 = Post(
            body="post from susan",
            author=user2,
            timestamp=now + timedelta(seconds=4),
        )
        post3 = Post(
            body="post from mary",
            author=user3,
            timestamp=now + timedelta(seconds=3),
        )
        post4 = Post(
            body="post from david",
            author=user4,
            timestamp=now + timedelta(seconds=2),
        )
        db.session.add_all([
            post1,
            post2,
            post3,
            post4,
        ])
        db.session.commit()

        # Setup followers
        user1.follow(user2)
        user1.follow(user4)
        user2.follow(user3)
        user3.follow(user4)
        db.session.commit()

        # Check the follower posts for each user
        followed_posts1 = user1.followed_posts().all()
        followed_posts2 = user2.followed_posts().all()
        followed_posts3 = user3.followed_posts().all()
        followed_posts4 = user4.followed_posts().all()

        self.assertEqual(followed_posts1, [post2, post4, post1])
        self.assertEqual(followed_posts2, [post2, post3])
        self.assertEqual(followed_posts3, [post3, post4])
        self.assertEqual(followed_posts4, [post4])

    def test_messages(self):
        user_generator = user_factory()
        user1 = next(user_generator)
        user2 = next(user_generator)
        db.session.add_all([
            user1,
            user2,
        ])
        db.session.commit()

        self.assertEqual(0, user1.new_messages())
        self.assertEqual(0, user2.new_messages())

        message = Message(
            receiver_id=user1.user_id,
            sender_id=user2.user_id,
        )
        db.session.add(message)
        db.session.commit()

        self.assertEqual(1, user1.new_messages())
        self.assertEqual(0, user2.new_messages())

        user1.last_message_read_time = datetime.utcnow()
        user2.last_message_read_time = datetime.utcnow()
        db.session.add_all([
            user1,
            user2,
        ])
        message = Message(
            receiver_id=user2.user_id,
            sender_id=user1.user_id,
        )
        db.session.add(message)
        db.session.commit()

        self.assertEqual(0, user1.new_messages())
        self.assertEqual(1, user2.new_messages())

    def test_notifications(self):
        user_generator = user_factory()
        user = next(user_generator)
        db.session.add(user)

        user.add_notification('notification1', {'key': 1})
        db.session.commit()

        self.assertEqual(1, user.notifications.count())
        notification = user.notifications.first()
        self.assertIsNotNone(notification)
        self.assertIsInstance(notification.payload, str)
        payload = notification.get_data()
        self.assertIsInstance(payload, dict)
        self.assertIn('key', payload)
        self.assertEqual(1, payload['key'])

        user.add_notification('notification1', {'key': 2})
        db.session.commit()

        self.assertEqual(1, user.notifications.count())
        notification = user.notifications.first()
        self.assertIsNotNone(notification)
        self.assertIsInstance(notification.payload, str)
        payload = notification.get_data()
        self.assertIsInstance(payload, dict)
        self.assertIn('key', payload)
        self.assertEqual(2, payload['key'])

        user.add_notification('notification2', {'key': 2})
        db.session.commit()

        self.assertEqual(2, user.notifications.count())
        notification = user.notifications.first()
        self.assertIsNotNone(notification)
        self.assertIsInstance(notification.payload, str)
        payload = notification.get_data()
        self.assertIsInstance(payload, dict)
        self.assertIn('key', payload)
        self.assertEqual(2, payload['key'])

    def test_tasks(self):
        self.app.redis.return_value = {'data': {}}

        user_generator = user_factory()
        user = next(user_generator)
        db.session.add(user)

        now = datetime.utcnow()
        post1 = Post(
            body="post from john",
            author=user,
            timestamp=now + timedelta(seconds=1),
        )
        post2 = Post(
            body="post from susan",
            author=user,
            timestamp=now + timedelta(seconds=4),
        )
        db.session.add_all([
            post1,
            post2,
        ])
        db.session.commit()

        user.launch_task('export_posts', 'description')
        db.session.commit()

        self.assertEqual(1, len(user.get_tasks_in_progress()))

        task = user.get_task_in_progress('export_posts')
        self.assertIsInstance(task, Task)
        self.assertEqual('export_posts', task.name)
        self.assertEqual('description', task.description)

        self.assertIsNone(task.get_rq_job())
        self.assertEqual(100, task.get_progress())

    def test_to_dict(self):
        user_generator = user_factory()
        user = next(user_generator)
        db.session.add(user)
        db.session.commit()

        as_dict = user.to_dict()
        self.assertIsInstance(as_dict, dict)
        self.assertIn('id', as_dict)
        self.assertEqual(user.user_id, as_dict['id'])
        self.assertIn('username', as_dict)
        self.assertEqual(user.username, as_dict['username'])
        self.assertNotIn('email', as_dict)

        as_dict = user.to_dict(True)
        self.assertIsInstance(as_dict, dict)
        self.assertIn('email', as_dict)
        self.assertEqual(user.email, as_dict['email'])

    def test_from_dict(self):
        user_generator = user_factory()
        user1 = next(user_generator)
        user1.set_password('oldpassword')
        db.session.add(user1)
        db.session.commit()

        user2 = next(user_generator)
        user1.from_dict({
            'username': user2.username,
            'password': 'newpassword',
            'email': user2.email,
            'about_me': user2.about_me,
        })

        self.assertEqual(user2.username, user1.username)
        self.assertEqual(user2.email, user1.email)
        self.assertEqual(user2.about_me, user1.about_me)
        self.assertFalse(user1.check_password('newpassword'))

        user1.from_dict({'password': 'newpassword'}, True)
        self.assertTrue(user1.check_password('newpassword'))

    def test_token(self):
        user_generator = user_factory()
        user = next(user_generator)

        token = user.get_token()
        self.assertEqual(user, User.check_token(token))

        self.assertIsNone(User.check_token('wrong token'))

        token = user.get_token()
        self.assertEqual(user, User.check_token(token))

        user.revoke_token()
        self.assertIsNone(User.check_token(token))


if __name__ == "__main__":
    unittest.main(verbosity=2)
