from django import forms
from .models import Subreddit


class CreateSubredditForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=250, required=True)
    sidebar_content = forms.CharField(max_length=250, required=False)

    class Meta:
        model = Subreddit
        fields = ["name", "description", "sidebar_content"]

