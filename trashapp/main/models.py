from django.db import models

# Create your models here.

class DistanceMeasurement(models.Model):
    distance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.distance} cm"
