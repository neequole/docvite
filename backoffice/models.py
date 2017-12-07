from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    pass


class Doctor(User):
    class Meta:
        verbose_name = 'Doctor'

    @property
    def referral_code(self):
        return 'BMDOC{}'.format(self.id)


class Client(User):
    class Meta:
        verbose_name = 'Client'


class Invitation(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_REJECTED = 'rejected'
    STATUS_WITHDRAWN = 'withdrawn'

    STATUSES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_WITHDRAWN, 'Withdrawn')
    )

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUSES)
