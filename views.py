from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, TutorRegisterForm
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + username)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('first_app/home')


def logout_view(request):
    logout(request)
    return redirect('first_app/home')

def login_error(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login_error.html')

def tutor_registration(request):
    if request.method == 'POST':
        form = TutorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    else:
        form = TutorRegisterForm()
    return render(request, 'users/tutorregister.html', {'form':form})
    
