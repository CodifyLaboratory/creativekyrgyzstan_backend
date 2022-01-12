from django.urls import path
from . import views

urlpatterns = [
    path('association_members', views.members_show, name='members')
]
