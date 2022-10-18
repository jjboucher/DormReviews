from django.shortcuts import render
from django.http import HttpResponse
from dormapp.helpers import queries

# Create your views here.

def index(request):
    context = {
        'universitiesList': queries.getUniversities()
    }
    return render(request, "homePage.html", context)

def resHallsPage(request):
    universityId=request.POST.get('universities')

    context = {
        'resHallsList': queries.getResHalls(universityId),
        'universityName': queries.getUniversityName(universityId)
    }
    return render(request, 'resHalls.html', context)

def dormRoomsPage(request):
    universityId=request.POST.get()
    context = {
        'dormRoomList': queries.getDormRooms(request.resHallId)
    }
    return render(request, 'dormRooms.html', context)