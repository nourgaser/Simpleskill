from django.shortcuts import render
from django.http import Http404, HttpResponse
from app.models import *

# Create your views here.
def index(request):
    user = request.user
    print(user.username)
    data = Simpleskill.objects.all()
    context = {
        'data': data,
        'user': user,
    }
    return render(request, 'website/index.html', context=context)