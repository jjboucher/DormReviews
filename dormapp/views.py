from django.shortcuts import render
from django.http import HttpResponse
from dormapp.helpers import queries
from django.shortcuts import redirect


# All views in the webapp.

## index(HttpRequest request)
## This view represents the homepage. It will contain a list of
## all universities contained within the database for user selection,
## as well as the function to add a new unrepresented university.
## Associated with homePage.html.
## url: ''
def index(request):
    context = {
        'universitiesList': queries.getUniversities()
    }
    return render(request, "homePage.html", context)

## addUniversityPage(HttpRequest request)
## This view represents the resulting page when a user uploads
## a new university using the form from homePage.html.
## url: '/addUniversityPage
def addUniversityPage(request):
    if request.method == 'POST':
        name = request.POST['name']

        queries.addUniversity(name)
        return redirect('/dormapp/')
        #return index(request)

## resHallsPage(HttpRequest request, uuid universityId)
## View that retrieves a Residence Hall page according to the given
## uuid universityId. 
## Associated with resHalls.html
## url: '<uuid:universityId>/resHalls'
def resHallsPage(request, universityId):

    context = {
        'resHallsList': queries.getResHalls(universityId),
        'universityName': queries.getUniversityName(universityId),
        'universityId': universityId
    }
    return render(request, 'resHalls.html', context)

## addResHallPage(HttpRequest request, uuid universityId)
## View that adds a new Residence Hall page according to the form on
## resHalls.html. The new resHall object is created according to the 
## form data and the uuid universityId passed in by the page.
## url: '<uuid:universityId>/addResHall'
def addResHallPage(request, universityId):
    if request.method == 'POST':
        name = request.POST['name']

        queries.addResHall(universityId, name)
        
        return redirect(f'/dormapp/{universityId}/resHalls')

## dormRoomsPage(HttpRequest request, uuid resHallId)
## View that retrieves a Dorm Room page according to the given uuid
## resHallId. 
## To clarify: This page will show all of the dorm rooms within the 
## given res hall.
## Associated with dormRooms.html
## url: '<uuid:resHallId>/dormRooms'
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

## addDormRoomPage(HttpRequest request, uuid resHallId)
## View that inserts a new dormRoom object into the database according
## to the filled-out form from dormRooms.html.
## url: '<uuid:resHallId>/addDormRoom'
def addDormRoomPage(request, resHallId):
    if request.method == 'POST':
        roomNumber = request.POST['roomNumber']

        queries.addDormRoom(resHallId, roomNumber)

        return redirect(f'/dormapp/{resHallId}/dormRooms')

## dormReviewsPage(HttpRequest request, uuid dormId)
## View that retrieves a page according to the given uuid dormId which
## will display all of the photos and reviews associated with that dorm
## room. 
## Associated with dormReviews.html
## url: '<uuid:dormId>/reviews'
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

## addReview(HttpRequest request, uuid resHallId)
## View that inserts a new ResHallReview object into the database according
## to the formdata from the reviewForm form within dormRooms.html.
## url: '<uuid:resHallId>/addReview'
def addReview(request, resHallId):
    if request.method == 'POST':
        reviewTitle = request.POST['reviewTitle']
        rating = request.POST['rating']
        body = request.POST['comments']

        queries.addResHallReview(resHallId,rating,reviewTitle,body)

        return redirect(f'/dormapp/{resHallId}/dormRooms')

## addDormReviewPage(HttpRequest request, uuid dormId)
## View that inserts a new DormRoomReview object into the database according
## to the formdata from the reviewForm dormReviews.html.
## url: '<uuid:dormId>/addDormReview'
def addDormReviewPage(request,dormId):
    if request.method == 'POST':
        reviewTitle = request.POST.get('reviewTitle')
        rating = request.POST.get('rating')
        body = request.POST.get('comments')
        # dormId = request.POST.get('dormId')

        queries.addDormRoomReview(dormId,rating,reviewTitle,body)

        return redirect(f'/dormapp/{dormId}/reviews')

## addResHallPhoto(HttpRequest request, uuid resHallId)
## View that inserts a new ResHallPhoto object into the database according
## to the formdata from the photoForm within dormRooms.html.
## url: '<uuid:resHallId>/addResHallPhoto'
def addResHallPhoto(request, resHallId):
    if request.method == 'POST':
        
        photo = request.FILES.get('myPhoto', False)
        assert(photo)
        queries.addResHallPhoto(resHallId, photo)

        return redirect(f'/dormapp/{resHallId}/dormRooms')

## addDormRoomPhoto(HttpRequest request, uuid dormRoomId)
## View that inserts a new DormRoomPhoto object into the database according
## to the formdata from the photoForm within dormReviews.html.
## url: '<uuid:dormRoomId>/addDormRoomPhoto'
def addDormRoomPhoto(request, dormRoomId):
    if request.method == 'POST':
        photo = request.FILES.get('myPhoto', False)
        assert(photo)
        queries.addDormRoomPhoto(dormRoomId, photo)

        return redirect(f'/dormapp/{dormRoomId}/reviews')