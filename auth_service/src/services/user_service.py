from auth_service.src.models.user_model import User
from commons.errors import MAIL_ALREADY_PRESENT, USER_NOT_FOUND


class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        if self.user_is_present(mail=user.email):
            raise MAIL_ALREADY_PRESENT

        self.users.append(user)
        return user

    def get_all_users(self):
        return self.users

    def get_user(self, email):
        for user in self.users:
            if user.email == email:
                return user

        raise USER_NOT_FOUND

    def delete_user(self, email):
        user = self.get_user(email)
        self.users.remove(user)
        return user

    def user_is_present(self, mail: str) -> bool:
        for user in self.users:
            if user.email == mail:
                return True

        return False
