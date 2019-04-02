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
from RedditUser.models import RedditUser
from Subreddit.models import Subreddit
from Thread.models import Thread
from Vote.models import Vote
from ThreadComment.models import ThreadComment
from .views import Homepage


admin.site.register(RedditUser)
admin.site.register(Subreddit)
admin.site.register(ThreadComment)
admin.site.register(Thread)
admin.site.register(Vote)

urlpatterns = [path("admin/", admin.site.urls), path("", Homepage.as_view())]
