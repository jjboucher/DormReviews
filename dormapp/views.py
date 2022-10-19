from django.shortcuts import render
from django.http import HttpResponse
from dormapp.helpers import queries
from dormapp.forms import ResHallReviewForm

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

def dormRoomsPage(request, resHallId):
    form = ResHallReviewForm()
    if request.method=="POST":
        form= ResHallReviewForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'dormRoomList': queries.getDormRooms(resHallId),
        'resHallName': queries.getResHallName(resHallId),
        'form':form
    }
    return render(request, 'dormRooms.html', context)