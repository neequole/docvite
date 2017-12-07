from rest_framework import status
from rest_framework.test import APITestCase

from backoffice.models import Client, Doctor, Invitation

from .decorators import needs_doctor_login, needs_client_login


class ClientTests(APITestCase):
    API_URL = '/api/clients'
    DOCTOR_ACCOUNT = {'username': 'foo', 'password': 'foo'}
    CLIENT_ACCOUNT = {'username': 'bar', 'password': 'bar'}

    def setUp(self):
        self.client.doctor = Doctor.objects.create_user(**self.DOCTOR_ACCOUNT)
        self.client.client = Client.objects.create_user(
            **self.CLIENT_ACCOUNT, email='bar@gmail.com')

    def test_anonymous_invite(self):
        """ Ensure anonymous users cannot perform invite """
        url = '{}/invite/'.format(self.API_URL)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @needs_client_login
    def test_client_invite(self):
        """ Ensure clients cannot perform invite """
        url = '{}/invite/'.format(self.API_URL)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @needs_doctor_login
    def test_invite_missing_email(self):
        """ Ensure we require e-mail during invite """
        url = '{}/invite/'.format(self.API_URL)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    @needs_doctor_login
    def test_invite_nonclient_email(self):
        """ Ensure we check that the e-mail belongs to a Client """
        url = '{}/invite/'.format(self.API_URL)
        request_data = {'email': 'test@gmail.com'}
        response = self.client.post(url, request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    @needs_doctor_login
    def test_invite(self):
        """ Ensure we create new invitations """
        url = '{}/invite/'.format(self.API_URL)
        request_data = {'email': 'bar@gmail.com'}
        response = self.client.post(url, request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['doctor'], self.client.doctor.pk)
        self.assertEqual(response.data['client'], self.client.client.pk)
        self.assertIn('created', response.data)
        self.assertEqual(response.data['status'], Invitation.STATUS_PENDING)
        self.assertTrue(response.data['is_sent'])
