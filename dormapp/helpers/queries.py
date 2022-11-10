import dormapp.models as m
import uuid

#region homePage
class universityView():
    def __init__(self, id, name, reviewCount):
        self.id = id
        self.name = name
        self.reviewCount = reviewCount

def getUniversities():
    universities = m.University.objects.all()
    universityList = []
    for university in universities:
        dormReviewCount = m.DormRoomReview.objects.filter(dormRoom__resHall__university = university).count()
        resHallReviewCount = m.ResHallReview.objects.filter(resHall__university = university).count()

        reviewCount = dormReviewCount + resHallReviewCount
        
        universityList.append(universityView(id=university.id, name=university.name, reviewCount=reviewCount))
        
    return universityList

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
            thumbnail = photos.earliest('dateCreated').photo

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

def addResHallPhoto(hallId, uploadedPhoto):
    hall = m.ResHall.objects.get(id=hallId)
    photo = m.ResHallPhoto(resHall = hall, photo = uploadedPhoto)
    photo.save()

class dormRoomView():
    def __init__(self, id, roomNumber, thumbnail, rating):
        self.id = id
        self.roomNumber = roomNumber
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
        photos = m.DormRoomPhoto.objects.filter(dormRoom = dormRoom.id)
        if len(photos) > 0:
            thumbnail = photos.earliest('dateCreated').photo

        returnList.append(dormRoomView(dormRoom.id, dormRoom.roomNumber, thumbnail, averageRating))
    
    return returnList

def getResHallReviews(resHallId):
    return m.ResHallReview.objects.filter(resHall = resHallId).order_by('-dateCreated')

def getResHallPhotos(resHallId):
    return m.ResHallPhoto.objects.filter(resHall = resHallId).order_by('dateCreated')

#endregion

#region dormRoomReviews
def addDormRoomReview(dormId, rating, title, body):
    dorm = m.DormRoom.objects.get(id=dormId)
    review = m.DormRoomReview(id = uuid.uuid4(), dormRoom = dorm, starRating = rating, reviewTitle = title, reviewBody = body)
    review.save()

def getDormReviews(dormRoomId):
    return m.DormRoomReview.objects.filter(dormRoom = dormRoomId).order_by('-dateCreated')

def getDormName(dormRoomId):
    dormRoom = m.DormRoom.objects.get(id = dormRoomId)
    return dormRoom.roomNumber

def getDormPhotos(dormRoomId):
    return m.DormRoomPhoto.objects.filter(dormRoom = dormRoomId).order_by('dateCreated')

def addDormRoomPhoto(dormId, uploadedPhoto):
    dormRoom = m.DormRoom.objects.get(id=dormId)
    photo = m.DormRoomPhoto(dormRoom = dormRoom, photo = uploadedPhoto)
    photo.save()

#endregion
