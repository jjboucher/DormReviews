import dormapp.models as m

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
        photos = m.ResHallPhoto.objects.filter(resHall = resHall.id)
        if len(photos) > 0:
            thumbnail = photos.latest('dateCreated').photo

        returnList.append(resHallView(resHall.id, resHall.name, thumbnail, averageRating))
    
    return returnList

def getUniversityName(universityId):
    university = m.University.objects.get(id=universityId)
    return university.name
#endregion

def addResHallReview(hall, rating, title, body):
    review = m.ResHallReview(resHall = hall, starRating = rating, reviewTitle = title, reviewBody = body)
    review.save()

class dormRoomView():
    def __init__(self, name, thumbnail, rating):
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

def addDormRoomReview(room, rating, title, body):
    review = m.DormHallReview(dormRoom = room, starRating = rating, reviewTitle = title, reviewBody = body)
    review.save()