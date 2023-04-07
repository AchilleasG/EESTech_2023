from django.shortcuts import render
from .models import *
import datetime
# Create your views here.

def user_profile(request,username):
    user = User.objects.get(username=username)

    img = user.icon.image
    achievements = len(Achievement.objects.filter(user=user))
    delta = datetime.date.today() - user.joined_date
    points = user.total_points
    context = {'image':img, 'achievements' : achievements, 'username' : username, 'days':delta.days, 'points' : points}
    return render(request,'user_profile.html' , context=context)