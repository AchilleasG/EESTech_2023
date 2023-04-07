from django.http import HttpResponse
from django.shortcuts import redirect
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
    return redirect(reverse(refreshStage), kwargs={'journey':journeyname, 'user':username})

def refreshStage(request, journey, user):
    return HttpResponse("yay for" + journey + ' ' + user)