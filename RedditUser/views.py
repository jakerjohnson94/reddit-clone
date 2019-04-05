from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote
from RedditUser.forms import LoginForm
from django.views import View
from django.contrib.auth.models import User
from .forms import UserRegisterForm


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
                return redirect("/")
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_action(request):
    logout(request)
    return redirect(request.GET.get("next", "/"))


def create_user_view(request):
    form = None
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username=username, email=email, password=password) # noqa
            RedditUser.objects.create(user=user)
            messages.success(request, f'Account created for {username}!')
            return redirect("/")
    else:
        form = UserRegisterForm()
    html = "signup.html"
    return render(request, html, {"form": form})
