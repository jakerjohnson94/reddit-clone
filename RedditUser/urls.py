from django.contrib import admin
from django.urls import path
from .views import login_view, logout_action


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout", logout_action, name="logout"),
]


# endpoints for mvp:
# user/<str:username>
# user/edit
# user/subscriptions
