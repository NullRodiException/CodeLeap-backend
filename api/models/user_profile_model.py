from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    app_username = models.CharField(max_length=50, unique=True, blank=True, null=True,
                                    help_text="Nome de usuário único na aplicação, para mentions.")

    def __str__(self):
        return self.user.username
