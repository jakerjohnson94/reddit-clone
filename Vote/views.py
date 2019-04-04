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
    user_vote = thread.votes.filter(user=reddit_user)
    if user_vote.exists():
        user_vote.delete()
    else:
        vote = Vote(user=reddit_user, vote_type=vote_type)
        vote.save()
        thread.votes.add(vote)
    thread.set_score()
    thread.save()
    return redirect("/")


def comment_vote(request, comment_id, vote_type):
    comment = get_object_or_404(ThreadComment, pk=comment_id)
    thread = comment.post_thread
    reddit_user = request.user.reddituser
    user_vote = comment.votes.filter(user=reddit_user)
    if user_vote.exists():
        user_vote.delete()
    else:
        vote = Vote(user=reddit_user, vote_type=vote_type)
        vote.save()
        comment.votes.add(vote)
    comment.set_score()
    comment.save()
    return redirect("threaddetail", thread.id)
