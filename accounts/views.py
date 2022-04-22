from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import models, get_user_model
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, "registration/register.html")
    elif request.method == 'POST':
        newUser = get_user_model().objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
        newUser.last_name = request.POST['lname']
        newUser.first_name = request.POST['fname']
        newUser.birthdate = request.POST['bdate']
        newUser.save()
        return redirect('/app')
