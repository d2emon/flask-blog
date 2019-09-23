import base64
import json
import jwt
import os
from app import db, login
from datetime import datetime, timedelta
from flask import current_app, url_for
from flask_login import UserMixin
from hashlib import md5
from time import time
from werkzeug.security import generate_password_hash, check_password_hash
from .message import Message
from .notification import Notification
from .paginated import PaginatedAPIMixin
from .post import Post
from .task import Task


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.user_id')),
)


class User(PaginatedAPIMixin, UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    last_message_read_time = db.Column(db.DateTime)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
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

    def to_dict(self, include_email=False):
        data = {
            'id': self.user_id,
            'username': self.username,
            'last_seen': self.last_seen.isoformat() + 'Z',
            'about_me': self.about_me,
            'post_count': self.posts.count(),
            'follower_count': self.followers.count(),
            'followed_count': self.followed.count(),
            '_links': {
                'self': url_for('api.get_user', user_id=self.user_id),
                'followers': url_for('api.get_followers', user_id=self.user_id),
                'followed': url_for('api.get_followed', user_id=self.user_id),
                'avatar': self.avatar(128),
            },
        }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        fields = (field for field in data if field in ('username', 'email', 'about_me'))
        for field in fields:
            setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
