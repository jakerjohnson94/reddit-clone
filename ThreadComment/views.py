from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ThreadComment
from .forms import PostCommentForm
from Thread.models import Thread
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote
from django.views import View


@login_required
def post_comment(request, thread_id):
    html = "new_thread.html"
    form = None
    if request.method == "POST":
        form = PostCommentForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data["body"]
            reddit_user = get_object_or_404(RedditUser, user=request.user)
            thread = get_object_or_404(Thread, pk=thread_id)
            comment = ThreadComment(
                body=body, sender=reddit_user, post_thread=thread
            )
            comment.save()
            return redirect("threaddetail", thread_id)
    else:
        form = PostCommentForm()

    return render(request, html, {"form": form})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(ThreadComment, pk=comment_id)
    thread = comment.post_thread
    subreddit = thread.subreddit
    is_moderator = subreddit.moderators.filter(user=request.user).exists()
    is_own_post = comment.sender.user is request.user
    if is_moderator or is_own_post:
        comment.delete()
    else:
        return HttpResponseForbidden()
    return redirect("subreddit", subreddit.name)
