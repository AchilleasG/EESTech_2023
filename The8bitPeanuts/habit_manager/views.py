from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from user_system.models import *
from .models import *

def newJourney(request, username, journeyname):
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponse(404)
    try:
        journey = Journey.objects.get(name=journeyname)
    except:
        return HttpResponse(404)

    connection = JourneyUser.objects.create(journey= journey,user = user,current_stage=1)
    connection.save()
    return redirect(refreshStage, journeyname=journeyname, username=username, stage=1)

def refreshStage(request, journeyname, username,stage):
    journey_habits = JourneyHabit.objects.filter(journey=journeyname, stage=stage)
    habits = [journey_habit.habit for journey_habit in journey_habits]
    user = User.objects.get(username=username)
    for i in habits:
        connection = HabitUser.objects.create(habit=i,user=user)
        connection.save()
    return render(request, 'journey_habit_list.html', {'habits': habits})