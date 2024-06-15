from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tickets.models import Ticket
from users.models import User


class TicketTest(APITestCase):
    def test_crud_ticket(self):
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

        url = reverse('ticket_post')
        data = {
            'code': 'test_code',
            'place_code': 'test_placecode',
            'user_id': 1,
            'date': '2024-06-14'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.get().code, 'test_code')
        self.assertEqual(Ticket.objects.get().place_code, 'test_placecode')
        self.assertEqual(Ticket.objects.get().date.strftime('%Y-%m-%d'), '2024-06-14')

        url = reverse('ticket_list')
        response = self.client.get(url, format='json')

        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            'code': 'test_code2',
            'place_code': 'test_placecode2',
            'user_id': 1,
            'date': '2024-06-15'
        }
        url = reverse('ticket_update', kwargs={'ticket_id': 1})
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('ticket_get', kwargs={'ticket_id': 1})
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.get().code, 'test_code2')
        self.assertEqual(Ticket.objects.get().place_code, 'test_placecode2')
        self.assertEqual(Ticket.objects.get().date.strftime('%Y-%m-%d'), '2024-06-15')
        url = reverse('ticket_update', kwargs={'ticket_id': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ticket.objects.count(), 0)

        url = reverse('ticket_list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 0)

        url = reverse('ticket_get', kwargs={'ticket_id': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
