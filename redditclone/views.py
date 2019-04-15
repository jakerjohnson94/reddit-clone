from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Message.models import Message
from .helpers import flag_user_thread_votes


def homepage(request):
    html = "index.html"
    notifications = []
    if request.user.is_authenticated:
        subscribed_subreddits = request.user.reddituser.subscribers.all()
        threads = Thread.objects.filter(
            subreddit__in=subscribed_subreddits
        ).order_by("-score", "-created_at")[:25]
        for thread in threads:
            flag_user_thread_votes(thread, request)

        notifications = Message.objects.filter(
            notification=request.user.reddituser
        )
    else:
        threads = Thread.objects.all().order_by("-score", "-created_at")[:25]
    if not threads.exists():
        threads = None
    data = {"threads": threads, "notifications": len(notifications)}
    return render(request, html, data)

