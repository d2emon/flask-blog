from app import db


post_tags = db.Table(
    'tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.tag_id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.post_id')),
)


class Tag(db.Model):
    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    posts = db.relationship(
        'Post',
        secondary=post_tags,
        backref=db.backref('tags', lazy='dynamic'),
        lazy='dynamic',
    )

    def __repr__(self):
        return '<Tag {}>'.format(self.name)
