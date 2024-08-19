from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def blogs(request):
    return HttpResponse("I am niggaman")

def Folk(request):
    return HttpResponse("am not gey")