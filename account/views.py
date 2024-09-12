from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import ShopUser
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# test
def index(request):
    return render(request, 'account/index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('templates:index')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if ShopUser.objects.filter(phone=phone).exists():
                messages.error(request, 'phone is exists')
                return redirect('templates:index')
            else:
                return HttpResponse('خوش آمدید')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['phone'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('templates:index')
                else:
                    return HttpResponse('Your account is disabled!')
            else:
                messages.error(request, 'wrong phone or password')
                return redirect('templates:login')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def log_out(request):
    logout(request)
    return HttpResponse('exit')
