from django.db import models
from RedditUser.models import RedditUser


class Message(models.Model):
    body = models.CharField("Body", max_length=1000)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    sender = models.ForeignKey(
        RedditUser,
        verbose_name="Sender",
        related_name="sender",
        on_delete=models.CASCADE,
    )
    notification = models.ManyToManyField(
        RedditUser,
        verbose_name="Notification",
        related_name="notification",
        blank=True,
    )

