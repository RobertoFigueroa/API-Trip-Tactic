from django.db import models

class TransportProvider(models.Model):
    name = models.CharField(max_length=200)
