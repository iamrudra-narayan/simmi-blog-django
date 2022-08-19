from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .models import User

# Create your views here.

def home(request):
    return render(request, "index.html")

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login/')
	form = UserCreationForm()    		
	return render (request, "register.html", {"form":form})
    
def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/home/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"form":form})    

def account(request):
    return HttpResponse("Hello tracker")  

def logout(request):
    return HttpResponse("Hello Checkout")
