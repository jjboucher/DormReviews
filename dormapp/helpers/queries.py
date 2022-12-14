import dormapp.models as m
import uuid

# for form validation:
shortMaxLength = 255
longMaxLength = 1500

#region homePage

## universityView
## Data transfer object for homepage universities list
class universityView():
    def __init__(self, id, name, reviewCount, logo):
        self.id = id
        self.name = name
        self.reviewCount = reviewCount
        self.logo = logo

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
## If name has value, return the new university object, else return None
def addUniversity(name) -> m.University:
    if name:
        university = m.University(id = uuid.uuid4(), name = name)
        university.save()
        return university
    return None

## addUniversityPhoto(photo, uuid universityId)
## Inserts a new UniversityPhoto object into database
## Returns true if Successful, False otherwise
def addUniversityPhoto(university, uploadedPhoto) -> bool:
    if university and uploadedPhoto:
        photo = m.UniversityPhoto(university = university, photo = uploadedPhoto)
        photo.save()
        return True
    return False

#endregion

#region resHallsPage

## resHallView
## Data transfer object for residence halls page
class resHallView():
    def __init__(self, id, name, thumbnail, rating):
        self.id = id
        self.name = name
        self.thumbnail = thumbnail
        self.rating = rating

## getResHalls(uuid universityId)
## Retreives all residence halls associated with a given university ID
## returns a list of resHallView() objects
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
## Returns university name given its ID
def getUniversityName(universityId):
    university = m.University.objects.get(id=universityId)
    return university.name

## addResHall(uuid universityId, string name)
## Adds a new residence hall to the database given its university and name
## Returns True if successful, False otherwise
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
## Returns ResHall name given its ID
def getResHallName(resHallId):
    resHall = m.ResHall.objects.get(id=resHallId)
    return resHall.name

## addResHallReview(uuid hallId, int rating, string title, string body)
## Adds ResHallReview to database
## Returns True if successful, False otherwise
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
## Adds ResHallPhoto to database
## Returns True if successful, False otherwise
def addResHallPhoto(hallId, uploadedPhoto):
    if uploadedPhoto:
        hall = m.ResHall.objects.get(id=hallId)
        photo = m.ResHallPhoto(resHall = hall, photo = uploadedPhoto)
        photo.save()
        return True
    return False

## addDormRoom(uuid hallId, int roomNumber)
## Adds DormRoom to database
## Returns True if successful, False otherwise
def addDormRoom(hallId, roomNumber):
    if roomNumber and len(roomNumber) <= shortMaxLength:
        resHall = m.ResHall.objects.get(id=hallId)
        dormRoom = m.DormRoom(id = uuid.uuid4(), resHall = resHall, roomNumber = roomNumber)
        dormRoom.save()
        return True
    return False

## dormRoomView
## Data transfer object for dorm rooms list in dormRooms template
class dormRoomView():
    def __init__(self, id, roomNumber, thumbnail, rating):
        self.id = id
        self.roomNumber = roomNumber
        self.thumbnail = thumbnail
        self.rating = rating

## getDormRooms(uuid resHallId)
## Returns a list of dormRoomView objects for dorm rooms associated with given resHall id
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
## Returns ResHallReview queryset given resHall id
def getResHallReviews(resHallId):
    return m.ResHallReview.objects.filter(resHall = resHallId).order_by('-dateCreated')

## getResHallPhotos(resHallId)
## Returns ResHallPhoto queryset given resHall id
def getResHallPhotos(resHallId):
    return m.ResHallPhoto.objects.filter(resHall = resHallId).order_by('-dateCreated')

#endregion

#region dormRoomReviews

## addDormRoomReview(uuid dormId, int rating, string title, string body)
## Adds DormRoomReview to database
## Returns True if successful, False otherwise
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
## Returns DormRoomReview queryset given dormRoom ID
def getDormReviews(dormRoomId):
    return m.DormRoomReview.objects.filter(dormRoom = dormRoomId).order_by('-dateCreated')

## getDormName(uuid dormRoomId)
## Returns dorm room name given its ID
def getDormName(dormRoomId):
    dormRoom = m.DormRoom.objects.get(id = dormRoomId)
    return dormRoom.roomNumber

## getDormPhotos(uuid dormRoomId)
## Returns DormRoomPhoto queryset given dorm room ID
def getDormPhotos(dormRoomId):
    return m.DormRoomPhoto.objects.filter(dormRoom = dormRoomId).order_by('-dateCreated')

## addDormRoomPhoto(uuid dormId, file uploadedPhoto)
## Adds DormRoomPhoto to database
## Returns True if successful, False otherwise
def addDormRoomPhoto(dormId, uploadedPhoto):
    if uploadedPhoto:
        dormRoom = m.DormRoom.objects.get(id=dormId)
        photo = m.DormRoomPhoto(dormRoom = dormRoom, photo = uploadedPhoto)
        photo.save()
        return True
    return False

#endregion
