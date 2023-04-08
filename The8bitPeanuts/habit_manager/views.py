from django.http import HttpResponse, JsonResponse
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
    return HttpResponse("done")

def journeyPicker(request):
    journey_list = Journey.objects.all()
    names = []
    desc = []
    images = []
    for i in journey_list:
        names.append(i.name)
        desc.append(i.description)
        images.append(i.image)
    context = {'names':names, 'descriptions':desc, 'images':images}
    return render(request, "", context)

def habitPicker(request, username, journeyname, stage):
    habits_list = JourneyHabitUser.objects.filter(journey=journeyname, user=username)
    habits = [journey_habit.habit for journey_habit in habits_list]
    names = []
    done = []
    for i in habits:
        journey_habit_list = JourneyHabit.objects.filter(habit=i)
        for j in journey_habit_list:
            if j.stage == stage:
                names.append(i.name)
                done.append(JourneyHabitUser.objects.get(habit=i,journey=journeyname, user=username).done)
    context = {'names': names, 'done': done}
    return JsonResponse(context)