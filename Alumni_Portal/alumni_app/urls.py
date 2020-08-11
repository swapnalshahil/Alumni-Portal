from django.contrib import admin
from django.urls import path
from alumni_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name='logoutUser'),


]
