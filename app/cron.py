from .models import *
import fcntl
from django.shortcuts import render,redirect,HttpResponse


def hello_wd(request):
    gm=Games.objects.all().values()
    sp=AdminInfo.objects.get(id=1)
    return render(request,"game.html",{"gm":gm,"sp":sp})