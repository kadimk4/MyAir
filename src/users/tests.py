from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UsersTest(APITestCase):

    def test_crud_user(self):

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

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('users-list')
        response = self.client.get(url, format='json')
        user_id = response.data[0]['id']
        self.assertEqual(len(response.data), 1)

        url = reverse('user-change', kwargs={'id': user_id})
        data = {
            'first_name': 'Kate_change',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('user-view', kwargs={'id': user_id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Kate_change')

        url = reverse('user-change', kwargs={'id': user_id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('user-view', kwargs={'id': user_id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
