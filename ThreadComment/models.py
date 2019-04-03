from django.db import models
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Thread.models import Thread
from Vote.models import Vote


class ThreadComment(models.Model):
    body = models.CharField("body", max_length=250)
    sender = models.ForeignKey(
        RedditUser, verbose_name="Sender", on_delete=models.CASCADE
    )
    post_thread = models.ForeignKey(
        Thread, verbose_name="Parent Thread", on_delete=models.CASCADE
    )
    votes = models.ManyToManyField(Vote, verbose_name="Votes", blank=True)
    created_at = models.DateTimeField("Created At", auto_now=True)

    def __str__(self):
        return f"{self.post_thread} - #{self.id}"

