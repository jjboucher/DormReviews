from django.db import models
import uuid

# Models for our database.
shortMaxLength = 255
longMaxLength = 1500

class University(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=shortMaxLength)

class ResHall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=shortMaxLength)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class DormRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    roomNumber = models.CharField(max_length=shortMaxLength)
    resHall = models.ForeignKey(ResHall, on_delete=models.CASCADE)

class ResHallReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resHall = models.ForeignKey(ResHall, on_delete=models.CASCADE)
    starRating = models.IntegerField(default=0)
    reviewTitle = models.CharField(max_length=shortMaxLength)
    reviewBody = models.TextField(max_length=longMaxLength)
    dateCreated = models.DateTimeField(auto_now=True)

class DormRoomReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dormRoom = models.ForeignKey(DormRoom, on_delete=models.CASCADE)
    starRating = models.IntegerField(default=0)
    reviewTitle = models.CharField(max_length=shortMaxLength)
    reviewBody = models.TextField(max_length=longMaxLength)
    dateCreated = models.DateTimeField(auto_now=True)

class UniversityPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='university-photos')
    dateCreated = models.DateTimeField(auto_now=True)

class ResHallPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resHall = models.ForeignKey(ResHall, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='res-hall-photos')
    dateCreated = models.DateTimeField(auto_now=True)

class DormRoomPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dormRoom = models.ForeignKey(DormRoom, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='dorm-room-photos')
    dateCreated = models.DateTimeField(auto_now=True)
