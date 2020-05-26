from django.conf import settings
from django.db import models

class UserFeedback(models.Model):
    comment = models.CharField(max_length=2000)
    score = models.IntegerField()
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    place = models.ForeignKey(
        'places.Place',
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )
