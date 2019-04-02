from django.contrib import admin
from django.urls import path
from .views import home_view


urlpatterns = [path("r/<str:subreddit_name>", home_view, name="subreddit")]

# r/<int:id>/subscribe
# r/<int:id>/unsubscribe

# r/<int:id>/post
# r/<int:id>create
# r/<int:id>/delete
# r/<int:id>/edit
