from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    hour = models.DateTimeField()
    description = models.CharField(max_length=2000)
    place = models.ForeignKey(
        'places.Place',
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )
    plan = models.ForeignKey(
        'plans.Plan',
        on_delete= models.CASCADE,
        null=True,
        blank=True
    )
