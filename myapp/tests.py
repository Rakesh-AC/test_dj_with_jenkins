from django.test import TestCase
from .models import Item
from django.urls import reverse


class ItemModelTest(TestCase):

    def test_create_item(self):
        item = Item.objects.create(
            name="Test Item", description="This is a test item.")
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.description, "This is a test item.")


class ItemListViewTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Test Item 1",
                            description="This is a test item 1.")
        Item.objects.create(name="Test Item 2",
                            description="This is a test item 2.")

    def test_item_list_view(self):
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Item 1")
        self.assertContains(response, "Test Item 2")
