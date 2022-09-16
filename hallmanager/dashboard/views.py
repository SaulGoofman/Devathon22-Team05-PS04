from django.shortcuts import render, HttpResponse
from .models import SeminarHall

# Create your views here.


def myaccount(request):
    params = {'name':request.user.first_name,'email':request.user.email}
    return render(request, 'my-account.html', params)


def dashboard(request):
    halls = SeminarHall.objects.all()
    return render(request, 'dashboard.html', {'halls': halls})