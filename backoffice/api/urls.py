from django.conf.urls import url, include
from rest_framework import routers

from .viewsets import ClientViewSet, DoctorViewSet


router = routers.DefaultRouter()
router.register('clients', ClientViewSet)
router.register('doctors', DoctorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
