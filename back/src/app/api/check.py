BANNED = ['BannedUserId']
HOST_MACHINE = "HOST_MACHINE"
NO_LOGIN = None


def __check_banned(user_id):
    """
    Check if banned first
    Check to see if UID in banned list
    :param user_id:
    """
    if user_id in BANNED:
        raise Exception("I'm sorry- that userId has been banned")


def __check_host(hostname):
    """
    Check we are running on the correct host
    :param hostname:
    :return:
    """
    if hostname not in HOST_MACHINE:
        raise Exception("Blog is only available on {}, not on {}".format(HOST_MACHINE, hostname))


def __check_login():
    """
    Check if there is a no login active
    :return:
    """
    if NO_LOGIN:
        raise Exception(NO_LOGIN)


def check_all(user_id, hostname):
    """
    Check all
    :param user_id:
    :param hostname:
    :return:
    """
    __check_banned(user_id)
    __check_host(hostname)
    __check_login()
    return True
