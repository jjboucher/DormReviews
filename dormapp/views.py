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

def dormRoomsPage(request, resHallId):
    context = {
        'dormRoomList': queries.getDormRooms(resHallId),
        'resHallReviewList': queries.getResHallReviews(resHallId),
        'resHallName': queries.getResHallName(resHallId),
        'resHallId': resHallId
        
    }
    return render(request, 'dormRooms.html', context)

def addReview(request, resHallId):
    if request.method == 'POST':
        reviewTitle = request.POST['reviewTitle']
        rating = request.POST['rating']
        body = request.POST['comments']

        queries.addResHallReview(resHallId,rating,reviewTitle,body)

        return dormRoomsPage(request,resHallId)

def addPhoto(request, resHallId):
    if request.method == 'POST':
        photo = request.POST.get('myPhoto', False)

        queries.addResHallPhoto(resHallId, photo)

        return dormRoomsPage(request,resHallId)