import json
import jwt
from app import db, login
from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from hashlib import md5
from time import time
from werkzeug.security import generate_password_hash, check_password_hash
from .message import Message
from .notification import Notification
from .post import Post
from .task import Task


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.user_id')),
)


class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    posts = db.relationship(
        'Post',
        backref='author',
        lazy='dynamic',
    )
    followed = db.relationship(
        'User',
        secondary=followers,
        primaryjoin=(followers.c.follower_id == user_id),
        secondaryjoin=(followers.c.followed_id == user_id),
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic',
    )
    messages_sent = db.relationship(
        'Message',
        foreign_keys='Message.sender_id',
        backref='author',
        lazy='dynamic',
    )
    messages_received = db.relationship(
        'Message',
        foreign_keys='Message.receiver_id',
        backref='receiver',
        lazy='dynamic',
    )
    last_message_read_time = db.Column(db.DateTime)
    notifications = db.relationship(
        'Notification',
        backref='user',
        lazy='dynamic',
    )
    tasks = db.relationship(
        'Task',
        backref='user',
        lazy='dynamic',
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_id(self):
        return self.user_id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {
                'reset_password': self.user_id,
                'exp': time() + expires_in,
            },
            current_app.config['SECRET_KEY'],
            algorithm='HS256',
        ).decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256']
            )['reset_password']
        except jwt.exceptions.InvalidSignatureError:
            return

        return User.query.get(id)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.user_id).count() > 0

    def followed_posts(self):
        return Post.query.join(
            followers,
            (followers.c.followed_id == Post.user_id),
        ).filter(
            followers.c.follower_id == self.user_id
        ).union(
            Post.query.filter_by(user_id=self.user_id)
        ).order_by(
            Post.timestamp.desc()
        )

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(receiver=self).filter(Message.timestamp > last_read_time).count()

    def add_notification(self, name, data):
        self.notifications.filter_by(name=name).delete()
        notification = Notification(
            name=name,
            payload=json.dumps(data),
            user=self,
        )
        db.session.add(notification)
        return notification

    def launch_task(self, name, description, *args, **kwargs):
        rq_job = current_app.task_queue.enqueue('app.tasks.' + name, self.user_id, *args, **kwargs)
        task = Task(
            task_id=rq_job.get_id(),
            name=name,
            description=description,
            user=self,
        )
        db.session.add(task)
        return task

    def get_tasks_in_progress(self):
        return Task.query.filter_by(user=self, complete=False).all()

    def get_task_in_progress(self, name):
        return Task.query.filter_by(
            name=name,
            user=self,
            complete=False,
        ).first()


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
