from django.urls import path
from .views import reply_to_thread_view

urlpatterns = [
    path(
        "message/reply/<int:thread_id>",
        reply_to_thread_view,
        name="reply_to_thread",
    )
]

