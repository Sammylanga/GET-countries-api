from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models
from .models import Country

@api_view(['GET'])
def get_countries(request):
    currency_filter = request.query_params.get('currency', None)

    if currency_filter:
        countries = Country.objects.filter(currencies__name=currency_filter, deleted=False)
    else:
        countries = Country.objects.filter(deleted=False)

    data = [
        {'name': country.name, 'alpha2': country.alpha2, 'alpha3': country.alpha3, 'currencies': [currency.name for currency in country.currencies.all()]}
        for country in countries
    ]
    return Response(data)

@api_view(['GET'])
def get_country(request, code):
    country = get_object_or_404(Country, models.Q(alpha2=code) | models.Q(alpha3=code), deleted=False)
    data = {'name': country.name, 'alpha2': country.alpha2, 'alpha3': country.alpha3, 'currencies': [currency.name for currency in country.currencies.all()]}
    return Response(data)

@api_view(['DELETE'])
def soft_delete_country(request, code):
    country = get_object_or_404(Country, models.Q(alpha2=code) | models.Q(alpha3=code), deleted=False)
    country.deleted = True
    country.save()
    return Response({'message': 'Country soft-deleted successfully'})
