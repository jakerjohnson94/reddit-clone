from django.db import models
from django.contrib.auth.models import User

# User(ID, username, password, email,
class RedditUser(models.Model):
    user = models.OneToOneField(
        User, verbose_name="Auth User", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username
