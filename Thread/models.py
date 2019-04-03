from django.db import models
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote


class Thread(models.Model):
    title = models.CharField("Title", max_length=50)
    is_link_post = models.BooleanField("Is the Post a link?")
    body = models.CharField("Body", max_length=500, blank=True, null=True)
    link = models.URLField("Link URL", max_length=200, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    sender = models.ForeignKey(
        RedditUser, verbose_name="Sender", on_delete=models.CASCADE
    )
    subreddit = models.ForeignKey(
        Subreddit, verbose_name="Subreddit", on_delete=models.CASCADE
    )
    votes = models.ManyToManyField(Vote, verbose_name="Votes", blank=True)
    score = models.IntegerField("Vote Score", blank=True, null=True)

    def __str__(self):
        return f"{self.subreddit} - {self.title}"
