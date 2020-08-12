from django.contrib import admin
from django.urls import path
from alumni_app import views

urlpatterns = [
  path('', views.home, name='home'),
  # TEMPORARY
  path('signin', views.sign_in, name='signin'),
  path('signout', views.home, name='signout'),
  path('calendar', views.home, name='calendar'),
  path('callback', views.callback, name='callback'),

]
