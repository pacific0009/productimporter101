from django.db import models
# SKU your models here.
class SKU(models.Model):
    name = models.CharField(max_length=250)
    sku = models.CharField(unique=True, max_length=250)
    description = models.CharField(max_length=1000)