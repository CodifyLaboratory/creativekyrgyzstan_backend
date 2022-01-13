from rest_framework import routers, urlpatterns
from .views import AboutUsViewSet, ReportsViewSet, SupervisoryViewSet

router = routers.SimpleRouter()
router.register('api/about', AboutUsViewSet, 'about_us')
router.register('api/supervisory', SupervisoryViewSet, 'members')
router.register('api/reports', ReportsViewSet, 'reports')

urlpatterns = router.urls