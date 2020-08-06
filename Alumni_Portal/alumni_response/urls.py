from django.contrib import admin
from django.urls import path, re_path ,include
from . import views

app_name='alumni_response'

urlpatterns=[
    path('form1/',views.response1,name='form1'),
    path('form2a/',views.response2a,name='form2a'),
    path('form2b/',views.response2b,name='form2b'),
    path('form2c/',views.response2c,name='form2c'),
    path('form3/',views.response3,name='form3'),
    re_path(r'^form_update/(?P<pk>\d+)/$', views.update_current, name='form_update'),
]
