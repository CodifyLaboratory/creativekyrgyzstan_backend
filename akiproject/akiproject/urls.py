from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_urls
# from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Admin urls
    path('admin/', admin.site.urls),

    # Apps urls
    path('api/', include('event.api.urls')),
    path('api/', include('contacts.api.urls')),
    path('api/', include('mainpage.api.urls')),
    path('api/', include('association_member.api.urls')),
    path('api/', include('about_us.api.urls')),
    path('api/', include('submit.api.urls')),
    path('api/', include('resources.api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += doc_urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# TODO: Убрать когда закончится обновления сайта
from django.views.generic import TemplateView
urlpatterns += [
    path('', TemplateView.as_view(template_name='maintenance/maintenance.html')),
]
