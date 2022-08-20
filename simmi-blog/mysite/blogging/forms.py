from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    class meta:
        model = User
        fields = ('username','password1','password2')

class LoginForm(AuthenticationForm):
    class meta:
        model = User
        fields = ('username','password')        