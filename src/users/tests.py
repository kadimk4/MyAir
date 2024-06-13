from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UsersTest(APITestCase):

    def test_create_user(self):
        url = reverse('user-create')
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        data = {'first_name': 'Kate',
                'last_name': 'Laster',
                'username': 'gipo',
                'email': 'kategipo@yandex.ru',
                'link': 'gip',
                'password': '123214124124',
                'passport': image
                }
        response = self.client.post(url, data, format='multipart')
        url = reverse('users-list')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data['results']), 1)
