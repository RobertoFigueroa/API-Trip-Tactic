from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    trip = models.ForeignKey(
        'trips.Trip',
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )