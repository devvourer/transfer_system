from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User


class TestUser(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@mail.com', first_name='test', last_name='testovich',
                                   password='test')
        self.user.save()

    def test_user_detail(self):
        self.client.login(email='test@mail.com', password='test')
        client = APIClient()
        response = client.get(f'/detail/{self.user.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
