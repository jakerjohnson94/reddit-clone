from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Thread
from .forms import TextThreadForm, LinkThreadForm
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote
from django.views import View
from django.http import HttpResponseForbidden


def thread_page_view(request, thread_id):
    html = "thread_page.html"
    thread = get_object_or_404(Thread, pk=thread_id)
    comments = ThreadComment.objects.filter(post_thread=thread).order_by(
        "-created_at"
    )
    is_moderator = thread.subreddit.moderators.filter(
        user=request.user
    ).exists()
    is_own_post = thread.sender.user == request.user
    return render(
        request,
        html,
        {
            "thread": thread,
            "comments": comments,
            "is_moderator": is_moderator,
            "is_own_post": is_own_post,
        },
    )


@login_required
def new_thread_view(request, subreddit_name, post_type):
    html = "new_thread.html"
    form = None
    if request.method == "POST":
        if post_type == "text":
            form = TextThreadForm(request.POST)
            is_link_post = False
        elif post_type == "link":
            form = LinkThreadForm(request.POST)
            is_link_post = True

        if form.is_valid():
            data = form.cleaned_data
            reddit_user = get_object_or_404(RedditUser, user=request.user)
            subreddit = get_object_or_404(Subreddit, name=subreddit_name)
            thread = Thread(
                title=data["title"],
                sender=reddit_user,
                subreddit=subreddit,
                is_link_post=is_link_post,
            )

            if post_type == "text":
                thread.body = data["body"]
            elif post_type == "link":
                thread.link = data["link"]

            thread.save()
            return redirect("subreddit", subreddit_name)
    else:
        if post_type == "text":
            form = TextThreadForm()
        elif post_type == "link":
            form = LinkThreadForm()

    return render(request, html, {"form": form, "post_type": post_type})


@login_required
def delete_thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    subreddit = thread.subreddit
    is_moderator = subreddit.moderators.filter(user=request.user).exists()
    is_own_post = thread.sender.user == request.user
    if is_moderator or is_own_post:
        thread.delete()
    else:
        return HttpResponseForbidden()
    return redirect("subreddit", subreddit.name)
