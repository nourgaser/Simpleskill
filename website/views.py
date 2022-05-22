from django.shortcuts import render
from django.http import Http404, HttpResponse
from app.models import *

# Create your views here.
def index(request):
    data = Simpleskill.objects.all()
    context = {
        'data': data
    }
    if (request.user.is_authenticated):
        context["user"] = request.user
    return render(request, 'website/index.html', context=context)

def about(request):
    return render(request, 'website/about.html', context={'user': request.user})

def field(request, field_id):
    field = Category.objects.get(id=field_id)
    simpleskills = []

    tags = field.tags.all()

    for tag in tags:
        simpleskills.append(tag.simpleskills.all())

    context = {
        "field": field,
        "simpleskills":  simpleskills
    }

    if (request.user.is_authenticated):
        context["user"] = request.user
    return render(request, 'website/field.html', context=context)