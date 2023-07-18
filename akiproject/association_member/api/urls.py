from rest_framework import routers, urlpatterns
from .views import RulesAndPoliticsViewSet, MembersViewSet

router = routers.SimpleRouter()
router.register('rules_and_politics', RulesAndPoliticsViewSet, 'rules_and_politics')
router.register('members', MembersViewSet, 'members')

urlpatterns = router.urls
