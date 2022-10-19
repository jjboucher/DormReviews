import dormapp.models as m
import uuid

#region homePage
def getUniversities():
    universities = m.University.objects.all()
    return universities

#endregion

#region resHallsPage
class resHallView():
    def __init__(self, id, name, thumbnail, rating):
        self.id = id
        self.name = name
        self.thumbnail = thumbnail
        self.rating = rating

def getResHalls(universityId):
    resHalls = m.ResHall.objects.filter(university = universityId)
    returnList = []
    for resHall in resHalls:
        ratings = m.ResHallReview.objects.filter(resHall = resHall.id).values_list('starRating', flat=True)
        
        averageRating = 0
        if len(ratings) > 0:
            averageRating = sum(ratings) / len(ratings)

        thumbnail = None
        photos = m.ResHallPhoto.objects.filter(resHall = resHall)
        if len(photos) > 0:
            thumbnail = photos.latest('dateCreated').photo
        print(thumbnail)

        returnList.append(resHallView(resHall.id, resHall.name, thumbnail, averageRating))
    
    return returnList

def getUniversityName(universityId):
    university = m.University.objects.get(id=universityId)
    return university.name
#endregion

#region dormRoomsPage

def getResHallName(resHallId):
    resHall = m.ResHall.objects.get(id=resHallId)
    return resHall.name

def addResHallReview(hallId, rating, title, body):
    hall = m.ResHall.objects.get(id=hallId)
    review = m.ResHallReview(id = uuid.uuid4(), resHall = hall, starRating = rating, reviewTitle = title, reviewBody = body)
    review.save()

class dormRoomView():
    def __init__(self, id, name, thumbnail, rating):
        self.id = id
        self.name = name
        self.thumbnail = thumbnail
        self.rating = rating

def getDormRooms(resHallId):
    dormRooms = m.DormRoom.objects.filter(resHall = resHallId)
    returnList = []
    for dormRoom in dormRooms:
        ratings = m.DormRoomReview.objects.filter(dormRoom = dormRoom.id).values_list('starRating', flat=True)
    
        averageRating = 0
        if len(ratings) > 0:
            averageRating = sum(ratings) / len(ratings)

        thumbnail = None
        photos = m.DormRoomPhoto.objects.filter(dormRoom = dormRoom.Id)
        if len(photos) > 0:
            thumbnail = photos.latest('dateCreated').photo

        returnList.append(dormRoomView(dormRoom.name, thumbnail, averageRating))
    
    return returnList

def getResHallReviews(resHallId):
    return m.ResHallReview.objects.filter(resHall = resHallId).order_by('-dateCreated')

#endregion

#region dormRoom
def addDormRoomReview(room, rating, title, body):
    review = m.DormRoomReview(dormRoom = room, starRating = rating, reviewTitle = title, reviewBody = body)
    review.save()

#endregion