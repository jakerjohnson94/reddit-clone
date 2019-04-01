from django.db import models
from redditclone.RedditUser.models import RedditUser
from redditclone.Subreddit.models import Subreddit
from redditclone.Vote.models import Vote


class MainPost(models.Model):
    title = models.CharField("Title", max_length=50)
    is_link_post = models.BooleanField("Is a Link Post?")
    body = models.CharField("Body", max_length=500, blank=True, null=True)
    link = models.URLField("Link URL", max_length=200, blank=True, null=True)
    sender = models.ForeignKey(
        RedditUser, verbose_name="Sender", on_delete=models.CASCADE
    )
    subreddit = models.ForeignKey(
        Subreddit, verbose_name="Subreddit", on_delete=models.CASCADE
    )
    votes = models.ManyToManyField(Vote, verbose_name="Votes", blank=True)

    def __str__(self):
        return f" {self.subreddit} - {self.title}"
