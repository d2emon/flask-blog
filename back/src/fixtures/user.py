from app.models import User


def __users():
    yield User(
        username='user',
        email='user@example.com',
    )
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


def add_users():
    for user in __users():
        user.set_password('password')
        yield user
