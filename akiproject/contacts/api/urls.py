from rest_framework import routers, urlpatterns
from .views import ContactViewSet

router = routers.DefaultRouter()
router.register('contact', ContactViewSet, 'contact')

urlpatterns = router.urls
