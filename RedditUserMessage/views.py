from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewMessageForm, SelectUserForm
from .models import RedditUserMessage
from RedditUser.models import RedditUser


def new_message_select_user(request):
    form = None
    if request.method == "POST":
        form = SelectUserForm(request.POST)
        if form.is_valid():
            receiver = form.cleaned_data["receiver"]
            return redirect("newMessageSend", receiver)
    else:
        form = SelectUserForm()
    html = "new_user_message_select_user.html"
    return render(request, html, {"form": form})


def new_message_send(request, receiver_username):
    form = None
    receiver = get_object_or_404(RedditUser, user__username=receiver_username)
    if request.method == "POST":
        form = NewMessageForm(request.POST)
        if form.is_valid():
            sender = request.user.reddituser
            data = form.cleaned_data
            body = data["body"]
            title = data["title"]
            new_message = RedditUserMessage(
                sender=sender,
                receiver=receiver,
                notification=receiver,
                body=body,
                title=title,
            )
            new_message.save()
            return redirect("/")
    else:
        form = NewMessageForm()
    html = "new_user_message.html"
    return render(request, html, {"form": form, "receiver": receiver})


def all_messages_view(request):
    html = "message_list.html"
    messages = RedditUserMessage.objects.filter(sender=request.user.reddituser)
    data = {"messages": messages}
    return render(request, html, data)
