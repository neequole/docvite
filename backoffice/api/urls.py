from django.conf.urls import url, include
from rest_framework import routers

from .viewsets import ClientViewSet, DoctorViewSet, InvitationViewSet


router = routers.DefaultRouter()
router.register('clients', ClientViewSet)
router.register('doctors', DoctorViewSet)
router.register('invitations', InvitationViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
