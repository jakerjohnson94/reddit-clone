from django.db import models
from redditclone.RedditUser.models import RedditUser
from redditclone.Subreddit.models import Subreddit
from redditclone.Vote.models import Vote


class Post(models.Model):
    is_new_thread = models.BooleanField("Is a New Thread?")
    title = models.CharField("Title", max_length=50, blank=True, null=True)
    body = models.CharField("Body", max_length=500, blank=True, null=True)
    link = models.URLField("Link URL", max_length=200, blank=True, null=True)
    sender = models.ForeignKey(
        RedditUser, verbose_name="Sender", on_delete=models.CASCADE
    )
    subreddit = models.ForeignKey(
        Subreddit, verbose_name="Subreddit", on_delete=models.CASCADE
    )
    votes = models.ManyToManyField(Vote, verbose_name="Votes")

    def __str__(self):
        return self.title
