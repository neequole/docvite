from rest_framework import status
from rest_framework.test import APITestCase

from backoffice.models import Client, Doctor, Invitation


class InvitationTests(APITestCase):
    API_URL = '/api/invitations'
    DOCTOR_ACCOUNT = {'username': 'foo', 'password': 'foo'}
    CLIENT_ACCOUNT = {'username': 'bar', 'password': 'bar'}

    def setUp(self):
        self.client.doctor = Doctor.objects.create_user(**self.DOCTOR_ACCOUNT)
        self.client.client = Client.objects.create_user(**self.CLIENT_ACCOUNT)
        self.client.invitation = Invitation.objects.create(
            doctor=self.client.doctor, client=self.client.client)

    def test_accept_invalid_hash(self):
        """ Ensure we check invalid hash """
        url = '{}/MTAw/accept/'.format(self.API_URL)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_accept_not_found(self):
        """ Ensure we check hash pk is an Invitation """
        hash_pk = Invitation.serialize_id(9999)
        url = '{}/{}/accept/'.format(self.API_URL, hash_pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_accept(self):
        """ Ensure we update Invitation once accepted """
        hash_pk = Invitation.serialize_id(self.client.invitation.pk)
        url = '{}/{}/accept/'.format(self.API_URL, hash_pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['doctor'], self.client.doctor.pk)
        self.assertEqual(response.data['client'], self.client.client.pk)
        self.assertEqual(response.data['status'], Invitation.STATUS_CONFIRMED)
        self.assertIsNotNone(response.data['updated'])
