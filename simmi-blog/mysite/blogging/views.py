from re import L
from urllib import request, response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, LoginForm
from django.contrib import messages
from .models import User, Post
from django.contrib.auth.models import User, auth

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "index.html",{'posts':posts})

def register(request):
	if request.method == "POST":
		fm = RegistrationForm(request.POST)
		if fm.is_valid():
			username = fm.cleaned_data['username']
			password = fm.cleaned_data['password1']
			user = User(username=username,password=password)
			user.save()
			return redirect('/login/') 

	else:
		fm = RegistrationForm()			   		
	return render (request, "register.html", {"form":fm})


def login(request):
    if request.method == "POST":

        user = authenticate(request, username = request.POST['username'],
                        password = request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('/account/')

        else:
            messages.error(request, "Either your email or password is wrong!")
            return redirect('/login/')

    return render(request, 'login.html')  

@login_required
def account(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
          
        return render(request, "account.html") 

def logout(request):
	logout(request)
	return redirect("/login/")
