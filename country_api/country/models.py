from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=50)

class Country(models.Model):
    name = models.CharField(max_length=100)
    alpha2 = models.CharField(max_length=2, unique=True)
    alpha3 = models.CharField(max_length=3, unique=True)
    currencies = models.ManyToManyField(Currency)
    deleted = models.BooleanField(default=False)
