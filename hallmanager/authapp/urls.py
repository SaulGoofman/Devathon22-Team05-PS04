from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginpage/', views.login_page, name='loginpage'),
    path('login', views.user_login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout')
]