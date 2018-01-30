from django.conf.urls import url
from .views import (
    index,
    about
)

from .feeds import RSS

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'about/?', about, name='about'),
    url(r'^rss/?', RSS(), name='rss'),
]