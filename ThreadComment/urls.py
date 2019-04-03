from django.contrib import admin
from django.urls import path
from .views import post_comment, delete_comment


urlpatterns = [
    path("thread/<int:thread_id>/comment", post_comment, name="postcomment"),
    path(
        "comment/<int:coment_id>/delete", delete_comment, name="deleteComment"
    ),
]

