from django.conf.urls import url
from .views import (
    Index,
    Post_Add,
    Post_Edit,
    Post_Delete,
    Post_Details,
    User_Index,
)

import blog.views

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^user$', User_Index.as_view(), name='user'),
    url(r'^add$', Post_Add.as_view(), name='add'),     
    url(r'^edit/(?P<id>[0-9]{1,})$', Post_Edit.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]{1,})$', Post_Delete.as_view(), name='delete'),
    url(r'^details/(?P<id>[0-9]{1,})$', Post_Details.as_view(), name='details'),
]
