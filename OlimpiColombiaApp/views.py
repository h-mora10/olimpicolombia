from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

## Models
from OlimpiColombiaApp.models import *

# Create your views here.

def index(request):
    #ToDo write a seed file
    sports = Sport.objects.order_by(('name'))
    return render(request, 'OlimpiColombiaApp/index.html',{'sports': sports})

def sport(request,sport_id):
    this_sport = Sport.objects.get(id=sport_id)
    athletes = Athlete.objects.filter(sport=this_sport.id)
    return render(request, 'OlimpiColombiaApp/sport.html',{'athletes':athletes,'sport':this_sport.name})


def calendar(request,athlete_id):
    athlete = Athlete.objects.get(athlete_id)
    events = athlete.events

    return render(request, 'OlimpiColombiaApp/calendar.html')
