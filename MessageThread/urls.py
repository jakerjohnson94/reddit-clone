from django.urls import path
from .views import (
    thread_list_view,
    thread_detail_view,
    new_message_thread_select_view,
)

urlpatterns = [
    path("messages/all/", thread_list_view, name="all_messages"),
    path(
        "messages/<int:thread_id>",
        thread_detail_view,
        name="message_thread_detail",
    ),
    path(
        "messages/new/",
        new_message_thread_select_view,
        name="message_thread_select",
    ),
]

