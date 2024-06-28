from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.tickets.models import Ticket
from apps.users.models import User


class TicketTest(APITestCase):
    def test_crud_ticket(self):
        url = reverse('user-create')

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )

        image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        user_data = {'first_name': 'Kate',
                     'last_name': 'Laster',
                     'username': 'gipo',
                     'email': 'kategipo@yandex.ru',
                     'link': 'gip',
                     'password': '123214124124',
                     'passport': image
                     }

        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password123'
        )
        login = self.client.login(username='admin', password='password123')
        self.assertTrue(login)

        response = self.client.post(url, user_data, format='multipart')
        url = reverse('users-list')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        login = self.client.login(username=user_data['username'], password=user_data['password'])
        self.assertTrue(login)

        url = reverse('ticket_post')
        data = {
            'date': '2024-11-11',
            'city_code_from': 'MAD',
            'city_code_to': 'OPO',
            'adults_count': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)

        login = self.client.login(username='admin', password='password123')
        self.assertTrue(login)

        url = reverse('ticket_list')
        response = self.client.get(url, format='json')

        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            'date': '2024-11-11',
            'city_code_from': 'MAD',
            'city_code_to': 'OPO',
            'adults_count': 2,
        }

        login = self.client.login(username=user_data['username'], password=user_data['password'])
        self.assertTrue(login)

        url = reverse('ticket_update', kwargs={'ticket_id': 1})
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('ticket_get', kwargs={'ticket_id': 1})
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ticket.objects.count(), 1)

        url = reverse('ticket_update', kwargs={'ticket_id': 1})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ticket.objects.count(), 0)

        login = self.client.login(username='admin', password='password123')
        self.assertTrue(login)

        url = reverse('ticket_list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data['results']), 0)

        login = self.client.login(username=user_data['username'], password=user_data['password'])
        self.assertTrue(login)

        url = reverse('ticket_get', kwargs={'ticket_id': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
