from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse,HttpResponseBadRequest,HttpResponseNotFound
import simplejson
from .models import Content,Post
from user.models import User
from user.views import authenticate
import datetime
import math
# Create your views here.
@authenticate
def pub(request):
    post=Post()#新增
    content=Content()
    try:
        payload=simplejson.loads(request.body)
        post.title=payload['title']
        post.author=User(id=request.user.id)#注入的
        post.postdate=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        post.save()
        content.content=payload['content']
        content.post=post
        content.save()
        return JsonResponse({'post_id':post.id})
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()

def get(request:HttpRequest,id):
    try:
        id=int(id)
        post=Post.objects.get(pk=id)
        print(post,'~~~~~~~~~~')
        if post:
            return JsonResponse({
                'post':{
                    'post_id':post.id,
                    'title':post.title,
                    'author':post.author.name,
                    'postdate':post.postdate.timestamp(),
                    'cotent':post.content.content
                }
            })
    except Exception as e:
        print(e)
        return HttpResponseNotFound()
def validate(d:dict,name:str,type_func,default,validate_func):
    try:
        result=type_func(d.get(name,default))
        result=validate_func(result,default)
    except:
        result=default
    return result
def getall(request:HttpRequest):
    # try:
    #     page=int(request.Get.get('page',1))
    #     page=page if page >0 else 1
    # except:
    #     page=1
    # try:
    #     size=int(request.GET.get('size',20))
    #     size=size if size > 0 and size <101 else 20
    # except:
    #     size =20
    page=validate(request.GET,'page',int,1,lambda x: x if x>0 else 1)
    size=validate(request.GET,'size',int,20, lambda x: x if x>0 and x<101 else 20)
    try:
        start=(page-1)*size
        posts=Post.objects.oder_by('-id')
        print(posts.query)
        count=posts.count()
        posts=posts[start:start+size]
        print(posts.query)
        return JsonResponse({
            "posts":[
                {
                    "post_id":post.id,
                    "title":post.title
                } for post in posts
            ],"pagination":{
            "page":page,
            "size":size,
            "count":count,
            "pages":math.ceil(count/size)
        }
        })
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()
