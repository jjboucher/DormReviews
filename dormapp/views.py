from django.shortcuts import render
from django.http import HttpResponse
from dormapp.helpers import queries
from django.shortcuts import redirect


# Create your views here.

def index(request):
    context = {
        'universitiesList': queries.getUniversities()
    }
    return render(request, "homePage.html", context)

def addUniversityPage(request):
    if request.method == 'POST':
        name = request.POST['name']

        queries.addUniversity(name)
        return redirect('/dormapp/')
        #return index(request)

def resHallsPage(request, universityId):

    context = {
        'resHallsList': queries.getResHalls(universityId),
        'universityName': queries.getUniversityName(universityId),
        'universityId': universityId
    }
    return render(request, 'resHalls.html', context)

def addResHallPage(request, universityId):
    if request.method == 'POST':
        name = request.POST['name']

        queries.addResHall(universityId, name)
        
        return redirect(f'/dormapp/{universityId}/resHalls')

def dormRoomsPage(request, resHallId):
    resHallPhotos = queries.getResHallPhotos(resHallId)

    context = {
        'dormRoomList': queries.getDormRooms(resHallId),
        'resHallReviewList': queries.getResHallReviews(resHallId),
        'resHallName': queries.getResHallName(resHallId),
        'resHallPhotos': resHallPhotos,
        'photoCount': resHallPhotos.count(),
        'resHallId': resHallId
        
    }
    return render(request, 'dormRooms.html', context)

def addDormRoomPage(request, resHallId):
    if request.method == 'POST':
        roomNumber = request.POST['roomNumber']

        queries.addDormRoom(resHallId, roomNumber)

        return redirect(f'/dormapp/{resHallId}/dormRooms')

def dormReviewsPage(request, dormId):
    dormPhotos = queries.getDormPhotos(dormId)

    context = {
        'dormReviewList': queries.getDormReviews(dormId),
        'dormName': queries.getDormName(dormId),
        'dormPhotos': dormPhotos,
        'photoCount': dormPhotos.count(),
        'dormId': dormId
    }
    return render(request, 'dormReviews.html', context)

def addReview(request, resHallId):
    if request.method == 'POST':
        reviewTitle = request.POST['reviewTitle']
        rating = request.POST['rating']
        body = request.POST['comments']

        queries.addResHallReview(resHallId,rating,reviewTitle,body)

        return redirect(f'/dormapp/{resHallId}/dormRooms')

def addDormReviewPage(request,dormId):
    if request.method == 'POST':
        reviewTitle = request.POST.get('reviewTitle')
        rating = request.POST.get('rating')
        body = request.POST.get('comments')
        # dormId = request.POST.get('dormId')

        queries.addDormRoomReview(dormId,rating,reviewTitle,body)

        return redirect(f'/dormapp/{dormId}/reviews')

def addResHallPhoto(request, resHallId):
    if request.method == 'POST':
        
        photo = request.FILES.get('myPhoto', False)
        assert(photo)
        queries.addResHallPhoto(resHallId, photo)

        return redirect(f'/dormapp/{resHallId}/dormRooms')

def addDormRoomPhoto(request, dormRoomId):
    if request.method == 'POST':
        photo = request.FILES.get('myPhoto', False)
        assert(photo)
        queries.addDormRoomPhoto(dormRoomId, photo)

        return redirect(f'/dormapp/{dormRoomId}/reviews')