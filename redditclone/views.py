from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote


@login_required
def homepage(request):
    html = "index.html"
    # if request.user is not None:
    #     reddit_user = get_object_or_404(RedditUser, user=request.user)
    #     subscriptions = Subreddit.subscribers.filter(user=reddit_user)
    #     print(subscriptions)
    threads = Thread.objects.all().order_by("-score")[:25]
    for thread in threads:
        if thread.upvoters.filter(user=request.user).exists():
            thread.has_upvoted = True
        elif thread.downvoters.filter(user=request.user).exists():
            thread.has_downvoted = True
    data = {"threads": threads}
    return render(request, html, data)

