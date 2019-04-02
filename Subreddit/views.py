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


def home_view(request, subreddit_id):
    html = "subreddit_homepage.html"
    subreddit = get_object_or_404(Subreddit, pk=subreddit_id)
    threads = Thread.objects.filter(subreddit=subreddit)

    if subreddit.moderators.filter(user=request.user).exists():
        is_moderator = True
    else:
        is_moderator = False

    data = {
        "subreddit": subreddit,
        "threads": threads,
        "subscribers": subreddit.subscribers.all(),
        "moderators": subreddit.moderators.all(),
        "is_moderator": is_moderator,
    }
    return render(request, html, data)
