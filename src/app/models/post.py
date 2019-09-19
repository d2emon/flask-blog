from app import db
from datetime import datetime
from .searchable import SearchableMixin


class Post(SearchableMixin, db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    language = db.Column(db.String(5))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    __searchable__ = ['body']

    def __repr__(self):
        return '<Post {}>'.format(self.body)
