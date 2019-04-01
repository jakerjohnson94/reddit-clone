"""redditclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from redditclone.RedditUser.models import RedditUser
from redditclone.Subreddit.models import Subreddit
from redditclone.MainPost.models import MainPost
from redditclone.Vote.models import Vote
from redditclone.PostComment.models import PostComment

admin.site.register(RedditUser)
admin.site.register(Subreddit)
admin.site.register(PostComment)
admin.site.register(MainPost)
admin.site.register(Vote)

urlpatterns = [path("admin/", admin.site.urls)]
