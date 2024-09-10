from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form =UserRegistrationForm()

    return render(request ,'users/register.html' ,{'form':form})


def logout_user(request):
    logout(request)
    return redirect('login')

def login_user(request):
    if request.method =='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            
        else:
            messages.success(request , 'Username and Password is invalid . Try again !! ')
    return render (request , 'users/login.html')