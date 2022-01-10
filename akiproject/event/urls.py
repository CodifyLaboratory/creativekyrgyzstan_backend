from django.urls import path
from . import views

urlpatterns = [
    path('event', views.show_event, name='event')
]
