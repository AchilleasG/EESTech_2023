from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from user_system.models import *
from .models import *

def newJourney(request, journeyname):
    try:
        username = request.session['username']
    except KeyError as ke:
        print("nope")
        return redirect('/')
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
    ids = []
    for i in journey_list:
        names.append(i.r_name)
        ids.append(i.name)
        desc.append(i.description)
        images.append(i.image.url)
    context = {'names':json.dumps(names), 'descriptions':json.dumps(desc), 'images':json.dumps(images), 'ids':json.dumps(ids)}
    return render(request, "journey_picker.html", context)

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

def completeHabit(request, username, journeyname, habitname):
    try:
        habitUser = HabitUser.objects.get(habit=habitname,user=username)
        journeyHabitUser = JourneyHabitUser.objects.get(journey=journeyname, user=username, habit=habitname)
    except:
        return HttpResponse(404)
    habitUser.times_completed += 1
    new_streak = 1.0 + (habitUser.times_completed//5)*0.1
    if new_streak != habitUser.streak:
        habitUser.streak = new_streak
    journeyHabitUser.done = True
    habitUser.save()
    journeyHabitUser.save()
    return HttpResponse(200)