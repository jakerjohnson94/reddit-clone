from django.urls import path
from .views import login_view, logout_action, create_user_view, change_password
from RedditUser import views

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout", logout_action, name="logout"),
    path("signup/", create_user_view, name="signup"),
    path("edit/password/", change_password, name="change_password"),
]


# endpoints for mvp:
# user/<str:username>
# user/edit
# user/subscriptions
