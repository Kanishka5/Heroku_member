from django.contrib.auth.models import User
from django import forms


class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
#    email=forms.EmailField(label="Email address")
#    email2=forms.EmailField(label='confirm Email')
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'email',
        'username',
        'password'
        ]
