from django.shortcuts import render
from django.http      import HttpResponse


def index(request):
    return HttpResponse("firs step for all news")
# Create your views here.


