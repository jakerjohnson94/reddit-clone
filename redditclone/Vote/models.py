from django.db import models
from redditclone.RedditUser.models import RedditUser
from redditclone.Subreddit.models import Subreddit


# Vote(ID, user, type, post )
STATUS_CHOICES = ((1, "Upvote"), (2, "Downvote"))


class Vote(models.Model):
    user = models.ForeignKey(
        RedditUser, verbose_name="User", on_delete=models.CASCADE
    )
    vote_type = models.IntegerField("Type", choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user}"

