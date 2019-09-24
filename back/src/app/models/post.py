from app import db
from datetime import datetime
from .searchable import SearchableMixin


class Post(SearchableMixin, db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)
    # content = db.Column(
    #     db.Text,
    #     info={'label': "Content:", 'render_kw': {'class': "huy"}},
    # )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # modified_at = db.Column(db.DateTime, default=datetime.utcnow)
    language = db.Column(db.String(5))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    views = db.Column(db.Integer, default=0)
    # comments_count = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    # tags_name = db.Column(db.Text)
    __id_field__ = 'post_id'
    __searchable__ = ['body']

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    # def _url(self):
    #     return url_for('article_byname', postname=self.post_name)

    # @cached_property
    # def url(self):
    #     return self._url()

    # @cached_property
    # def comments(self):
    #     allcomments = Comment.query.filter(Comment.post_id == self.id).all()
    #     return allcomments

    # @cached_property
    # def markdown(self):
    #     return Markup(markdown(self.post_content or ''))
