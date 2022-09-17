from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import SeminarHall, Request
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
        redirect('/auth/')


def dashboard(request):
    if request.user.is_authenticated:
        halls = SeminarHall.objects.all()
        return render(request, 'dashboard.html', {'halls': halls})
    else:
        return redirect('/auth/login')


def hallbrief(request):
    # if request.user.is_authenticated:
    hallname = request.GET.get('name')
    hall = get_object_or_404(SeminarHall, name=hallname)
    return render(request, 'hall.html', {'hall': hall})


def requestForm(request):
    if request.method == 'POST':
        f = RequestForm(request.POST, request.FILES)
        if f.is_valid():
            print(request.POST.get('hall'))
            hall = SeminarHall.objects.get(name=request.POST.get('hall'))
            print(f.fields['startTime'])
            newreq = Request(user=request.user, hall=hall, startTime=str(f.fields['startTime']), endTime=str(f.fields['startTime']))
            newreq.save()
            # newreq = f.save()
            # newreq.user = request.user
            # newreq.hall = SeminarHall.objects.get(name = request.POST.get('hall'))
            # newreq.save()
            return redirect('/dashboard')
        else:
            print('form is invalid')
    return render(request, 'requestform.html', {'form': RequestForm(), 'hall': request.GET.get('hall')})


def mybooking(request):
    if request.user.is_authenticated:
        hallrequests = Request.objects.filter(user = request.user)
        return render(request, 'my-bookings.html', {'reqs': hallrequests})
    else:
        redirect('/auth')