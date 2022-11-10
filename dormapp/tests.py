import django.test
import dormapp.models as m
import datetime
from dormapp.helpers import queries as q

# globals
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
twoDaysAgo = today - datetime.timedelta(days=1)
universityA = None
universityB = None
universityC = None
resHallA1 = None
resHallA2 = None
resHallB1 = None
dormRoomA1x = None
dormRoomA1y = None
dormRoomB1x = None
resHallReviewA1x = None
resHallReviewA2x = None
resHallReviewA2y = None
dormRoomReviewA1x1 = None
dormRoomReviewB1x1 = None
dormRoomReviewB1x2 = None
resHallPhotoA1x = None
resHallPhotoA1y = None
resHallPhotoB1x = None
dormRoomPhotoA1y1 = None
dormRoomPhotoA1y2 = None
dormRoomPhotoB1x1 = None

# Unit tests for queries
class QueriesUnitTests(django.test.TestCase):

    # set up initial database values (will be reset for each test)
    def setUp(self):

        global universityA
        global universityB
        global universityC
        global resHallA1
        global resHallA2
        global resHallB1
        global dormRoomA1x
        global dormRoomA1y
        global dormRoomB1x
        global resHallReviewA1x
        global resHallReviewA2x
        global resHallReviewA2y
        global dormRoomReviewA1x1
        global dormRoomReviewB1x1
        global dormRoomReviewB1x2
        global resHallPhotoA1x
        global resHallPhotoA1y
        global resHallPhotoB1x
        global dormRoomPhotoA1y1
        global dormRoomPhotoA1y2
        global dormRoomPhotoB1x1
        
        # create universities:
        universityA = m.University.objects.create(name='University A')
        universityB = m.University.objects.create(name='University B')
        universityC = m.University.objects.create(name='University C')

        # create resHalls:
        resHallA1 = m.ResHall.objects.create(name='ResHall A1', university=universityA)
        resHallA2 = m.ResHall.objects.create(name='ResHall A2', university=universityA)
        resHallB1 = m.ResHall.objects.create(name='ResHall B1', university=universityB)

        # create dormRooms:
        dormRoomA1x = m.DormRoom.objects.create(roomNumber='DormRoom A1x', resHall=resHallA1)
        dormRoomA1y = m.DormRoom.objects.create(roomNumber='DormRoom A1y', resHall=resHallA1)
        dormRoomB1x = m.DormRoom.objects.create(roomNumber='DormRoom B1x', resHall=resHallB1)
        
        # create resHallReviews:
        resHallReviewA1x = m.ResHallReview.objects.create(reviewTitle='title A1x', starRating=1, reviewBody='body A1x', dateCreated=today, resHall=resHallA1)
        resHallReviewA2x = m.ResHallReview.objects.create(reviewTitle='title A2x', starRating=2, reviewBody='body A2x', dateCreated=yesterday, resHall=resHallA2)
        resHallReviewA2y = m.ResHallReview.objects.create(reviewTitle='title A2x', starRating=3, reviewBody='body A2x', dateCreated=twoDaysAgo, resHall=resHallA2)
    
        # create dormRoomReviews:
        dormRoomReviewA1x1 = m.DormRoomReview.objects.create(reviewTitle='title A1x1', starRating=4, reviewBody='body A1x1', dateCreated=today, dormRoom=dormRoomA1x)
        dormRoomReviewB1x1 = m.DormRoomReview.objects.create(reviewTitle='title B1x1', starRating=5, reviewBody='body B1x1', dateCreated=yesterday, dormRoom=dormRoomB1x)
        dormRoomReviewB1x2 = m.DormRoomReview.objects.create(reviewTitle='title B1x2', starRating=1, reviewBody='body B1x2', dateCreated=twoDaysAgo, dormRoom=dormRoomB1x)

        # create resHallPhotos:
        resHallPhotoA1x = m.ResHallPhoto.objects.create(photo='res-hall-photos/booth.jpg', dateCreated=today, resHall=resHallA1)
        resHallPhotoA1y = m.ResHallPhoto.objects.create(photo='res-hall-photos/shaw.jpg', dateCreated=yesterday, resHall=resHallA1)
        resHallPhotoB1x = m.ResHallPhoto.objects.create(photo='res-hall-photos/booth.jpg', dateCreated=twoDaysAgo, resHall=resHallB1)

        # create dormRoomPhotos:
        dormRoomPhotoA1y1 = m.DormRoomPhoto.objects.create(photo='dorm-room-photos/test.jpg', dateCreated=today, dormRoom=dormRoomA1y)
        dormRoomPhotoA1y2 = m.DormRoomPhoto.objects.create(photo='dorm-room-photos/test2.jpg', dateCreated=yesterday, dormRoom=dormRoomA1y)
        dormRoomPhotoB1x1 = m.DormRoomPhoto.objects.create(photo='dorm-room-photos/test.jpg', dateCreated=twoDaysAgo, dormRoom=dormRoomB1x)

    def test_getUniversities(self):
        
        queryResult = q.getUniversities()
        
        # test list count
        self.assertEqual(3, len(queryResult))
        
        # test list
        testList = ['University A', 'University B', 'University C']
        for i in range(3):
            self.assertEqual(testList[i], queryResult[i].name)
    
    def test_getResHalls(self):
        global universityA
        global universityB
        global universityC

        queryResult = q.getResHalls(universityA.id)

        # test list counts
        self.assertEqual(2, len(queryResult))
        self.assertEqual(1, len(q.getResHalls(universityB.id)))
        self.assertEqual(0, len(q.getResHalls(universityC.id)))

        # test list
        testList = ['ResHall A1', 'ResHall A2']
        for i in range(2):
            self.assertEqual(testList[i], queryResult[i].name)

    def test_getUniversityName(self):
        global universityA
        global universityB

        # test return value
        self.assertEqual('University A', q.getUniversityName(universityA.id))
        self.assertEqual('University C', q.getUniversityName(universityC.id))
    
    def test_getResHallName(self):
        global resHallA1
        global resHallA2

        # test return value
        self.assertEqual('ResHall A1', q.getResHallName(resHallA1.id))
        self.assertEqual('ResHall A2', q.getResHallName(resHallA2.id))

    def test_addResHallReview(self):
        global resHallA1
        global resHallB1

        q.addResHallReview(hallId=resHallA1.id, rating=1, title='test', body='body')
        q.addResHallReview(hallId=resHallB1.id, rating=1, title='test title', body='test body')

        testList1 = ['title A1x', 'test']
        testList2 = ['test title']

        testQuery1 = list(m.ResHallReview.objects.filter(resHall=resHallA1).order_by('dateCreated').values_list('reviewTitle', flat=True))
        testQuery2 = list(m.ResHallReview.objects.filter(resHall=resHallB1).order_by('dateCreated').values_list('reviewTitle', flat=True))

        # test whether resHallReview was added to DB table with existing data
        self.assertEqual(testList1, testQuery1)

        # test whether resHallReview was added to empty DB table
        self.assertEqual(testList2, testQuery2)

    def test_addResHallPhoto(self):
        global resHallA2

        q.addResHallPhoto(hallId=resHallA2.id, uploadedPhoto='res-hall-photos/shaw.jpg')

        testList = ['res-hall-photos/shaw.jpg']
        testQuery = list(m.ResHallPhoto.objects.filter(resHall=resHallA2).order_by('dateCreated').values_list('photo', flat=True))

        # test whether resHallPhoto was added to DB table
        self.assertEqual(testList, testQuery)

    def test_getDormRooms(self):
        global resHallA1
        global resHallA2
        global resHallB1

        queryResult = q.getDormRooms(resHallA1.id)

        # test list counts
        self.assertEqual(2, len(queryResult))
        self.assertEqual(0, len(q.getDormRooms(resHallA2.id)))
        self.assertEqual(1, len(q.getDormRooms(resHallB1.id)))

        # test list
        testList = ['DormRoom A1x', 'DormRoom A1y']
        for i in range(2):
            self.assertEqual(testList[i], queryResult[i].roomNumber)

    def test_getResHallReviews(self):
        global resHallA1
        global resHallA2
        global resHallB1

        queryResult = q.getResHallReviews(resHallA1.id)

        # test list counts
        self.assertEqual(1, len(queryResult))
        self.assertEqual(2, len(q.getResHallReviews(resHallA2.id)))
        self.assertEqual(0, len(q.getResHallReviews(resHallB1.id)))

        # test list
        self.assertEqual(queryResult[0].reviewTitle, 'title A1x')

    def test_getResHallPhotos(self):
        global resHallA1
        global resHallA2
        global resHallB1

        queryResult = q.getResHallPhotos(resHallA1.id)

        # test list counts
        self.assertEqual(2, len(queryResult))
        self.assertEqual(0, len(q.getResHallPhotos(resHallA2.id)))
        self.assertEqual(1, len(q.getResHallPhotos(resHallB1.id)))

        # test list
        testList = ['res-hall-photos/booth.jpg', 'res-hall-photos/shaw.jpg']
        for i in range(2):
            self.assertEqual(testList[i], queryResult[i].photo)

    def test_addDormRoomReview(self):
        global dormRoomA1y
        global dormRoomB1x

        q.addDormRoomReview(dormId=dormRoomB1x.id, rating=1, title='test', body='body')
        q.addDormRoomReview(dormId=dormRoomA1y.id, rating=1, title='test title', body='test body')

        testList1 = ['title B1x1', 'title B1x2', 'test']
        testList2 = ['test title']

        testQuery1 = list(m.DormRoomReview.objects.filter(dormRoom=dormRoomB1x).order_by('dateCreated').values_list('reviewTitle', flat=True))
        testQuery2 = list(m.DormRoomReview.objects.filter(dormRoom=dormRoomA1y).order_by('dateCreated').values_list('reviewTitle', flat=True))

        # test whether resHallReview was added to DB table with existing data
        self.assertEqual(testList1, testQuery1)

        # test whether resHallReview was added to empty DB table
        self.assertEqual(testList2, testQuery2)

    def test_getDormReviews(self):
        global dormRoomA1x
        global dormRoomA1y
        global dormRoomB1x

        queryResult = q.getDormReviews(dormRoomA1x.id)

        # test list counts
        self.assertEqual(1, len(queryResult))
        self.assertEqual(0, len(q.getDormReviews(dormRoomA1y.id)))
        self.assertEqual(2, len(q.getDormReviews(dormRoomB1x.id)))

        # test list
        self.assertEqual(queryResult[0].reviewTitle, 'title A1x1')
    
    def test_getDormName(self):
        global dormRoomA1x
        global dormRoomB1x

        # test return value
        self.assertEqual('DormRoom A1x', q.getDormName(dormRoomA1x.id))
        self.assertEqual('DormRoom B1x', q.getDormName(dormRoomB1x.id))
    
    def test_getDormPhotos(self):
        global dormRoomA1x
        global dormRoomA1y
        global dormRoomB1x

        queryResult = q.getDormPhotos(dormRoomA1y.id)

        # test list counts
        self.assertEqual(2, len(queryResult))
        self.assertEqual(0, len(q.getDormPhotos(dormRoomA1x.id)))
        self.assertEqual(1, len(q.getDormPhotos(dormRoomB1x.id)))

        # test list
        testList = ['dorm-room-photos/test.jpg', 'dorm-room-photos/test2.jpg']
        for i in range(2):
            self.assertEqual(testList[i], queryResult[i].photo)
    
    def test_addDormRoomPhoto(self):
        global dormRoomA1x

        q.addDormRoomPhoto(dormId=dormRoomA1x.id, uploadedPhoto='dorm-room-photos/test.jpg')

        testList = ['dorm-room-photos/test.jpg']
        testQuery = list(m.DormRoomPhoto.objects.filter(dormRoom=dormRoomA1x).order_by('dateCreated').values_list('photo', flat=True))

        # test whether resHallPhoto was added to DB table
        self.assertEqual(testList, testQuery)