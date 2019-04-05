from django.contrib import admin
from django.urls import path
from .views import login_view, logout_action, create_user_view


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout", logout_action, name="logout"),
    path("signup/", create_user_view, name="signup"),
]


# endpoints for mvp:
# user/<str:username>
# user/edit
# user/subscriptions
