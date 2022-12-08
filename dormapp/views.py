from django.shortcuts import render
from dormapp.helpers import queries
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
import dormapp.models as m

message = ''

# All views in the webapp.

## homePage(HttpRequest request)
## This view represents the homepage. It will contain a list of
## all universities contained within the database for user selection,
## as well as the function to add a new unrepresented university.
## Associated with homePage.html.
## url: ''
def homePage(request):
    global message
    context = {
        'universitiesList': queries.getUniversities(),
        'message': message #kwargs.get('message', '')
    }
    message = ''
    return render(request, "homePage.html", context)

## addUniversityPage(HttpRequest request)
## This view represents the resulting page when a user uploads
## a new university using the form from homePage.html.
## url: '/addUniversityPage
def addUniversityPage(request):
    global message
    if request.method == 'POST':
        name = request.POST.get('name', None)
        photo = request.FILES.get('myPhoto', False)

        newUniversity = queries.addUniversity(name)
        successPhoto = queries.addUniversityPhoto(newUniversity, photo)
        message = '' if newUniversity else 'Invalid university name'
        

        return redirect('dormapp:homePage')
        #return index(request)

## resHallsPage(HttpRequest request, uuid universityId)
## View that retrieves a Residence Hall page according to the given
## uuid universityId. 
## Associated with resHalls.html
## url: '<uuid:universityId>/resHalls'
def resHallsPage(request, universityId):
    global message
    context = {
        'resHallsList': queries.getResHalls(universityId),
        'universityName': queries.getUniversityName(universityId),
        'universityId': universityId,
        'backUrl': '/dormapp/',
        'message': message
    }
    message = ''
    return render(request, 'resHalls.html', context)

## addResHallPage(HttpRequest request, uuid universityId)
## View that adds a new Residence Hall page according to the form on
## resHalls.html. The new resHall object is created according to the 
## form data and the uuid universityId passed in by the page.
## url: '<uuid:universityId>/addResHall'
def addResHallPage(request, universityId):
    global message
    if request.method == 'POST':
        name = request.POST['name']

        success = queries.addResHall(universityId, name)
        message = '' if success else 'Invalid residence hall name'

        return redirect('dormapp:resHallsPage', universityId=universityId)

## dormRoomsPage(HttpRequest request, uuid resHallId)
## View that retrieves a Dorm Room page according to the given uuid
## resHallId. 
## To clarify: This page will show all of the dorm rooms within the 
## given res hall.
## Associated with dormRooms.html
## url: '<uuid:resHallId>/dormRooms'
def dormRoomsPage(request, resHallId):
    global message
    resHallPhotos = queries.getResHallPhotos(resHallId)
    universityId = m.ResHall.objects.get(id=resHallId).university.id
    context = {
        'dormRoomList': queries.getDormRooms(resHallId),
        'resHallReviewList': queries.getResHallReviews(resHallId),
        'resHallName': queries.getResHallName(resHallId),
        'resHallPhotos': resHallPhotos,
        'photoCount': resHallPhotos.count(),
        'resHallId': resHallId,
        'backUrl': f'/dormapp/{universityId}/resHalls',
        'message': message
    }
    message = ''
    return render(request, 'dormRooms.html', context)

## addDormRoomPage(HttpRequest request, uuid resHallId)
## View that inserts a new dormRoom object into the database according
## to the filled-out form from dormRooms.html.
## url: '<uuid:resHallId>/addDormRoom'
def addDormRoomPage(request, resHallId):
    global message
    if request.method == 'POST':
        roomNumber = request.POST['roomNumber']

        success = queries.addDormRoom(resHallId, roomNumber)
        message = '' if success else 'Invalid dorm room number'
        return redirect('dormapp:dormRoomsPage', resHallId=resHallId)

## dormReviewsPage(HttpRequest request, uuid dormId)
## View that retrieves a page according to the given uuid dormId which
## will display all of the photos and reviews associated with that dorm
## room. 
## Associated with dormReviews.html
## url: '<uuid:dormId>/reviews'
def dormReviewsPage(request, dormId):
    global message
    dormPhotos = queries.getDormPhotos(dormId)
    resHallId = m.DormRoom.objects.get(id=dormId).resHall.id
    context = {
        'dormReviewList': queries.getDormReviews(dormId),
        'dormName': queries.getDormName(dormId),
        'dormPhotos': dormPhotos,
        'photoCount': dormPhotos.count(),
        'dormId': dormId,
        'backUrl': f'/dormapp/{resHallId}/dormRooms',
        'message': message
    }
    message = ''
    return render(request, 'dormReviews.html', context)

## addReview(HttpRequest request, uuid resHallId)
## View that inserts a new ResHallReview object into the database according
## to the formdata from the reviewForm form within dormRooms.html.
## url: '<uuid:resHallId>/addReview'
def addReview(request, resHallId):
    global message
    if request.method == 'POST':
        reviewTitle = request.POST['reviewTitle']
        rating = request.POST['rating']
        body = request.POST['comments']

        success = queries.addResHallReview(resHallId,rating,reviewTitle,body)
        message = '' if success else 'Invalid review input'
        return redirect('dormapp:dormRoomsPage', resHallId)

## addDormReviewPage(HttpRequest request, uuid dormId)
## View that inserts a new DormRoomReview object into the database according
## to the formdata from the reviewForm dormReviews.html.
## url: '<uuid:dormId>/addDormReview'
def addDormReviewPage(request,dormId):
    global message
    if request.method == 'POST':
        reviewTitle = request.POST.get('reviewTitle')
        rating = request.POST.get('rating')
        body = request.POST.get('comments')
        # dormId = request.POST.get('dormId')

        success = queries.addDormRoomReview(dormId,rating,reviewTitle,body)
        message = '' if success else 'Invalid review input'
        return redirect('dormapp:dormReviewsPage', dormId)

## addResHallPhoto(HttpRequest request, uuid resHallId)
## View that inserts a new ResHallPhoto object into the database according
## to the formdata from the photoForm within dormRooms.html.
## url: '<uuid:resHallId>/addResHallPhoto'
def addResHallPhoto(request, resHallId):
    global message
    if request.method == 'POST':
        
        photo = request.FILES.get('myPhoto', False)
        success = queries.addResHallPhoto(resHallId, photo)
        message = '' if success else 'Invalid photo'
        return redirect('dormapp:dormRoomsPage', resHallId)

## addDormRoomPhoto(HttpRequest request, uuid dormRoomId)
## View that inserts a new DormRoomPhoto object into the database according
## to the formdata from the photoForm within dormReviews.html.
## url: '<uuid:dormRoomId>/addDormRoomPhoto'
def addDormRoomPhoto(request, dormRoomId):
    global message
    if request.method == 'POST':
        photo = request.FILES.get('myPhoto', False)
        success = queries.addDormRoomPhoto(dormRoomId, photo)
        message = '' if success else 'Invalid photo'
        return redirect('dormapp:dormReviewsPage', dormId=dormRoomId)