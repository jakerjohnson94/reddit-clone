from django.db import models
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Thread.models import Thread


class ThreadComment(models.Model):
    body = models.CharField("body", max_length=250)
    sender = models.ForeignKey(
        RedditUser, verbose_name="Sender", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    post_thread = models.ForeignKey(
        Thread, verbose_name="Parent Thread", on_delete=models.CASCADE
    )
    score = models.IntegerField("Vote Score", blank=True, null=True)
    upvoters = models.ManyToManyField(
        RedditUser,
        verbose_name="Upvoters",
        related_name="comment_upvoters",
        blank=True,
    )
    downvoters = models.ManyToManyField(
        RedditUser,
        verbose_name="Downvoters",
        related_name="comment_downvoters",
        blank=True,
    )

    def __str__(self):
        return f"{self.post_thread} - #{self.id}"

    def set_score(self):
        self.score = len(self.upvoters.all()) - len(self.downvoters.all())

