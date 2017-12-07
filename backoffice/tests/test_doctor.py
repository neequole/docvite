from rest_framework import status
from rest_framework.test import APITestCase

from backoffice.models import Client, Doctor

from .decorators import needs_doctor_login, needs_client_login


class DoctorTests(APITestCase):
    API_URL = '/api/doctors'
    LOGIN_URL = '{}/login/'.format(API_URL)
    LOGOUT_URL = '{}/logout/'.format(API_URL)
    DOCTOR_ACCOUNT = {'username': 'foo', 'password': 'foo'}
    CLIENT_ACCOUNT = {'username': 'bar', 'password': 'bar'}

    def setUp(self):
        self.client.doctor = Doctor.objects.create_user(**self.DOCTOR_ACCOUNT)
        self.client.client = Client.objects.create_user(**self.CLIENT_ACCOUNT)

    def test_invalid_login(self):
        """ Ensure we return an authentication error """
        request_data = {'username': 'dummy', 'password': 'dummy'}
        response = self.client.post(self.LOGIN_URL, request_data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_client_login(self):
        """ Ensure we check the user is a Doctor """
        response = self.client.post(self.LOGIN_URL, self.CLIENT_ACCOUNT,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_doctor_login(self):
        response = self.client.post(self.LOGIN_URL, self.DOCTOR_ACCOUNT,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @needs_client_login
    def test_client_logout(self):
        """ Ensure we check the session user is a Doctor """
        response = self.client.post(self.LOGOUT_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @needs_doctor_login
    def test_doctor_logout(self):
        response = self.client.post(self.LOGOUT_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @needs_doctor_login
    def test_invitations(self):
        url = '{}/{}/invitations/'.format(self.API_URL, self.client.doctor.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
