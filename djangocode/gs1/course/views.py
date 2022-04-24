from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  learn_django(request):
    return HttpResponse('Hello Djnago')

def  learn_ptyhon(request):
    return HttpResponse('<h1>Hello Python</h1>')