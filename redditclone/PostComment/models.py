from django.db import models
from redditclone.RedditUser.models import RedditUser
from redditclone.Subreddit.models import Subreddit
from redditclone.MainPost.models import MainPost
from redditclone.Vote.models import Vote


class PostComment(models.Model):
    body = models.CharField("body", max_length=250)
    sender = models.ForeignKey(
        RedditUser, verbose_name="Sender", on_delete=models.CASCADE
    )
    post_thread = models.ForeignKey(
        MainPost, verbose_name="Parent Thread", on_delete=models.CASCADE
    )
    votes = models.ManyToManyField(Vote, verbose_name="Votes", blank=True)

    def __str__(self):
        return f"{self.post_thread} - #{self.id}"

