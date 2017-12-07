from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Client, Doctor, Invitation


class DoctorAdmin(UserAdmin):
    pass


class ClientAdmin(UserAdmin):
    pass


# Register your models here.
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Invitation)
