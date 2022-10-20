from django.db import models
import uuid

# Create your models here.

class University(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class ResHall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class DormRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    roomNumber = models.CharField(max_length=255)
    resHall = models.ForeignKey(ResHall, on_delete=models.CASCADE)

class ResHallReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resHall = models.ForeignKey(ResHall, on_delete=models.CASCADE)
    starRating = models.IntegerField(default=0)
    reviewTitle = models.CharField(max_length=255)
    reviewBody = models.TextField(max_length=1500)
    dateCreated = models.DateTimeField(auto_now=True)

class DormRoomReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dormRoom = models.ForeignKey(DormRoom, on_delete=models.CASCADE)
    starRating = models.IntegerField(default=0)
    reviewTitle = models.CharField(max_length=255)
    reviewBody = models.TextField(max_length=1500)
    dateCreated = models.DateTimeField(auto_now=True)

class ResHallPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resHall = models.ForeignKey(ResHall, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='res-hall-photos')
    dateCreated = models.DateTimeField(auto_now=True)

class DormRoomPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dormRoom = models.ForeignKey(ResHall, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='dorm-room-photos')
    dateCreated = models.DateTimeField(auto_now=True)
