from django import forms


class User(forms.Form):
    User = forms.CharField(min_length=3, max_length=32, required=True)
    Email = forms.EmailField(max_length=64, required=True)
    Password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=128, required=True)