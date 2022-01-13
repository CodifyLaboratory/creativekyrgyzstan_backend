from rest_framework import routers, urlpatterns
from .views import EventViewSet

router = routers.DefaultRouter()
router.register('api/about', EventViewSet, 'about_us')

urlpatterns = router.urls