from django.db import models

class Transport(models.Model):
    transport_type = models.CharField(max_length=200)
    price = models.FloatField()
    transportProvider = models.ForeignKey(
        'transportProviders.TransportProvider',
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )
    destination = models.ForeignKey(
        'countries.Country',
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )
