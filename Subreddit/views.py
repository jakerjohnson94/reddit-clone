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


def list_all_view(request):
    html = "subreddit_list.html"
    subreddits = Subreddit.objects.all().order_by("name")
    data = {"subreddits": subreddits}
    return render(request, html, data)


def home_view(request, subreddit_name):
    html = "subreddit_homepage.html"
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    threads = Thread.objects.filter(subreddit=subreddit).order_by("-created_at")

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


def unsubscribe(request, subreddit_name):
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    try:
        reddit_user = RedditUser.objects.get(user=request.user)
        subreddit.subscribers.remove(reddit_user)
    except Exception as e:
        print(e)
    return redirect("subreddit", subreddit_name)


def subscribe(request, subreddit_name):
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    try:
        reddit_user = RedditUser.objects.get(user=request.user)
        subreddit.subscribers.add(reddit_user)
    except Exception as e:
        print(e)
    return redirect("subreddit", subreddit_name)
