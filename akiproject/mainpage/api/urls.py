from rest_framework import routers, urlpatterns
from .views import MainPageViewSet, FooterViewSet

router = routers.DefaultRouter()
router.register('api/main', MainPageViewSet, 'main')
router.register('api/footer', FooterViewSet, 'footer')

urlpatterns = router.urls