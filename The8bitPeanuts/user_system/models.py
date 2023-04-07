from django.db import models
import datetime

# Create your models here.
class Basic_User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=20)
class User (Basic_User):
    total_points = models.IntegerField()
    icon= models.ForeignKey('Icon', on_delete=models.CASCADE, default=1)
    achievement = models.ManyToManyField('Achievement',through='UserAchievement', blank=True)
    joined_date = models.DateField(default=datetime.date.today)
class Achievement(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(upload_to='media/achievement_icons')

class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
class Day (models.Model):
    date =models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.IntegerField()
class Therapist(Basic_User):
    user = models.ManyToManyField(User,through='UserTherapist', blank=True)

class UserTherapist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    has_access = models.BooleanField(default=False)
class Icon(models.Model):
    points_required = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/user_icons')

