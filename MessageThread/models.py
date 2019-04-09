from django.db import models
from RedditUser.models import RedditUser
from Message.models import Message


class MessageThread(models.Model):
    users = models.ManyToManyField(RedditUser, verbose_name="Users")
    messages = models.ManyToManyField(
        Message, verbose_name="Messages", blank=True
    )
    title = models.CharField("Title", max_length=50)

    def __str__(self):
        return self.title
