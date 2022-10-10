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
    resHalls = m.ResHall.filter(university = universityId)
    returnList = []
    for resHall in resHalls:
        reviews = m.ResHallReview.filter(resHall = resHall.id)
        ratings = []
        for review in reviews:
            ratings.append(review.starRating)
        
        averageRating = sum(ratings) / len(ratings)

        thumbnail = m.ResHallPhoto.filter(resHall = resHall.id).latest('dateCreated').photo

        returnList.append(resHallView(resHall.name, thumbnail, averageRating))
    
    return returnList

class dormRoomView():
    def __init__(self, name, thumbnail, rating):
        self.name = name
        self.thumbnail = thumbnail
        self.rating = rating

def getDormRooms(resHallId):
    dormRooms = m.DormRoom.filter(resHall = resHallId)
    returnList = []
    for dormRoom in dormRooms:
        ratings = m.DormRoomReview.filter(dormRoom = dormRoom.id).values('starRating')
    
        averageRating = sum(ratings) / len(ratings)

        thumbnail = m.DormRoomPhoto.filter(dormRoom = dormRoom.Id).latest('dateCreated').photo

        returnList.append(dormRoomView(dormRoom.name, thumbnail, averageRating))
    
    return returnList
