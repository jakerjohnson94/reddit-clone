from django.contrib import admin
from django.urls import path
from .views import home_view


urlpatterns = [
    path("subreddit/<int:subreddit_id>", home_view, name="subreddit_home")
]

# subreddit/<int:id>
# subreddit/<int:id>/post
# subreddit/<int:id>/subscribe
# subreddit/<int:id>/unsubscribe

# subreddit/<int:id>create
# subreddit/<int:id>/delete
# subreddit/<int:id>/edit
