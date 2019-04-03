from django.contrib import admin
from django.urls import path
from RedditUser.urls import urlpatterns as reddit_user_urls
from Subreddit.urls import urlpatterns as subbredit_urls
from Thread.urls import urlpatterns as thread_urls
from ThreadComment.urls import urlpatterns as thread_comment_urls
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Vote.models import Vote
from .views import homepage

admin.site.register(RedditUser)
admin.site.register(Subreddit)
admin.site.register(ThreadComment)
admin.site.register(Thread)
admin.site.register(Vote)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage, name="homepage"),
]

urlpatterns += reddit_user_urls
urlpatterns += subbredit_urls
urlpatterns += thread_urls
urlpatterns += thread_comment_urls
