from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=24)
    password = forms.CharField(max_length=50)

