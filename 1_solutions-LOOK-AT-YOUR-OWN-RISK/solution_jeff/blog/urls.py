from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^register$', User_Register.as_view(), name='register'),
    url(r'^login$', User_Login.as_view(), name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^detail/(?P<pk>[0-9]+)$', Post_Detail.as_view(), name='detail'),
    url(r'^create$', Create_Post.as_view(), name='create'),
    url(r'^delete/(?P<pk>[0-9]+)$', Delete_Post.as_view(), name='delete'),
    url(r'^update/(?P<pk>[0-9]+)$', Update_Post.as_view(), name='update'),
    url(r'^$', Post_List.as_view(), name='list')
]
