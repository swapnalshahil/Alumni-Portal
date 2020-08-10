from django.contrib import admin
from django.urls import path, re_path ,include
from . import views

app_name='alumni_response'

urlpatterns=[
    path('form1/',views.response1,name='form1'),
    re_path(r'^form2a/(?P<pk>\d+)/$',views.response2a,name='form2a'),
    re_path(r'^form2b/(?P<pk>\d+)/$',views.response2b,name='form2b'),
    re_path(r'^form2c/(?P<pk>\d+)/$',views.response2c,name='form2c'),
    re_path(r'^form3/(?P<pk>\d+)/$',views.response3,name='form3'),
    re_path(r'^detail/(?P<pk>\d+)/$', views.AlumniDetail.as_view(template_name='alumni_response/alum_detail.html'),name='alumni_detail'),
    re_path(r'^form_update/(?P<pk>\d+)/$', views.update_current, name='form_update'),

]
