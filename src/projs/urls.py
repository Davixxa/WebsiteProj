from django.conf.urls import url
from .views import (
    proj_list,
    proj_detail,
)

urlpatterns = [

    url(r'^(?P<slug>[\w-]+)/?$', proj_detail, name='detail'),
    url(r'^$', proj_list, name='list'),

]