import dormapp.models as m
import uuid

# for form validation:
shortMaxLength = 255
longMaxLength = 1500

#region homePage

## universityView
## TODO
class universityView():
    def __init__(self, id, name, reviewCount, logo):
        self.id = id
        self.name = name
        self.reviewCount = reviewCount
        self.logo

## getUniversities()
## Retrieves list of all University objects from database
def getUniversities():
    universities = m.University.objects.all()
    universityList = []
    for university in universities:
        dormReviewCount = m.DormRoomReview.objects.filter(dormRoom__resHall__university = university).count()
        resHallReviewCount = m.ResHallReview.objects.filter(resHall__university = university).count()

        reviewCount = dormReviewCount + resHallReviewCount

        logo = m.UniversityPhoto.objects.filter(university = university).first()
        
        universityList.append(universityView(id=university.id, name=university.name, reviewCount=reviewCount, logo=logo))
        
    return universityList

## addUniversity(string name)
## Inserts a new University object into database
def addUniversity(name) -> m.University:
    if name:
        university = m.University(id = uuid.uuid4(), name = name)
        university.save()
        return university
    return None

## addUniversityPhoto(photo, uuid universityId)
## Inserts a new UniversityPhoto object into database
# def addUniversityPhoto(photo, universityId):
#     universityPhoto = m.UniversityPhoto(university = m.University.objects.get(id = universityId), photo = photo)
#     universityPhoto.save()

def addUniversityPhoto(university, uploadedPhoto) -> bool:
    if university and uploadedPhoto:
        photo = m.UniversityPhoto(university = university, photo = uploadedPhoto)
        photo.save()
        return True
    return False

#endregion

#region resHallsPage

## resHallView
## TODO
class resHallView():
    def __init__(self, id, name, thumbnail, rating):
        self.id = id
        self.name = name
        self.thumbnail = thumbnail
        self.rating = rating

## getResHalls(uuid universityId)
## TODO
def getResHalls(universityId):
    resHalls = m.ResHall.objects.filter(university = universityId)
    returnList = []
    for resHall in resHalls:
        ratings = m.ResHallReview.objects.filter(resHall = resHall.id).values_list('starRating', flat=True)
        
        averageRating = 0
        if len(ratings) > 0:
            averageRating = round(sum(ratings) / len(ratings), 1)

        thumbnail = None
        photos = m.ResHallPhoto.objects.filter(resHall = resHall)
        if len(photos) > 0:
            thumbnail = photos.latest('dateCreated').photo

        returnList.append(resHallView(resHall.id, resHall.name, thumbnail, averageRating))
    
    return returnList

## getUniversityName(uuid universityId)
## TODO
def getUniversityName(universityId):
    university = m.University.objects.get(id=universityId)
    return university.name

## addResHall(uuid universityId, string name)
## TODO
def addResHall(universityId, name):
    if name and len(name) <= shortMaxLength:
        university = m.University.objects.get(id=universityId)
        resHall = m.ResHall(id = uuid.uuid4(), university = university, name = name)
        resHall.save()
        return True
    return False

#endregion

#region dormRoomsPage

## getResHallName(uuid resHallId)
## TODO
def getResHallName(resHallId):
    resHall = m.ResHall.objects.get(id=resHallId)
    return resHall.name

## addResHallReview(uuid hallId, int rating, string title, string body)
## TODO
def addResHallReview(hallId, rating, title, body):
    rating = (int)(rating) if rating else 0
    if (len(title) <= shortMaxLength and
        rating >= 1 and 
        rating <= 5 and
        len(body) <= longMaxLength):

            hall = m.ResHall.objects.get(id=hallId)
            review = m.ResHallReview(id = uuid.uuid4(), resHall = hall, starRating = rating, reviewTitle = title, reviewBody = body)
            review.save()
            return True
    return False

## addResHallPhoto(uuid hallId, file uploadedPhoto)
## TODO
def addResHallPhoto(hallId, uploadedPhoto):
    if uploadedPhoto:
        hall = m.ResHall.objects.get(id=hallId)
        photo = m.ResHallPhoto(resHall = hall, photo = uploadedPhoto)
        photo.save()
        return True
    return False

## addDormRoom(uuid hallId, int roomNumber)
## TODO
def addDormRoom(hallId, roomNumber):
    if roomNumber and len(roomNumber) <= shortMaxLength:
        resHall = m.ResHall.objects.get(id=hallId)
        dormRoom = m.DormRoom(id = uuid.uuid4(), resHall = resHall, roomNumber = roomNumber)
        dormRoom.save()
        return True
    return False

## dormRoomView
## TODO
class dormRoomView():
    def __init__(self, id, roomNumber, thumbnail, rating):
        self.id = id
        self.roomNumber = roomNumber
        self.thumbnail = thumbnail
        self.rating = rating

## getDormRooms(uuid resHallId)
## TODO
def getDormRooms(resHallId):
    dormRooms = m.DormRoom.objects.filter(resHall = resHallId)
    returnList = []
    for dormRoom in dormRooms:
        ratings = m.DormRoomReview.objects.filter(dormRoom = dormRoom.id).values_list('starRating', flat=True)
    
        averageRating = 0
        if len(ratings) > 0:
            averageRating = round(sum(ratings) / len(ratings), 1)

        thumbnail = None
        photos = m.DormRoomPhoto.objects.filter(dormRoom = dormRoom.id)
        if len(photos) > 0:
            thumbnail = photos.latest('dateCreated').photo

        returnList.append(dormRoomView(dormRoom.id, dormRoom.roomNumber, thumbnail, averageRating))
    
    return returnList

## getResHallReviews(uuid resHallId)
## TODO
def getResHallReviews(resHallId):
    return m.ResHallReview.objects.filter(resHall = resHallId).order_by('-dateCreated')

## getResHallPhotos(resHallId)
## TODO
def getResHallPhotos(resHallId):
    return m.ResHallPhoto.objects.filter(resHall = resHallId).order_by('-dateCreated')

#endregion

#region dormRoomReviews

## addDormRoomReview(uuid dormId, int rating, string title, string body)
## TODO
def addDormRoomReview(dormId, rating, title, body):
    rating = (int)(rating) if rating else 0
    if (len(title) <= shortMaxLength and
        rating >= 1 and rating <= 5 and
        len(body) <= longMaxLength):
            dorm = m.DormRoom.objects.get(id=dormId)
            review = m.DormRoomReview(id = uuid.uuid4(), dormRoom = dorm, starRating = rating, reviewTitle = title, reviewBody = body)
            review.save()
            return True
    return False

## getDormReviews(uuid dormRoomId)
## TODO
def getDormReviews(dormRoomId):
    return m.DormRoomReview.objects.filter(dormRoom = dormRoomId).order_by('-dateCreated')

## getDormName(uuid dormRoomId)
## TODO
def getDormName(dormRoomId):
    dormRoom = m.DormRoom.objects.get(id = dormRoomId)
    return dormRoom.roomNumber

## getDormPhotos(uuid dormRoomId)
## TODO
def getDormPhotos(dormRoomId):
    return m.DormRoomPhoto.objects.filter(dormRoom = dormRoomId).order_by('-dateCreated')

## addDormRoomPhoto(uuid dormId, file uploadedPhoto)
## TODO
def addDormRoomPhoto(dormId, uploadedPhoto):
    if uploadedPhoto:
        dormRoom = m.DormRoom.objects.get(id=dormId)
        photo = m.DormRoomPhoto(dormRoom = dormRoom, photo = uploadedPhoto)
        photo.save()
        return True
    return False

#endregion
