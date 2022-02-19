from rest_framework import routers, urlpatterns
from .views import SubmitViewSet

router = routers.DefaultRouter()
router.register('api/submit', SubmitViewSet, 'submit')

urlpatterns = router.urls