from django.db import models
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit


class Vote(models.Model):
    VOTE_CHOICES = ((1, "Upvote"), (-1, "Downvote"))

    user = models.ForeignKey(
        RedditUser, verbose_name="User", on_delete=models.CASCADE
    )
    vote_type = models.IntegerField("Type", choices=VOTE_CHOICES)

    def __str__(self):
        return f"{self.user} - {self.vote_type}"

