from django.contrib import admin
from django.urls import path
from .views import Homepage
from RedditUser.urls import urlpatterns as reddit_user_urls

from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote

admin.site.register(RedditUser)
admin.site.register(Subreddit)
admin.site.register(ThreadComment)
admin.site.register(Thread)
admin.site.register(Vote)

urlpatterns = [path("admin/", admin.site.urls), path("", Homepage.as_view())]

urlpatterns += reddit_user_urls
