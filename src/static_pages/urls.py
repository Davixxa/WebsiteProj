from django.conf.urls import url
from .views import (
    index,
    about,
    redirect_view
)

from .feeds import RSS

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'about/?', about, name='about'),
    url(r'^rss/?', RSS(), name='rss'),
    url(r'^r/(?P<slug>[\w-]+)/?$', redirect_view, name='redirect')

]