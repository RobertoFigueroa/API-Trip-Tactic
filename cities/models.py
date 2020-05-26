from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(
        'countries.Country',
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )