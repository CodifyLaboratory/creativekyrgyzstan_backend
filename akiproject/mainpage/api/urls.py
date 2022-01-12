from rest_framework import routers, urlpatterns
from .views import MainPageViewSet

router = routers.DefaultRouter()
router.register('api/main', MainPageViewSet, 'main')

urlpatterns = router.urls