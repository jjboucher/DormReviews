from django.shortcuts import render
from django.http import HttpResponse
from dormapp.helpers import queries
import uuid


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
    #if request.method =='POST':
        #reviewTitle=request.POST['reviewTitle']
        #rating=request.POST['rating']
        #comments=request.POST['comments']

        #queries.addResHallReview(resHallId)

    context = {
        'dormRoomList': queries.getDormRooms(resHallId),
        'resHallName': queries.getResHallName(resHallId),
        'resHallId': resHallId
        
    }
    return render(request, 'dormRooms.html', context)

def addReview(request, resHallId):
    if request.method == 'POST':
        reviewTitle = request.POST['reviewTitle']
        rating = request.POST['rating']
        body = request.POST['comments']
        #resHallId = request.POST['resHallId']

        queries.addResHallReview(resHallId,rating,reviewTitle,body)

        return dormRoomsPage(request,resHallId)