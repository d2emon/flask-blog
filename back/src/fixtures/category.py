from app.models import Category


def add_categories():
    yield Category(
        name='Category1',
    )
    yield Category(
        name='Category2',
    )
    yield Category(
        name='Category3',
    )
