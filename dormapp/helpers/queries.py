import dormapp.models as m
import uuid

#region homePage

## universityView
## TODO

class universityView():
    def __init__(self, id, name, reviewCount):
        self.id = id
        self.name = name
        self.reviewCount = reviewCount

## getUniversities()
## Retrieves list of all University objects from database
## returntype: [University]

def getUniversities():
    universities = m.University.objects.all()
    universityList = []
    for university in universities:
        dormReviewCount = m.DormRoomReview.objects.filter(dormRoom__resHall__university = university).count()
        resHallReviewCount = m.ResHallReview.objects.filter(resHall__university = university).count()

        reviewCount = dormReviewCount + resHallReviewCount
        
        universityList.append(universityView(id=university.id, name=university.name, reviewCount=reviewCount))
        
    return universityList

## addUniversity(string name)
## Inserts a new University object into database
## returntype: void

def addUniversity(name):
    university = m.University(id = uuid.uuid4(), name = name)
    university.save()
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
## Retrieves a list of ResHall objects according to the given
## uuid universityId.
## returntype: [ResHall]

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
            thumbnail = photos.earliest('dateCreated').photo

        returnList.append(resHallView(resHall.id, resHall.name, thumbnail, averageRating))
    
    return returnList

## getUniversityName(uuid universityId)
## Retrieves the name of a University object in the database
## according to its uuid universityId.
## returntype: string

def getUniversityName(universityId):
    university = m.University.objects.get(id=universityId)
    return university.name

## addResHall(uuid universityId, string name)
## Inserts a ResHall object into the database according to passed in
## data.
## returntype: void

def addResHall(universityId, name):
    university = m.University.objects.get(id=universityId)
    resHall = m.ResHall(id = uuid.uuid4(), university = university, name = name)
    resHall.save()

#endregion

#region dormRoomsPage

## getResHallName(uuid resHallId)
## TODO

def getResHallName(resHallId):
    resHall = m.ResHall.objects.get(id=resHallId)
    return resHall.name

## addResHallReview(uuid hallId, int rating, string title, string body)
## Inserts a new ResHallReview object into the database according to the
## given data.
## returntype: void

def addResHallReview(hallId, rating, title, body):
    hall = m.ResHall.objects.get(id=hallId)
    review = m.ResHallReview(id = uuid.uuid4(), resHall = hall, starRating = rating, reviewTitle = title, reviewBody = body)
    review.save()

## addResHallPhoto(uuid hallId, file uploadedPhoto)
## Inserts a new ResHallPhoto object into the database according to the
## given data.
## returntype: void

def addResHallPhoto(hallId, uploadedPhoto):
    hall = m.ResHall.objects.get(id=hallId)
    photo = m.ResHallPhoto(resHall = hall, photo = uploadedPhoto)
    photo.save()

## addDormRoom(uuid hallId, int roomNumber)
## Inserts a new DormRoom object into the database according to the
## given data.
## returntype: void

def addDormRoom(hallId, roomNumber):
    resHall = m.ResHall.objects.get(id=hallId)
    dormRoom = m.DormRoom(id = uuid.uuid4(), resHall = resHall, roomNumber = roomNumber)
    dormRoom.save()

## dormRoomView
## TODO

class dormRoomView():
    def __init__(self, id, roomNumber, thumbnail, rating):
        self.id = id
        self.roomNumber = roomNumber
        self.thumbnail = thumbnail
        self.rating = rating

## getDormRooms(uuid resHallId)
## Retrieves a list of all DormRoom objects in the database which are
## associated with the given resHallId.
## returntype: [DormRoom]

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
            thumbnail = photos.earliest('dateCreated').photo

        returnList.append(dormRoomView(dormRoom.id, dormRoom.roomNumber, thumbnail, averageRating))
    
    return returnList

## getResHallReviews(uuid resHallId)
## Retrieves a list of all ResHallReview objects in the database which are
## associated with the given resHallId.
## returntype: [ResHallReview]

def getResHallReviews(resHallId):
    return m.ResHallReview.objects.filter(resHall = resHallId).order_by('-dateCreated')

## getResHallPhotos(resHallId)
## Retrieves a list of all ResHallPhoto objects in the database which are
## associated with the given resHallId.
## returntype: [ResHallPhoto]

def getResHallPhotos(resHallId):
    return m.ResHallPhoto.objects.filter(resHall = resHallId).order_by('dateCreated')

#endregion

#region dormRoomReviews

## addDormRoomReview(uuid dormId, int rating, string title, string body)
## Inserts a new DormRoomReview object into the database according to the
## given data.
## returntype: void

def addDormRoomReview(dormId, rating, title, body):
    dorm = m.DormRoom.objects.get(id=dormId)
    review = m.DormRoomReview(id = uuid.uuid4(), dormRoom = dorm, starRating = rating, reviewTitle = title, reviewBody = body)
    review.save()

## getDormReviews(uuid dormRoomId)
## Retrieves a list of all DormRoomReview objects in the database which are
## associated with the given dormRoomId.
## returntype: [DormRoomReview]

def getDormReviews(dormRoomId):
    return m.DormRoomReview.objects.filter(dormRoom = dormRoomId).order_by('-dateCreated')

## getDormName(uuid dormRoomId)
## Retrieves the name attribute of a given DormRoom object, through
## its uuid dormRoomId.
## returntype: string

def getDormName(dormRoomId):
    dormRoom = m.DormRoom.objects.get(id = dormRoomId)
    return dormRoom.roomNumber

## getDormPhotos(uuid dormRoomId)
## Retrieves a list of all DormRoomPhoto objects in the database which are
## associated with the given dormRoomId.
## returntype: [DormRoomPhoto]

def getDormPhotos(dormRoomId):
    return m.DormRoomPhoto.objects.filter(dormRoom = dormRoomId).order_by('dateCreated')

## addDormRoomPhoto(uuid dormId, file uploadedPhoto)
## Inserts a new DormRoomPhoto object into the database according to the
## given data.
## returntype: void

def addDormRoomPhoto(dormId, uploadedPhoto):
    dormRoom = m.DormRoom.objects.get(id=dormId)
    photo = m.DormRoomPhoto(dormRoom = dormRoom, photo = uploadedPhoto)
    photo.save()

#endregion
