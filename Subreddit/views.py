from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote
from RedditUser.forms import LoginForm
from django.views import View
from django.http import HttpResponseRedirect


def unsubscribe(request, subreddit_name):
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)


def home_view(request, subreddit_name):
    html = "subreddit_homepage.html"
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    threads = Thread.objects.filter(subreddit=subreddit)

    if subreddit.moderators.filter(user=request.user).exists():
        is_moderator = True
    else:
        is_moderator = False

    if subreddit.subscribers.filter(user=request.user).exists():
        is_subscriber = True
    else:
        is_subscriber = False

    data = {
        "subreddit": subreddit,
        "threads": threads,
        "subscribers": subreddit.subscribers.all(),
        "moderators": subreddit.moderators.all(),
        "is_subscriber": is_subscriber,
        "is_moderator": is_moderator,
    }
    return render(request, html, data)
