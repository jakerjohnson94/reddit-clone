from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ThreadReplyForm
from .models import Message
from MessageThread.models import MessageThread


@login_required
def reply_to_thread_view(request, thread_id):
    thread = get_object_or_404(MessageThread, pk=thread_id)
    form = None
    if request.method == "POST":
        form = ThreadReplyForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data["body"]
            reddit_user = request.user.reddituser
            notifiers = thread.users.filter(~Q(user=request.user))
            new_message = Message.objects.create(body=body, sender=reddit_user)
            new_message.notification.set(notifiers)
            new_message.save()
            thread.messages.add(new_message)
            thread.save()
            return redirect("message_thread_detail", thread_id)
    else:
        form = ThreadReplyForm()

    html = "thread_reply_form_view.html"
    return render(request, html, {"form": form})
