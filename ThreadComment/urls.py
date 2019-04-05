from django.contrib import admin
from django.urls import path
from .views import post_comment, delete_comment, comment_vote


urlpatterns = [
    path("thread/<int:thread_id>/comment", post_comment, name="postcomment"),
    path(
        "comment/<int:comment_id>/delete", delete_comment, name="deleteComment"
    ),
    path(
        "comment/<int:comment_id>/vote/<int:vote_type>",
        comment_vote,
        name="commentVote",
    ),
]

