'''
Module for defining URL patterns for visit app.
'''
from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('visit', VisitViewSet)
router.register('measurement', MeasurementViewSet)
router.register('attachment', AttachmentViewSet)

# from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', DashboardViewSet.as_view({'get': 'get'}), name='dashboard'),
    
]
