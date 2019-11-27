from django.contrib import admin
from django.urls import path,re_path
from .views import reg,login
urlpatterns = [
    re_path(r'^reg/',reg),
    re_path(r'^login/', login)
]