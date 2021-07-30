from django.db import models

# Create your models here.
class Climate(models.Model):
    year = models.IntegerField()
    country_or_area = models.CharField(max_length=250)
    value = models.FloatField()
    category = models.CharField(max_length=100)