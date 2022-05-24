from types import prepare_class
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="aki",
        default_version='v1',
        # url = 'localhost:8000',
        description='aki',
        contact=openapi.Contact(email='arkytbekovagulshat@gmail.com')
    ),
    public=True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    # path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema_json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=5), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=5), name='schema-redoc-ui'),
]