from django.contrib import admin
from django.urls import path
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from RedditUserMessage.models import RedditUserMessage
from RedditUserMessage.urls import urlpatterns as reddit_user_message_urls
from Subreddit.models import Subreddit
from RedditUser.urls import urlpatterns as reddit_user_urls
from Subreddit.urls import urlpatterns as subbredit_urls
from Thread.urls import urlpatterns as thread_urls
from ThreadComment.urls import urlpatterns as thread_comment_urls


from .views import homepage

admin.site.register(RedditUser)
admin.site.register(RedditUserMessage)
admin.site.register(Subreddit)
admin.site.register(ThreadComment)
admin.site.register(Thread)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage, name="homepage"),
]

urlpatterns += reddit_user_urls
urlpatterns += reddit_user_message_urls
urlpatterns += subbredit_urls
urlpatterns += thread_urls
urlpatterns += thread_comment_urls

