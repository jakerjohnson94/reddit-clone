from django import forms
from .models import Message


class ThreadReplyForm(forms.Form):
    body = forms.CharField(max_length=1000, required=True)

    class Meta:
        model = Message
        fields = ["body"]

