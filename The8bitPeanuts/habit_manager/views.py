from django.http import HttpResponse
from user_system.models import *

def newJourney(request, username, journeyname):
    try:
        user = User.objects.get(username=username)
    except:
        pass
        return HttpResponse(404)
    return HttpResponse("Hello, world. You're at the polls index.")