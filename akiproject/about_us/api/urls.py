from rest_framework import routers, urlpatterns
from .views import AboutUsViewSet, ReportsViewSet, SupervisoryViewSet, FoundersViewSet, AdvantagesViewSet, PurposeViewSet, DocumentsViewSet, DocumentsPolViewSet, AboutPicturesViewSet

router = routers.SimpleRouter()
router.register('api/about', AboutUsViewSet, 'about')
router.register('api/advantages', AdvantagesViewSet, 'advantages')
router.register('api/purpose',  PurposeViewSet, 'purpose')
router.register('api/supervisory', SupervisoryViewSet, 'supervisory')
router.register('api/founders', FoundersViewSet, 'founders')
router.register('api/reports', ReportsViewSet, 'reports')
router.register('api/documents', DocumentsViewSet, 'documents')
router.register('api/documentspol', DocumentsPolViewSet, 'documentspol')
router.register('api/aboutpictures', AboutPicturesViewSet, 'aboutpictures')

urlpatterns = router.urls