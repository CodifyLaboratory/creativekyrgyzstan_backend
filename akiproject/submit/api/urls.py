from rest_framework import routers, urlpatterns
from .views import SubmitViewSet

router = routers.DefaultRouter()
router.register('submit', SubmitViewSet, 'submit')

urlpatterns = router.urls
