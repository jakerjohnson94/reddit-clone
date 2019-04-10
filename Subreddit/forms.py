from django import forms
from django.forms import ModelForm
from .models import Subreddit


class CreateSubredditForm(ModelForm):
    class Meta:
        model = Subreddit
        fields = ["name", "description", "sidebar_content"]

