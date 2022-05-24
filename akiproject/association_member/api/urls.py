from rest_framework import routers, urlpatterns
from .views import RulesAndPoliticsViewSet, MembersViewSet

router = routers.SimpleRouter()
router.register('api/rules_and_politics', RulesAndPoliticsViewSet, 'rules_and_politics')
router.register('api/members', MembersViewSet, 'members')

urlpatterns = router.urls