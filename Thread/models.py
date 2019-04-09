from django.db import models
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from django.core.files.storage import FileSystemStorage
from django.conf import settings


fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Thread(models.Model):
    title = models.CharField("Title", max_length=100)
    is_link_post = models.BooleanField("Is the Post a link?")
    body = models.CharField("Body", max_length=500, blank=True, null=True)
    link = models.URLField("Link URL", max_length=200, blank=True, null=True)
    link_preview_img = models.FileField(
        "Link Preview Image", storage=fs, blank=True, null=True
    )
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    sender = models.ForeignKey(
        RedditUser, verbose_name="Sender", on_delete=models.CASCADE
    )

    subreddit = models.ForeignKey(
        Subreddit, verbose_name="Subreddit", on_delete=models.CASCADE
    )

    score = models.IntegerField(
        "Vote Score",
        blank=True,
        null=True
    )

    upvoters = models.ManyToManyField(
        RedditUser, verbose_name="Upvoters",
        related_name="upvoters",
        blank=True
    )

    downvoters = models.ManyToManyField(
        RedditUser,
        verbose_name="Downvoters",
        related_name="downvoters",
        blank=True,
    )

    def __str__(self):
        return f"{self.subreddit} - {self.title}"

    def set_score(self):
        self.score = len(self.upvoters.all()) - len(self.downvoters.all())
