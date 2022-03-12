from rest_framework import status
from rest_framework.test import APITestCase


class UserProfileTestCase(APITestCase):
    profile_url = '/api/users/user-update/'

    def setUp(self):
        url_auth = '/api/users/registration/'
        url_login = '/api/users/login/'

        self.user = self.client.post(url_auth, data={
            'username': 'dummy',
            'email': 'dummy@gmail.com',
            'password': '1234567!'
            })
        self.user.is_active = True

        response = self.client.post(url_login, data={
            'email': 'dummy@gmail.com',
            'password': '1234567!'
            })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.token = response.data['token']

    def test_userprofile_is_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_userprofile_is_not_unauthenticated(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
