from django.conf.urls import re_path
from .views import pub,get,getall

urlpatterns = [
    re_path(r'^pub$',pub),
    re_path(r'^(\d+)', get),
    re_path(r'^$', getall),
]
