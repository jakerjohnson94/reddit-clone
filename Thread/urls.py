from django.contrib import admin
from django.urls import path
from .views import new_thread_view, thread_page_view, delete_thread


urlpatterns = [
    path(
        "r/<str:subreddit_name>/post/<str:post_type>",
        new_thread_view,
        name="newtextthread",
    ),
    path("thread/<int:thread_id>", thread_page_view, name="threaddetail"),
    path("thread/delete/<int:thread_id>", delete_thread, name="threadDelete"),
]
