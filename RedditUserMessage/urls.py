from django.contrib import admin
from django.urls import path
from .views import all_messages_view, new_message_send, new_message_select_user

# from .views import


urlpatterns = [
    path("messages/all", all_messages_view, name="allMessages"),
    path(
        "messages/send/select", new_message_select_user, name="newMessageSelect"
    ),
    path(
        "messages/send/<str:receiver_username>",
        new_message_send,
        name="newMessageSend",
    ),
]

