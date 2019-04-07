from django.db import models
from RedditUser.models import RedditUser


class RedditUserMessage(models.Model):
    sender = models.ForeignKey(
        RedditUser,
        verbose_name="Sender",
        related_name="MessageSender",
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        RedditUser,
        verbose_name="Receiver",
        related_name="MessageReceiver",
        on_delete=models.CASCADE,
    )
    notification = models.ForeignKey(
        RedditUser,
        verbose_name="Receiver Notification",
        related_name="MessageReceiverNotification",
        on_delete=models.CASCADE,
        blank=True,
    )
    title = models.CharField("Title", max_length=50)
    body = models.CharField("Body", max_length=500)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return f"{self.sender.user.username} to {self.receiver.user.username} at {self.created_at}"

