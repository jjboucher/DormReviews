from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:universityId>/resHalls', views.resHallsPage, name='resHallsPage'),
    path('<uuid:resHallId>/dormRooms', views.dormRoomsPage, name='dormRoomsPage'),
    path('<uuid:resHallId>/addReview',views.addReview,name='addReview'),
    path('<uuid:resHallId>/addPhoto',views.addPhoto,name='addPhoto'),
    path('<uuid:dormId>/reviews', views.dormReviewsPage, name="dormReviewsPage"),
    path('<uuid:dormId>/addDormReview', views.addDormReviewPage, name='addDormReview')
]
