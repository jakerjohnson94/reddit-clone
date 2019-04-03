from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote


@login_required
def homepage(request):
    html = "index.html"
    threads = Thread.objects.all().order_by("-created_at")[:25]
    data = {"threads": threads}
    return render(request, html, data)

