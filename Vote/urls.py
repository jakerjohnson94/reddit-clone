from django.contrib import admin
from django.urls import path
from .views import thread_vote


urlpatterns = [
    path(
        "thread/<int:thread_id>/vote/<int:vote_type>",
        thread_vote,
        name="threadVote",
    )
]
