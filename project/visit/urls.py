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
    path('statistics/', Statistics.as_view({'get': 'get'}), name='dashboard'),
    





    path('deleted-visit/restore/<int:pk>/', DeletedVisitView.as_view({'post':'restore'}), name='visit-restore'),
    path('visit/deleted/', VisitViewSet.as_view({'get': 'get_deleted'}), name='visit-get-deleted'),
    path('deleted-visit/delete/<int:pk>/', DeletedVisitView.as_view({'delete':'destroy'}), name='visit-restore'),

    path('attachment/deleted/', AttachmentViewSet.as_view({'get': 'get_deleted'}), name='attachment-get-deleted'),
    path('deleted-attachment/delete/<int:pk>/', DeletedAttachmentView.as_view({'delete':'destroy'}), name='attachment-restore'),

    path('deleted-attachment/restore/<int:pk>/', DeletedAttachmentView.as_view({'post':'restore'}), name='attachment-restore'),
    path('', include(router.urls)),
]
