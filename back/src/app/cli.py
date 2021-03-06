import click
import os
from app.models import Post


def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel init -i messages.pot -d app/translations -l ' + lang):
            raise RuntimeError('extract command failed')
        os.remove('messages.pot')

    @translate.command()
    def update():
        """Update all languages."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel update -i messages.pot -d app/translations'):
            raise RuntimeError('extract command failed')
        os.remove('messages.pot')

    @translate.command()
    def compile():
        """Compile all languages."""
        if os.system('pybabel compile -d app/translations'):
            raise RuntimeError('compile command failed')

    @app.cli.group()
    def search():
        """Elasticsearch commands."""
        pass

    @search.command()
    def reindex():
        """Reindex all posts."""
        Post.reindex()

    @app.cli.group()
    def fill():
        """Fill data."""
        pass

    @fill.command()
    def categories():
        """Add categories."""
        categories = [
            "PYTHON",
            "cat1",
            "cat2",
            "cat3",
            "cat4",
            "cat5",
        ]
        # from model import Category
        for category_id, category in enumerate(categories):
            # item = Category()
            # item.category_id = category_id
            # item.category_name = category
            # db.session.add(item)
            pass
        # db.session.commit()
