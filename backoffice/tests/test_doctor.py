from rest_framework import status
from rest_framework.test import APITestCase

from backoffice.models import Client, Doctor


class DoctorTests(APITestCase):
    API_URL = '/api/doctors'
    LOGIN_URL = '{}/login/'.format(API_URL)
    LOGOUT_URL = '{}/logout/'.format(API_URL)
    VALID_DOCTOR = {'username': 'foo', 'password': 'foo'}
    INVALID_DOCTOR = {'username': 'bar', 'password': 'bar'}

    def setUp(self):
        Doctor.objects.create_user(**self.VALID_DOCTOR)
        Client.objects.create_user(**self.INVALID_DOCTOR)

    def test_invalid_login(self):
        """ Ensure we return an authentication error """
        request_data = {'username': 'dummy', 'password': 'dummy'}
        response = self.client.post(self.LOGIN_URL, request_data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_client_login(self):
        """ Ensure we check the user is a Doctor """
        response = self.client.post(self.LOGIN_URL, self.INVALID_DOCTOR,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_doctor_login(self):
        response = self.client.post(self.LOGIN_URL, self.VALID_DOCTOR,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.client.login(**self.VALID_DOCTOR)
        response = self.client.post(self.LOGOUT_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
