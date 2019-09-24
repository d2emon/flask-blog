from app import db


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    posts = db.relationship(
        'Post',
        backref='category',
        lazy='dynamic',
    )

    def __repr__(self):
        return '<Category {}>'.format(self.name)
