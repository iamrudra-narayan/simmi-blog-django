from .models import RegisterUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class meta:
        model = RegisterUser
        fields = ('username','email','password1','password2')
        labels = {'email': 'Your Email Id',} 

class LoginForm(AuthenticationForm):
    class meta:
        model = RegisterUser
        fields = ('username','password') 
               