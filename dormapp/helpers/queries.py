import dormapp.models as m

def getUniversities():
    universities = m.University.objects.all()
    return universities

class resHallView():
    def __init__(self, name, thumbnail, rating):
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

        returnList.append(resHallView(resHall.name, thumbnail, averageRating))
    
    return returnList

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