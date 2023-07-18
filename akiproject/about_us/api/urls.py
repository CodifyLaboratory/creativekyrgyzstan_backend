from rest_framework import routers, urlpatterns
from .views import AboutUsViewSet, ReportsViewSet, SupervisoryViewSet, FoundersViewSet, AdvantagesViewSet, PurposeViewSet, DocumentsViewSet, DocumentsPolViewSet, AboutPicturesViewSet

router = routers.SimpleRouter()
router.register('about', AboutUsViewSet, 'about')
router.register('advantages', AdvantagesViewSet, 'advantages')
router.register('purpose',  PurposeViewSet, 'purpose')
router.register('supervisory', SupervisoryViewSet, 'supervisory')
router.register('founders', FoundersViewSet, 'founders')
router.register('reports', ReportsViewSet, 'reports')
router.register('documents', DocumentsViewSet, 'documents')
router.register('documentspol', DocumentsPolViewSet, 'documentspol')
router.register('aboutpictures', AboutPicturesViewSet, 'aboutpictures')

urlpatterns = router.urls