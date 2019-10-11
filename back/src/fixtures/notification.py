from app.models import Notification


def add_notifications():
    yield Notification(
        name='Category1',
    )
    yield Notification(
        name='Category2',
    )
    yield Notification(
        name='Category3',
    )
