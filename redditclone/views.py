from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote


class Homepage(TemplateView):
    template_name = "index.html"
