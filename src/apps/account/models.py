from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    date_of_birth = models.DateField(blank=True, default=timezone.now)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True,
                              default='users/default/user_icon.png')

    def __str__(self) -> str:
        return f'Profile of {self.user.username}'
