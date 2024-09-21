from django.shortcuts import render, redirect, HttpResponse
from .models import ShopUser
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# test
def index(request):
    return render(request, 'account/index.html')


# def register(request):
#     if request.user.is_authenticated:
#         return redirect('templates:index')
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             phone = form.cleaned_data['phone']
#             if ShopUser.objects.filter(phone=phone).exists():
#                 messages.error(request, 'phone is exists', 'danger')
#                 return redirect('templates:login')
#             else:
#                 messages.success(request, 'wellcome', 'success')
#                 return redirect('templates:login')
#     else:
#         form = RegisterForm()
#     return render(request, 'account/register.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('templates:login')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if ShopUser.objects.filter(phone=phone).exists():
                messages.error(request, 'phone is exists', 'danger')
                return redirect('templates:login')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f'wellcome ', 'success')

            return redirect('templates:login')

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

                    messages.success(request, f'wellcome {request.user.first_name} {request.user.last_name}', 'success')

                    return redirect('templates:index')
                else:
                    return HttpResponse('Your account is disabled!')
            else:

                messages.error(request, 'name or password is wrong!!!', 'danger')

                messages.error(request, 'wrong phone or password')

                return redirect('templates:login')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def log_out(request):
    logout(request)

    messages.error(request, 'با موفقیت خارج شدید!', 'danger')
    return redirect('templates:index')


def search(request):
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # result = ShopUser.objects.filter(first_name__icontains=query)
            results = ShopUser.objects.filter(phone__iexact=query)
            # result = ShopUser.objects.filter(last_name__icontains=query)
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'account/search.html', {'context': context})
        # return HttpResponse('exit')