from django.db import models

class Habit(models.Model):
    TYPES = (
        ('b', 'boolean'),
        ('n', 'numerical')
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=TYPES)
    point_value = models.IntegerField(default=0)

class Journey(models.Model):
    name = models.CharField(max_length=200)
    total_journey_points = models.IntegerField(default=0)
    stage_count = models.IntegerField(default=0)

