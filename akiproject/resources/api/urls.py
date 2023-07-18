from rest_framework import routers, urlpatterns
from .views import RecommendationViewSet, FormalRegistrationsViewSet, CreativeProjectViewSet, HeaderTextViewSet

router = routers.DefaultRouter()
router.register('recommendations', RecommendationViewSet, 'recommendations')
router.register('formals', FormalRegistrationsViewSet, 'formals')
router.register('creativeprojects', CreativeProjectViewSet, 'creativeprojects')
router.register('headertext', HeaderTextViewSet, 'headertext')

urlpatterns = router.urls
