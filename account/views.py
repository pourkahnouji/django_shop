from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import ShopUser
from .forms import *
from django.contrib import messages

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
