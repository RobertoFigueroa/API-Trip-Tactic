from django.conf import settings
from django.db import models

class Trip(models.Model):
    name = models.CharField(max_length= 200)
    description = models.CharField(max_length=2000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
