from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse,HttpResponseBadRequest
import simplejson
from .models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import bcrypt
import jwt
import datetime
from django.conf import settings
import base64
import hashlib
#增加时间戳，判断是否重发token或重新登录
AUTH_EXPORE=8*60*60

def gen_token(user_id):
    '''生成token'''
    print(1)
    return jwt.encode({
        'user_id':user_id,
        'exp':int(datetime.datetime.now().timestamp())+AUTH_EXPORE
    },settings.SECRET_KEY,'HS256').decode()
def authenticate(view):
    def wrapper(request:HttpRequest):
        payload=request.META.get('HTTP_JWT')
        if not payload:
            return HttpResponse(status=401)
        try:
            payload=jwt.decode(payload,settings.SECRET_KEY,algorithms=['HS256'])
            print(payload)
        except:
            return HttpResponse(status=401)
        try:
            user_id=payload.get('user_id',-1)
            user=User.objects.filter(pk=user_id).get()
            request.user=user
        except Exception as e:
            print(e)
            return HttpResponse(status=401)
        ret=view(request)
        return ret
    return wrapper
@csrf_exempt
def reg(request:HttpRequest):
    print(request)
    print(request.POST)
    print(request.body)
    payload=simplejson.loads(request.body)

    try:
        email = payload["email"]
        query=User.objects.filter(email=email)
        print(query)
        print(query.query)
        if query:
            return HttpResponseBadRequest
        name = payload["name"]
        password=payload['password'].encode()
        #password = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password).digest()),bcrypt.gensalt())
        print(email, name, password)
        user=User()
        user.email=email
        user.name=name
        user.password=password
        try:
            user.save()
            return JsonResponse({"user":gen_token(user.id)})#
        except Exception as e:
            raise e
    except Exception as e:
        return HttpResponseBadRequest()
@csrf_exempt
def login(request:HttpRequest):
    payload=simplejson.loads(request.body)
    try:
        email=payload['email']
        user=User.objects.filter(email=email).get()
        print(email)
        # if bcrypt.checkpw(payload['password'].encode(),user.password.encode()):
        print(str(payload['password'].encode())==str(user.password))
        if (str(payload['password'].encode())==str(user.password)):
            token=gen_token(user.id)
            print(token)
            res=JsonResponse({
                'user':{
                    'user_id':user.id,
                    'name':user.name,
                    'email':user.email
                },'token':token
            })
            res.set_cookie('jwt',token)
            return res
        else:
            return HttpResponseBadRequest()
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()