from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('hall', views.hallbrief, name='hallbrief'),
    path('requesthall', views.requestForm, name='requestform')
]