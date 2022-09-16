from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'signup.html')


def login_page(request):
    return render(request, 'login.html')


@require_POST
def signup(request):
    first_name = request.POST.get('firstname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confpass = request.POST.get('confpass')
    if confpass==password:
        user = User.objects.create_user(username=email,email=email, password=password, first_name=first_name)
        login(request, user)
        print(user)
        return redirect('/dashboard')
    else:
        return render(request, 'signup.html')

@require_POST
def user_login(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect('/dashboard')
    else:
        return redirect('/auth')


def user_logout(request):
    logout(request)
    return redirect('/auth')
