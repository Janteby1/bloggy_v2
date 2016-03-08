from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import * 

# from .views import (
# 	Index,
#     User_Register,
#     User_Login,
#     User_Logout,
#     Create_Post,
#     Edit_Post,
#     Delete_Post,
# )


urlpatterns = [
	url(r'^$', Index.as_view(), name='index'),
    url(r'^register$', User_Register.as_view(), name='register'),
    url(r'^login$', User_Login.as_view(), name='login'),
    url(r'^logout$', User_Logout.as_view(), name='logout'),

    url(r'^create$', Create_Post.as_view(), name="create"),
    url(r'^edit/(?P<post_slug>[A-Za-z0-9\-\_]+)$', Edit_Post.as_view(), name="edit"),
    url(r'^delete/(?P<post_slug>[A-Za-z0-9\-\_]+)$', Delete_Post.as_view(), name='delete'),
]
