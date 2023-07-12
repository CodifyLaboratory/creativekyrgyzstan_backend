from rest_framework import routers, urlpatterns
from .views import EventViewSet, EventPastViewSet, EventFutureViewSet, EventImagesViewSet

router = routers.DefaultRouter()
router.register('api/event', EventViewSet, 'event')
router.register('api/eventpast', EventPastViewSet, 'eventpast')
router.register('api/eventfuture', EventFutureViewSet, 'eventfuture')
router.register('api/eventimages', EventImagesViewSet, 'eventimages')

urlpatterns = router.urls