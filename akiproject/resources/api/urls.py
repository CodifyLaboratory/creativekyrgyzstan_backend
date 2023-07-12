from rest_framework import routers, urlpatterns
from .views import RecommendationViewSet, FormalRegistrationsViewSet, CreativeProjectViewSet, HeaderTextViewSet

router = routers.DefaultRouter()
router.register('api/recommendations', RecommendationViewSet, 'recommendations')
router.register('api/formals', FormalRegistrationsViewSet, 'formals')
router.register('api/creativeprojects', CreativeProjectViewSet, 'creativeprojects')
router.register('api/headertext', HeaderTextViewSet, 'headertext')

urlpatterns = router.urls