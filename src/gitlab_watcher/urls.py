from django.conf.urls import url
from .views import (
    gitlab_detail,
)

urlpatterns = [

    url(r'^(?P<slug>[\w-]+)/?$', gitlab_detail, name='detail'),

]