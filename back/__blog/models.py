from app import db


from datetime import datetime


class User():
    username = "test"
    password = "test"
    error = ""

    def login(self, username, password):
        self.error = ""
        if username != self.username:
            self.error = 'Invalid username'
        elif password != self.password:
            self.error = 'Invalid password'

        return self.error == ""

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return 1

article_tags = db.Table(
    'tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
)


class Category(db.Model):
    # __tablename__ = 'category'
    # query_class = CategoryQuery
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255), unique=True)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<category name %r>' % self.category_name


class Tag(db.Model):
    # __tablename__ = 'tag'
    # query_class = TagQuery
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<tag name %r>' % self.name


class Post(db.Model):
    # __tablename__ = 'post'
    # query_class = PostQuery
    id = db.Column(db.Integer, primary_key=True)
    # name=db.Column(db.String(255), unique=True)
    title = db.Column(db.String(128))
    content = db.Column(
        db.Text,
        info={'label': "Content:", 'render_kw': {'class': "huy"}},
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)
    views = db.Column(db.Integer, default=0)
    comments_count = db.Column(db.Integer, default=0)

    # status=db.Column(db.Integer, default=1)

    # author_id=db.Column(db.Integer, default=1)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    categories = db.relationship(
        'Category',
        backref=db.backref('posts', lazy='dynamic'),
        lazy='select'
    )

    tags = db.relationship(
        'Tag',
        secondary=article_tags,
        backref=db.backref('posts', lazy='dynamic')
    )
    tags_name = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<post %r>' % self.title

    @property
    def author(self):
        return "d2emon"

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
