
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Country, Currency

class CountryApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.currency1 = Currency.objects.create(name='ZAR')
        self.country1 = Country.objects.create(name='South-Africa', alpha2='SA', alpha3='RSA', deleted=False)
        self.country1.currencies.add(self.currency1)

        self.country2 = Country.objects.create(name='United-States-of-america', alpha2='US', alpha3='USA', deleted=False)

    def test_get_countries(self):
        response = self.client.get('/countries/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_countries_with_currency_filter(self):
        response = self.client.get('/countries/', {'currency': 'ZAR'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_get_country(self):
        response = self.client.get('/countries/SA/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'South-Africa')

    def test_soft_delete_country(self):
        response = self.client.delete('/countries/SA/soft-delete/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Country.objects.get(alpha2='SA').deleted)
