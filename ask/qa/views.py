from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello (request):
    return HttpResponse('<h1>Hello QA</h1>')

def test(request, *args, **kwargs):
    return HttpResponse('OK')