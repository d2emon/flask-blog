from app.models import User


def add_users():
    yield User(
        username='usera',
        email='usera@example.com',
    )
    yield User(
        username='userb',
        email='userb@example.com',
    )
    yield User(
        username='userc',
        email='userc@example.com',
    )
