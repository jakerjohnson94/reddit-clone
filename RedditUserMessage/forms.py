from django import forms
from .models import RedditUserMessage
from RedditUser.models import RedditUser


def get_user_choices():
    choices = []
    all_users = RedditUser.objects.all()
    for user in all_users:
        choices.append((user.user.username, user.user.username))
    print(choices)
    return choices


RECEIVER_CHOICES = get_user_choices()
print(RECEIVER_CHOICES)


class NewMessageForm(forms.Form):
    title = forms.CharField(max_length=40, required=True)
    body = forms.CharField(max_length=500, required=True)

    class Meta:
        model = RedditUserMessage
        fields = ["title", "body"]


class SelectUserForm(forms.Form):
    receiver = forms.CharField(
        label="Select a User to Message",
        widget=forms.Select(
            attrs={"class": "browser-default"}, choices=RECEIVER_CHOICES
        ),
    )
