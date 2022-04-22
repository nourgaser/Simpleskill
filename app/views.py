from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello from app:index!")

def choose_categories(request):
    return HttpResponse("Hello from app:choose_categories!")

def experience_level(request):
    return HttpResponse("Hello from app:experience_level!")

def interest_level(request):
    return HttpResponse("Hello from app:interest_level!")

def dashboard(request):
    return HttpResponse("Hello from app:dashboard!")

def learn(request, ssid):
    res = "Hello from app:learn! You are learning: %s" % Simpleskill.objects.get(id=ssid) 
    return HttpResponse(res)

def explore(request):
    return HttpResponse("Hello from app:explore!")
