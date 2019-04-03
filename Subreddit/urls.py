from django.contrib import admin
from django.urls import path
from .views import home_view, list_all_view, subscribe, unsubscribe


urlpatterns = [
    path("r/all", list_all_view, name="allsubs"),
    path("r/<str:subreddit_name>", home_view, name="subreddit"),
    path("r/<str:subreddit_name>/subscribe", subscribe, name="subscribe"),
    path("r/<str:subreddit_name>/unsubscribe", unsubscribe, name="unsubscribe"),
]

# r/<int:id>/subscribe
# r/<int:id>/unsubscribe

# r/<int:id>/post
# r/<int:id>create
# r/<int:id>/delete
# r/<int:id>/edit
