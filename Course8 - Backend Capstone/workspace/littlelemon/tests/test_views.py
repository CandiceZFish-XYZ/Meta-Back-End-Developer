from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('menu')
        item = Menu.objects.create(id=6, title="IceCream2", price=7, inventory=200)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
       
    def test_getall(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
