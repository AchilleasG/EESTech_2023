from django.db import models


# Create your models here.
class Basic_User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=20)
class User (Basic_User):
    total_points = models.IntegerField()

class Therapist(Basic_User):
    user = models.ManyToManyField(User,through='UserTherapist')

class UserTherapist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    has_access = models.BooleanField(default=False)
class Icon(models.Model):
    points_required = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')

