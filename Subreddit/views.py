from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from .models import Subreddit
from .forms import CreateSubredditForm

from RedditUser.forms import LoginForm
from django.views import View
from django.http import HttpResponseRedirect
from redditclone.helpers import flag_user_thread_votes


def list_all_view(request):
    html = "subreddit_list.html"
    subreddits = Subreddit.objects.all().order_by("name")
    data = {"subreddits": subreddits}
    return render(request, html, data)


def home_view(request, subreddit_name):
    html = "subreddit_homepage.html"
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    threads = Thread.objects.filter(subreddit=subreddit).order_by("-score")
    is_moderator = False
    is_subscriber = False
    if request.user.is_authenticated:
        for thread in threads:
            flag_user_thread_votes(thread, request)
        if subreddit.moderators.filter(user=request.user).exists():
            is_moderator = True
        if subreddit.subscribers.filter(user=request.user).exists():
            is_subscriber = True

    data = {
        "subreddit": subreddit,
        "threads": threads,
        "subscribers": subreddit.subscribers.all(),
        "moderators": subreddit.moderators.all(),
        "is_subscriber": is_subscriber,
        "is_moderator": is_moderator,
    }
    return render(request, html, data)


@login_required
def create_new_view(request):
    html = "subreddit_create.html"
    form = None
    reddit_user = request.user.reddituser
    if request.method == "POST":
        form = CreateSubredditForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            sidebar_content = form.cleaned_data["sidebar_content"]
            new_subreddit = Subreddit(
                name=name,
                description=description,
                sidebar_content=sidebar_content,
                created_by=reddit_user,
            )
            new_subreddit.save()
            new_subreddit.moderators.set([reddit_user])
            return redirect("subreddit", new_subreddit.name)
    else:
        form = CreateSubredditForm()

    return render(request, html, {"form": form})


@login_required
def unsubscribe(request, subreddit_name):
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    reddit_user = request.user.reddituser
    try:
        subreddit.subscribers.remove(reddit_user)
    except Exception as e:
        print(e)
    return redirect("subreddit", subreddit_name)


@login_required
def subscribe(request, subreddit_name):
    subreddit = get_object_or_404(Subreddit, name=subreddit_name)
    reddit_user = request.user.reddituser
    try:
        subreddit.subscribers.add(reddit_user)
    except Exception as e:
        print(e)
    return redirect("subreddit", subreddit_name)

