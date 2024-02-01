# country_api/urls.py
from django.urls import path
from .views import get_countries, get_country, soft_delete_country

urlpatterns = [
    path('countries/', get_countries, name='get_countries'),
    path('countries/<code>/', get_country, name='get_country'),
    path('countries/<code>/soft-delete/', soft_delete_country, name='soft_delete_country'),
]
