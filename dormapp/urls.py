from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resHalls', views.resHallsPage, name='resHallsPage'),
    path('<resHallId>/dormRooms', views.dormRoomsPage, name='dormRoomsPage')
]