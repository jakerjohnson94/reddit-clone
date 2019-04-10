from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect

# importing with different name so we don't have conflicts with my lazy naming
from django.contrib import messages as alert_messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect, get_user_data
from django.contrib.auth.decorators import login_required
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
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


@login_required
def logout_action(request):
    logout(request)
    return redirect(request.GET.get("next", "/"))


def create_user_view(request):
    form = None
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            user = User.objects.create_user(
                username=username, email=email, password=password
            )  # noqa
            RedditUser.objects.create(user=user)
            alert_messages.success(request, f"Account created for {username}!")
            return redirect("/")
    else:
        form = UserRegisterForm()
    html = "signup.html"
    return render(request, html, {"form": form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            alert_messages.success(
                request, "Your password was successfully updated!"
            )  # noqa
            return redirect("change_password")
        else:
            alert_messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {"form": form})
