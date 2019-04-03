from django.contrib import admin
from django.urls import path
from .views import post_comment


urlpatterns = [
    path("thread/<int:thread_id>/comment", post_comment, name="postcomment")
]

