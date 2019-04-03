from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from ThreadComment.models import ThreadComment
from Thread.models import Thread
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from .models import Vote


def get_vote_score(votes):
    score = 0
    for vote in votes:
        if vote.vote_type == 1:
            score += 1
        elif vote.vote_type == 2:
            score -= 1
    return score


def thread_vote(request, thread_id, vote_type):
    thread = get_object_or_404(Thread, pk=thread_id)
    reddit_user = get_object_or_404(RedditUser, user=request.user)
    user_vote = thread.votes.filter(user=reddit_user)
    if user_vote.exists():
        user_vote.delete()
    else:
        vote = Vote(user=reddit_user, vote_type=vote_type)
        vote.save()
        thread.votes.set([vote])
    thread.score = get_vote_score(thread.votes.all())
    thread.save()
    return redirect("/")
