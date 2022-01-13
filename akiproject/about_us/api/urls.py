from rest_framework import routers, urlpatterns
from .views import AboutUsViewSet, ReportsViewSet, SupervisoryViewSet

router = routers.SimpleRouter()
router.register('api/about', AboutUsViewSet, 'about')
router.register('api/supervisory', SupervisoryViewSet, 'supervisory')
router.register('api/reports', ReportsViewSet, 'reports')

urlpatterns = router.urls