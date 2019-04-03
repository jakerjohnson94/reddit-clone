from django.contrib import admin
from django.urls import path
from .views import new_thread_view, thread_detail_view


urlpatterns = [
    path(
        "r/<str:subreddit_name>/post/<str:post_type>",
        new_thread_view,
        name="newtextthread",
    ),
    path("thread/<int:thread_id>", thread_detail_view, name="threaddetail"),
]
