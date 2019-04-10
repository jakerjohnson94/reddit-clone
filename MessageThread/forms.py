from django import forms
from .models import MessageThread
from Message.models import Message
from RedditUser.models import RedditUser


class MessageThreadUserSelectionForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    user = forms.ModelChoiceField(queryset=RedditUser.objects.all(), widget=forms.Select(attrs={'class':'browser-default'}))

    class Meta:
        model = MessageThread
        fields = ["title", "users"]


class MessageThreadComposeForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea, max_length=1000)

    class Meta:
        model = Message
        fields = ["body"]
