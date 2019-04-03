from django.db import models
from RedditUser.models import RedditUser

# Subreddit(ID, name, description, sidebar_content, created_at, subscribers, moderators,
class Subreddit(models.Model):
    name = models.CharField("Name", max_length=50, unique=True)
    description = models.CharField("Description", max_length=250)
    sidebar_content = models.CharField(
        "Sidebar Content", max_length=250, blank=True, null=True
    )
    created_at = models.DateTimeField("Created At", auto_now=True)
    created_by = models.ForeignKey(
        RedditUser, verbose_name="Created By", on_delete=models.CASCADE
    )
    subscribers = models.ManyToManyField(
        RedditUser,
        related_name="subscribers",
        verbose_name="Subscribers",
        blank=True,
    )
    moderators = models.ManyToManyField(
        RedditUser, related_name="moderators", verbose_name="Moderators"
    )

    def __str__(self):
        return self.name
