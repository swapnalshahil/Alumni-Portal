from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns=[
    path('signup/', views.SignupView, name='user_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
]
