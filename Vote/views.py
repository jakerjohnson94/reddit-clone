from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from ThreadComment.models import ThreadComment
from Thread.models import Thread
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from redditclone.helpers import get_vote_score
from .models import Vote


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


def comment_vote(request, comment_id, vote_type):
    comment = get_object_or_404(ThreadComment, pk=comment_id)
    thread = comment.post_thread
    reddit_user = request.user.reddituser
    user_upvote = comment.upvoters.filter(user=request.user)
    user_downvote = comment.downvoters.filter(user=request.user)
    if user_upvote.exists():
        comment.upvoters.remove(reddit_user)
    elif user_downvote.exists():
        comment.downvoters.remove(reddit_user)
    else:
        if vote_type == 1:
            comment.upvoters.add(reddit_user)
        if vote_type == 2:
            comment.downvoters.add(reddit_user)
    comment.set_score()
    comment.save()
    return redirect("threaddetail", thread.id)
