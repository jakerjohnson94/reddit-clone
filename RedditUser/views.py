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


def login_view(request):
    html = "login.html"
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})