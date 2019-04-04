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
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    post_thread = models.ForeignKey(
        Thread, verbose_name="Parent Thread", on_delete=models.CASCADE
    )
    votes = models.ManyToManyField(Vote, verbose_name="Votes", blank=True)
    score = models.IntegerField("Vote Score", blank=True, null=True)

    def __str__(self):
        return f"{self.post_thread} - #{self.id}"

    def set_score(self):
        score = 0
        for vote in self.votes.all():
            if vote.vote_type == 1:
                score += 1
            elif vote.vote_type == 2:
                score -= 1
        self.score = score
        return score
