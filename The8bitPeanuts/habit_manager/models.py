from django.db import models
from user_system.models import *
from django.utils import timezone

class Habit(models.Model):
    TYPES = (
        ('b', 'boolean'),
        ('n', 'numerical')
    )

    name = models.CharField(max_length=200, primary_key=True)
    type = models.CharField(max_length=1, choices=TYPES)
    point_value = models.IntegerField(default=0)

class Journey(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    r_name = models.CharField(max_length=50)
    stage_count = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media/journey_images')

class HabitUser(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(default=timezone.now)
    times_completed = models.IntegerField(default=0)
    streak = models.FloatField(default=1.0)

class JourneyUser(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_journey_points = models.IntegerField(default=0)
    weekly_journey_points = models.IntegerField(default=0)
    current_stage = models.IntegerField(default=0)
class JourneyHabit(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    stage = models.IntegerField(default=1)

class JourneyHabitUser(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)