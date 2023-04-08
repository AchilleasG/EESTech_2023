from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
import datetime
# Create your views here.


def login(request,username):
    request.session['username'] = str(username)
    request.session.save()
    print(request.session['username'])
def logout(request):
    request.session.flush()
    request.session.save()
    return HttpResponseRedirect('/')
def user_profile(request,username):
    user = User.objects.get(username=username)

    img = user.icon.image
    achievements = len(Achievement.objects.filter(user=user))
    delta = datetime.date.today() - user.joined_date
    points = user.total_points
    context = {'image':img, 'achievements' : achievements, 'username' : username, 'days':delta.days, 'points' : points}
    return render(request,'user_profile.html' , context=context)

