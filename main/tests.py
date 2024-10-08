# Create your tests here.
from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_product(self):
        new_product = Product.objects.create(
          name="bulu tangkis",
          description = "senang sih, cuman tadi baju aku basah kena hujan :(",
          price = 8,
          category = "sports",
        )
