from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from backendApp.Services.walletService import WalletService
from .forms import SignupForm, LoginForm


walletService = WalletService()
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
@login_required(login_url='login')
def my_stories(request):
    return render(request, 'mystories.html')

@login_required(login_url='login')
def story(request, id):
    return render(request, 'storyPage.html')

def user_register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            obj = form.save()
            walletService.create_new_wallet(obj.pk)
            messages.success(request, 'User created successfully!')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Username or password is incorrect. Try again!")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')