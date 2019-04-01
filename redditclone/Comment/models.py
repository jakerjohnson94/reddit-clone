from django.db import models
from redditclone.RedditUser.models import RedditUser
from redditclone.Subreddit.models import Subreddit
from redditclone.Post.models import Post
from redditclone.Vote.models import Vote


class Comment(models.Model):
    body = models.CharField("body", max_length=250)
    sender = models.ForeignKey(
        RedditUser, verbose_name="Sender", on_delete=models.CASCADE
    )
    post_thread = models.ForeignKey(
        Post, verbose_name="Parent Thread", on_delete=models.CASCADE
    )
    votes = models.ManyToManyField(Vote, verbose_name="Votes", blank=True)

