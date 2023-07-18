from rest_framework import routers, urlpatterns
from .views import MainPageViewSet, FooterViewSet

router = routers.DefaultRouter()
router.register('main', MainPageViewSet, 'main')
router.register('footer', FooterViewSet, 'footer')

urlpatterns = router.urls
