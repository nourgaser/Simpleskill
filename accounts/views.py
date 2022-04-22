from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, "registration/register.html")
    elif request.method == 'POST':
        print(request.POST['fname'])
        context = {
            'error': {
                'message': "You didn't enter the right data"
            }
        }
        return render(request, "registration/register.html", context)
