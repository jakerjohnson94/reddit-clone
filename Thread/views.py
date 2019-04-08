from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Thread
from .forms import TextThreadForm, LinkThreadForm
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit

from django.views import View
from django.http import HttpResponseForbidden
from redditclone.helpers import (
    flag_user_thread_votes,
    set_post_score,
    flag_own_post,
)


def thread_page_view(request, thread_id):
    html = "thread_page.html"
    thread = get_object_or_404(Thread, pk=thread_id)
    comments = ThreadComment.objects.filter(post_thread=thread).order_by(
        "-score"
    )
    for comment in comments:
        flag_own_post(comment, request.user)
        set_post_score(comment)
    is_moderator = False
    is_own_post = False
    if request.user.is_authenticated:
        flag_user_thread_votes(comments, request)
        flag_user_thread_votes([thread], request)
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
            reddit_user = request.user.reddituser
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


@login_required
def thread_vote(request, thread_id, vote_type):
    thread = get_object_or_404(Thread, pk=thread_id)
    reddit_user = request.user.reddituser
    user_upvote = thread.upvoters.filter(user=request.user)
    user_downvote = thread.downvoters.filter(user=request.user)
    if user_upvote.exists():
        thread.upvoters.remove(reddit_user)
    elif user_downvote.exists():
        thread.downvoters.remove(reddit_user)
    else:
        if vote_type == 1:
            thread.upvoters.add(reddit_user)
        if vote_type == 2:
            thread.downvoters.add(reddit_user)
    thread.set_score()
    thread.save()
    return redirect("/")
