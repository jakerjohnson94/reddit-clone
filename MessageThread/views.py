from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageThreadUserSelectionForm, MessageThreadComposeForm


from MessageThread.models import MessageThread
from Message.models import Message


def thread_list_view(request):
    reddit_user = request.user.reddituser
    message_threads = MessageThread.objects.filter(users=reddit_user)
    for thread in message_threads:
        thread.active_notification = thread.messages.filter(
            notification=request.user.reddituser
        ).exists()
    data = {"message_threads": message_threads}
    html = "message_thread_list.html"
    return render(request, html, data)


def thread_detail_view(request, thread_id):
    reddit_user = request.user.reddituser
    message_thread = get_object_or_404(MessageThread, pk=thread_id)
    messages = message_thread.messages.all().order_by("-created_at")

    for message in messages:
        if message.notification.filter(user=request.user).exists():
            message.notification.remove(reddit_user)

    data = {"message_thread": message_thread, "messages": messages}
    html = "message_thread_detail.html"
    return render(request, html, data)


def new_message_thread_select_view(request):
    form = None
    if request.method == "POST":
        form = MessageThreadUserSelectionForm(request.POST)
        if form.is_valid():
            users = form.cleaned_data["users"]
            title = form.cleaned_data["title"]
            new_thread = MessageThread(title=title)
            new_thread.save()
            new_thread.users.set([users, request.user.reddituser.id])
            new_thread.save()
            return redirect(f"/message/reply/{new_thread.id}")
    else:
        form = MessageThreadUserSelectionForm()

    html = "message_thread_user_select.html"
    return render(request, html, {"form": form})

