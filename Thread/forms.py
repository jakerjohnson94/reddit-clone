from django import forms
from .models import Thread
from django.forms.widgets import TextInput



class TextThreadForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    body = forms.CharField(max_length=500, required=True)

    class Meta:
        model = Thread
        fields = ["title", "body"]


class LinkThreadForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    link = forms.URLField(required=True, initial="http://", widget=TextInput)

    class Meta:
        model = Thread
        fields = ["title", "link"]
