from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.conf import settings
react_routes = getattr(settings, 'REACT_ROUTES', [])

from .yasg import urlpatterns as doc_urls

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path(r'^(%s)?$' % '|'.join(routes), TemplateView.as_view(template_name='index.html')),
#     path('', TemplateView.as_view(template_name='index.html')),
#     # path('', include('event.urls')),
#     path('', include('event.api.urls')),
#     # path('', include('contacts.urls')),
#     path('', include('contacts.api.urls')),
#     # path('', include('mainpage.urls')),
#     path('', include('mainpage.api.urls')),
#     # path('', include('association_member.urls')),
#     path('', include('association_member.api.urls')),
#     path('', include('about_us.api.urls')),
#     path('', include('submit.api.urls')),
#     path('', include('resources.api.urls')),
#     path('ckeditor/', include('ckeditor_uploader.urls')),
#     # path('', include('submit.urls')),
#     # path('i18n/', include('django.conf.urls.i18n'))
# ]
#
# urlpatterns += doc_urls
#
# for route in react_routes:
#     urlpatterns += [
#         path('{}'.format(route), TemplateView.as_view(template_name='index.html'))
#     ]
#
# from django.conf import settings
# from django.conf.urls.static import static
#
# # urlpatterns += i18n_patterns(
# #     path("", include("submit.urls")),
# #     path('', include('association_member.urls')),
# #     path('', include('mainpage.urls')),
# #     path('', include('contacts.urls')),
# #     path('', include('event.urls')),
# # )
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# TODO: Убрать когда закончится обновления сайта
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='maintenance/maintenance.html')),
]
