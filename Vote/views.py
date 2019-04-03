from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from ThreadComment.models import ThreadComment
from Thread.models import Thread
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from .models import Vote


def thread_vote(request, thread_id, vote_type):
    thread = get_object_or_404(Thread, pk=thread_id)
    reddit_user = get_object_or_404(RedditUser, user=request.user)
    user_vote = thread.votes.filter(user__user=request.user)
    has_upvoted = False
    has_downvoted = False
    if user_vote.exists():
        if user_vote[0].vote_type == 1:
            has_upvoted = True
        elif user_vote[0].vote_type == 2:
            has_downvoted = True
    else:
        vote = Vote(user=reddit_user, vote_type=vote_type)
        vote.save()
        thread.votes.set([vote])

    return redirect(
        "/",
        {
            "has_upvoted": has_upvoted,
            "has_downvoted": has_downvoted,
            "thread": thread,
        },
    )
