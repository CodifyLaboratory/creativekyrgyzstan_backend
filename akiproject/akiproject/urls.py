"""akiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.conf import settings
react_routes = getattr(settings, 'REACT_ROUTES', [])

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^(%s)?$' % '|'.join(routes), TemplateView.as_view(template_name='index.html')),
    path('', TemplateView.as_view(template_name='index.html')),
    # path('', include('event.urls')),
    path('', include('event.api.urls')),
    # path('', include('contacts.urls')),
    path('', include('contacts.api.urls')),
    # path('', include('mainpage.urls')),
    path('', include('mainpage.api.urls')),
    # path('', include('association_member.urls')),
    path('', include('association_member.api.urls')),
    path('', include('about_us.api.urls')),
    path('', include('submit.api.urls')),
    path('', include('resources.api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('', include('submit.urls')),
    # path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += doc_urls

for route in react_routes:
    urlpatterns += [
        path('{}'.format(route), TemplateView.as_view(template_name='index.html'))
    ]

from django.conf import settings
from django.conf.urls.static import static

# urlpatterns += i18n_patterns(
#     path("", include("submit.urls")),
#     path('', include('association_member.urls')),
#     path('', include('mainpage.urls')),
#     path('', include('contacts.urls')),
#     path('', include('event.urls')),
# )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
