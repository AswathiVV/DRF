from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse
# Create your views here.

def sample_fun(req):
    d=Projectuser.objects.all()
    s=sample(d,many=True)
    return JsonResponse(s.data,safe=False)

def fun1(req):
    if req.method=='GET':
        d=Projectuser.objects.all()
        s=model_serializer(d,many=True)
        return JsonResponse(s.data,safe=False)

