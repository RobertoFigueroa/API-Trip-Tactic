from django.db import models

class Place(models.Model):
    name = models.CharField(max_length= 200)
    place_type = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    city = models.ForeignKey(
        'cities.City',
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )
