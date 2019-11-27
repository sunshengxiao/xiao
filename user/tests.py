import jwt
key="secret"
token=jwt.encode({"payload":"abc123"},key,"HS256")
print(1,token)
print(2,(jwt.decode(token,key,algorithms="HS256")))
header,payload,signature=token.split(b".")
# Create your tests here.
import base64
def addeq(b:bytes):
    rem=len(b)%4
    return b+(b"="*rem)

print("header=",base64.urlsafe_b64decode(addeq(header)))
print("payload=",base64.urlsafe_b64decode(addeq(payload)))
print("signature=",base64.urlsafe_b64decode(addeq(signature)))
from jwt import algorithms
alg =algorithms.get_default_algorithms()["HS256"]
newkey=alg.prepare_key(key)
signing_input,_,_=token.rpartition(b'.')
print(4,signing_input)
signature=alg.sign(signing_input,newkey)
print(5,signature)
print(6,base64.urlsafe_b64encode(signature))
import json
print(7,base64.urlsafe_b64encode(json.dumps({"payload":"abc123"}).encode()))





import bcrypt
import datetime
password="123456"
print(password.encode())
print(1,bcrypt.gensalt())
print(2,bcrypt.gensalt())
salt=bcrypt.gensalt()
x=bcrypt.hashpw(password.encode(),salt)
print(3,x)
x=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
print(4,x)
print(bcrypt.checkpw(password.encode(),x),len(x))
print(bcrypt.checkpw(password.encode()+b' ',x),len(x))
start=datetime.datetime.now()
y=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
delta=(datetime.datetime.now()-start).total_seconds()
print(delta)

# from django.conf import settings
# print(settings.SECRET_KEY)

