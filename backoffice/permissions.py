from rest_framework.permissions import BasePermission

from .models import Doctor


class DoctorOnly(BasePermission):
    def has_permission(self, request, view):
        return Doctor.objects.filter(pk=request.user.pk).exists()
