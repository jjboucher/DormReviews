from django.urls import path
from django.conf.urls import include
from django.conf import settings

app_name = 'dormapp'
from . import views

# All of the unique urls and pages in the webapp, and their corresponding
# function within views.py

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('addUniversity', views.addUniversityPage, name='addUniversityPage'),
    path('<uuid:universityId>/resHalls', views.resHallsPage, name='resHallsPage'),
    path('<uuid:universityId>/addResHall', views.addResHallPage, name='addResHall'),
    path('<uuid:resHallId>/dormRooms', views.dormRoomsPage, name='dormRoomsPage'),
    path('<uuid:resHallId>/addReview', views.addReview, name='addReview'),
    path('<uuid:resHallId>/addResHallPhoto', views.addResHallPhoto, name='addResHallPhoto'),
    path('<uuid:resHallId>/addDormRoom', views.addDormRoomPage, name='addDormRoom'),
    path('<uuid:dormId>/reviews', views.dormReviewsPage, name="dormReviewsPage"),
    path('<uuid:dormId>/addDormReview', views.addDormReviewPage, name='addDormReview'),
    path('<uuid:dormRoomId>/addDormRoomPhoto', views.addDormRoomPhoto, name='addDormRoomPhoto')
]
