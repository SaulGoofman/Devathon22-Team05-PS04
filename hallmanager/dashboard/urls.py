from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('myaccount', views.myaccount, name='myaccount')
]