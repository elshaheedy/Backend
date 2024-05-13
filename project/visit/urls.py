'''
Module for defining URL patterns for visit app.
'''
from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('visit', VisitViewSet)
router.register('attachment', AttachmentViewSet)

# from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', include(router.urls)),
    path('statistics/', Statistics.as_view({'get': 'get'}), name='dashboard'),
    





    # path('patients/restore/', PatientViewSet.as_view({'post': 'restore'}), name='patient-restore'),
    # path('patients/deleted/', PatientViewSet.as_view({'get': 'get_deleted'}), name='patient-get-deleted'),

    path('visits/restore/', VisitViewSet.as_view({'post': 'restore'}), name='visit-restore'),
    path('visits/deleted/', VisitViewSet.as_view({'get': 'get_deleted'}), name='visit-get-deleted'),

    path('attachments/restore/', AttachmentViewSet.as_view({'post': 'restore'}), name='attachment-restore'),
    path('attachments/deleted/', AttachmentViewSet.as_view({'get': 'get_deleted'}), name='attachment-get-deleted'),
]
