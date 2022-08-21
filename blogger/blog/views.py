from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "index.html",{'posts':posts})

def register(request):
    if request.user.is_authenticated:
      return redirect("/account/")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your Account has been created {username}. Please Login it.")
            return redirect('/login/')
        else:
            messages.error(request, f"Register Again.")    
    else:
        form = RegistrationForm()
	
    return render (request, "register.html", {"form":form})


def login(request):
    if request.user.is_authenticated:
      return redirect("/account/")
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome Back {username}")
                return redirect('/account/')
            else:
                messages.error(request, f"Either your email or password is wrong!")
                return redirect('/login/', {'messages':messages})    

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

@login_required
def account(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:   
        return render(request, "account.html") 

def logout_user(request):
	logout(request)
	return redirect("/login/")

