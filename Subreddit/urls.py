from django.contrib import admin
from django.urls import path
from .views import (

    Home,
    create_new_view,
    subscribe,
    unsubscribe,
    ListAll
)


urlpatterns = [
    path("r/all", ListAll.as_view(), name="allsubs"),
    path("r/create", create_new_view, name="subredditCreate"),
    path("r/<str:subreddit_name>", Home.as_view(), name="subreddit"),
    path("r/<str:subreddit_name>/subscribe", subscribe, name="subscribe"),
    path("r/<str:subreddit_name>/unsubscribe", unsubscribe, name="unsubscribe"),
]

# r/<int:id>/subscribe
# r/<int:id>/unsubscribe

# r/<int:id>/post
# r/<int:id>create
# r/<int:id>/delete
# r/<int:id>/edit
