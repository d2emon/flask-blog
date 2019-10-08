import re


__users = [
    {
        'userId': 1,
        'username': "user",
        'password': "pass",
    }
]
__items = [
    {'name': "item"}
]
__valid_string = re.compile("^([a-z]+)$")
__reserved_words = [
    'the',
    'me',
    'myself',
    'it',
    'them',
    'him',
    'her',
    'someone',
    'there',
]


def get_motd():
    return "[Cannot Find -> MOTD]"


def find_item(name):
    return next(
        (item for item in __items if item.get('name', '').lower() == name),
        None,
    )


def validate_username(username):
    try:
        if not username:
            raise ValueError("Username is required")
        if '.' in username:
            raise ValueError("Illegal characters in username")
        if not __valid_string.match(username):
            raise ValueError("Username string is invalid")
        if username in __reserved_words:
            raise ValueError("Sorry I cant call you that")
        if len(username) > 10:
            raise ValueError("Username string is too long")
        if ' ' in username:
            raise ValueError("Spaces in user name")
        if find_item(username):
            raise ValueError("I can't call you that, It would be confused with an object")
        return None
    except ValueError as e:
        return str(e)


def validate_password(password):
    try:
        if not password:
            raise ValueError("Password is required")
        if '.' in password:
            raise ValueError("Illegal characters in password")
        return None
    except ValueError as e:
        return str(e)


def find_user(username):
    return next(
        (user for user in __users if user.get('username').lower() == username),
        None,
    )


def save_user(username, password):
    user = {
        'userId': len(__users) + 1,
        'username': username,
        'password': password,
    }
    __users.append(user)
    return user
