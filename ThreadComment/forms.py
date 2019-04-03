from django import forms
from .models import ThreadComment


class PostCommentForm(forms.Form):
    body = forms.CharField(max_length=500, required=True)

    class Meta:
        model = ThreadComment
        fields = ["body"]

