from rest_framework import routers, urlpatterns
from .views import EventViewSet, EventPastViewSet, EventFutureViewSet, EventImagesViewSet

router = routers.DefaultRouter()
router.register('event', EventViewSet, 'event')
router.register('eventpast', EventPastViewSet, 'eventpast')
router.register('eventfuture', EventFutureViewSet, 'eventfuture')
router.register('eventimages', EventImagesViewSet, 'eventimages')

urlpatterns = router.urls
