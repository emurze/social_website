from django.contrib.auth.models import User


class EmailAuthBackend:
    @staticmethod
    def authenticate(request, username: str | None = None,
                     password: str | None = None) -> User | None:
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    @staticmethod
    def get_user(user_id: int) -> User | None:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
