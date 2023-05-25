from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=5, title="IceCream", price=5.5, inventory=100)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream : 5.5")
