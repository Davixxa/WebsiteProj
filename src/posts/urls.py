from .views import (
#  post_list,
#  post_create,
  post_detail,
#  post_category,
#  post_tags_list,
#  post_update,
#  post_delete,
)
from django.conf.urls import url


urlpatterns = [

    url(r'^(?P<slug>[\w-]+)/?$', post_detail, name='detail'),

]