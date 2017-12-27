from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.mail import send_mail

from itsdangerous import URLSafeSerializer, base64_encode, base64_decode


class User(AbstractUser):
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


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
    status = models.CharField(max_length=20, choices=STATUSES,
                              default=STATUS_PENDING)
    is_sent = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created',]

    @classmethod
    def send(cls, requester, client):
        """ Sends out new invitation to client's email """
        doctor = Doctor.objects.get(pk=requester.pk)
        invitation = cls.objects.create(doctor=doctor, client=client)
        url = '{}/api/invitations/{}/accept'.format(
            settings.WEBSITE_ORIGIN, invitation.get_hash())
        message = '<a href="{}">Accept!</a><br><br>Your referral code is: {}'.format(
            url, doctor.referral_code)
        send_mail(
            subject='Your Docvite Invitation',
            message='',
            html_message=message,
            from_email='noreply@docvite.com',
            recipient_list=[client.email],
            fail_silently=False,)
        # update if sent
        invitation.is_sent = True
        invitation.save()
        return invitation

    @classmethod
    def deserialize_id(cls, hash):
        s = URLSafeSerializer(settings.SECRET_KEY)
        decoded_hash = base64_decode(hash)
        return s.loads(decoded_hash)

    @classmethod
    def serialize_id(cls, pk):
        s = URLSafeSerializer(settings.SECRET_KEY)
        hashed_pk = s.dumps(pk)
        return base64_encode(hashed_pk).decode('utf-8')

    def get_hash(self):
        return self.serialize_id(self.pk)

    def accept(self):
        self.updated = timezone.now()
        self.status = self.STATUS_CONFIRMED
        self.save()
