"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf.urls import url
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.shortcuts import render
from user.views import reg
def index(request):
    d={"a":1,"b":2,"v":3}
    return render(request,'index1.html',{'dct':d})
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^index/$',index),
    path(r'',index),
    re_path(r'^user/',include("user.urls")),
    re_path(r'^post/',include("post.urls"))
]
