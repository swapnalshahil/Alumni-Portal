from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    class Meta():
        model=User
        fields=('username','email','password')
