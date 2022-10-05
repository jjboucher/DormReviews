from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {
        'name': 'josh'
    }
    return render(request, "homePage.html",context)