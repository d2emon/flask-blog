import re


__items = [
    {'name': "item"}
]


def find_item(name):
    return next(
        (item for item in __items if item.get('name', '').lower() == name),
        None,
    )


class User:
    users = []
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

    def __init__(self, username, password, is_admin=False):
        if self.find(username):
            raise Exception("User already exists")

        self.user_id = len(self.users) + 1
        self.__username = (self.validate_username(username) is None) and username
        self.password = (self.validate_password(password) is None) and password
        self.is_admin = is_admin

    @classmethod
    def validate_username(cls, username):
        try:
            if not username:
                raise ValueError("Username is required")
            if '.' in username:
                raise ValueError("Illegal characters in username")
            if not cls.__valid_string.match(username):
                raise ValueError("Username string is invalid")
            if username in cls.__reserved_words:
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

    @classmethod
    def validate_password(cls, password):
        try:
            if not password:
                raise ValueError("Password is required")
            if '.' in password:
                raise ValueError("Illegal characters in password")
            return None
        except ValueError as e:
            return str(e)

    @classmethod
    def find(cls, username):
        return next(
            (user for user in cls.users if user.username == username),
            None,
        )

    @property
    def username(self):
        return self.__username.lower() if self.__username else ''

    @property
    def message_of_the_day(self):
        return "[Cannot Find -> MOTD]"

    def as_dict(self):
        return {
            'userId': self.user_id,
            'username': self.username,
            # 'password': self.password,
            'role': 'ADMIN' if self.is_admin else 'USER',
            'messageOfTheDay': self.message_of_the_day,
        }

    def save(self):
        self.users.append(self)
        return self


User("user", "pass", True).save()
