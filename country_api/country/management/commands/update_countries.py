import requests
from django.core.management.base import BaseCommand
from country.models import Country, Currency

class Command(BaseCommand):
    help = 'Update country information from the Restcountries API'

    def handle(self, *args, **options):
        url = 'https://restcountries.com/v3/all'
        response = requests.get(url)

        if response.status_code == 200:
            countries_data = response.json()

            for country_data in countries_data:
                name = country_data.get('name', {}).get('common', '')
                alpha2 = country_data.get('cca2', '')
                alpha3 = country_data.get('cca3', '')
                currencies = country_data.get('currencies', [])
                country, created = Country.objects.update_or_create(
                    alpha2=alpha2,
                    alpha3=alpha3,
                    defaults={'name': name}
                )
                country.currencies.clear()
                for currency_name in currencies:
                    currency, _ = Currency.objects.get_or_create(name=currency_name)
                    country.currencies.add(currency)

                self.stdout.write(self.style.SUCCESS(f'Successfully updated {name}'))

        else:
            self.stdout.write(self.style.ERROR('Failed to fetch country data from the API'))
