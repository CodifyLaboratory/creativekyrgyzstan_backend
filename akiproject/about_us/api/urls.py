from rest_framework import routers, urlpatterns
from .views import AboutUsViewSet, ReportsViewSet, SupervisoryViewSet, FoundersViewSet

router = routers.SimpleRouter()
router.register('api/about', AboutUsViewSet, 'about')
router.register('api/supervisory', SupervisoryViewSet, 'supervisory')
router.register('api/founders', FoundersViewSet, 'founders')
router.register('api/reports', ReportsViewSet, 'reports')

urlpatterns = router.urls