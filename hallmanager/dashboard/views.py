from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import SeminarHall
from authapp.models import Nuser
from .forms import RequestForm
# from django.

# Create your views here.


def myaccount(request):
    if request.user.is_authenticated:
        phone = ''
        if len(Nuser.objects.filter(user=request.user))!=0:
            phone = request.user.nuser.phone
        params = {'name':request.user.first_name,'email':request.user.email,'phone': phone}
        return render(request, 'my-account.html', params)
    else:
        redirect('/auth/login')


def dashboard(request):
    if request.user.is_authenticated:
        halls = SeminarHall.objects.all()
        return render(request, 'dashboard.html', {'halls': halls})
    else:
        redirect('/auth/login')


def hallbrief(request):
    # if request.user.is_authenticated:
    hallname = request.GET.get('name')
    hall = get_object_or_404(SeminarHall, name=hallname)
    return render(request, 'hall.html', {'hall': hall})


def requestForm(request):
    # if request.Method == 'POST':

    return render(request, 'requestform.html', {'form': RequestForm(), 'hall': request.GET.get('hall')})