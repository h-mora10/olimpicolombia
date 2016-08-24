from operator import attrgetter

from django.http import JsonResponse
from django.shortcuts import render

## Models
from .models import *

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
    athlete = Athlete.objects.get(id=athlete_id)
    sportevents = athlete.sportevent_set.all()
    sportevents = sorted(sportevents, key=attrgetter('date', 'time'), reverse=True)

    return render(request, 'OlimpiColombiaApp/calendar.html',{'athlete': athlete, 'sportevents': sportevents})

def latest_video_src(request,athlete_id):
    print('Entra a latest')
    athlete = Athlete.objects.get(id=athlete_id)
    print(athlete_id)
    sportevents = athlete.sportevent_set.all()
    print(sportevents)
    sportevents = sorted(sportevents, key=attrgetter('date', 'time'), reverse=True)
    print(sportevents)
    for event in sportevents:
        if event.video != None:
            return JsonResponse({'video_url':str(event.video)})
    return JsonResponse({'video_url': str("")})