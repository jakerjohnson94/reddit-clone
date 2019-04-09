from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Thread.models import Thread
from ThreadComment.models import ThreadComment
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from RedditUser.urls import urlpatterns as reddit_user_urls
from Subreddit.urls import urlpatterns as subbredit_urls
from Thread.urls import urlpatterns as thread_urls
from ThreadComment.urls import urlpatterns as thread_comment_urls
from Message.models import Message
from MessageThread.models import MessageThread
from Message.urls import urlpatterns as message_urls
from MessageThread.urls import urlpatterns as message_thread_urls
from .views import homepage

admin.site.register(RedditUser)
admin.site.register(Subreddit)
admin.site.register(ThreadComment)
admin.site.register(Thread)
admin.site.register(MessageThread)
admin.site.register(Message)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage, name="homepage"),
]

urlpatterns += reddit_user_urls
urlpatterns += subbredit_urls
urlpatterns += thread_urls
urlpatterns += thread_comment_urls
urlpatterns += message_urls
urlpatterns += message_thread_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
