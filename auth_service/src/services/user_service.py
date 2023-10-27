from auth_service.src.models.user_model import User
from commons.errors import MAIL_ALREADY_PRESENT, USER_NOT_FOUND

users = []


def add_user(user: User):
    if user_is_present(mail=user.email):
        raise MAIL_ALREADY_PRESENT

    users.append(user)
    return user


def get_all_users():
    return users


def get_user(email):
    for user in users:
        if user.email == email:
            return user

    raise USER_NOT_FOUND


def delete_user(email):
    user = get_user(email)
    users.remove(user)
    return user


def user_is_present(mail: str) -> bool:
    for user in users:
        if user.email == mail:
            return True

    return False
