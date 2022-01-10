from rest_framework import routers, urlpatterns
from .views import EventViewSet

router = routers.DefaultRouter()
router.register('api/event', EventViewSet, 'event')

urlpatterns = router.urls