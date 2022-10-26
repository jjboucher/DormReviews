from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resHalls', views.resHallsPage, name='resHallsPage'),
    path('<resHallId>/dormRooms', views.dormRoomsPage, name='dormRoomsPage'),
    path('<resHallId>/addReview',views.addReview,name='addReview'),
    path('<resHallId>/addPhoto',views.addPhoto,name='addPhoto'),
    path('dormroom/<dormId>', views.dormReviewsPage, name="dormReviewsPage")
]
