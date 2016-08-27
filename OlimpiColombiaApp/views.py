from operator import attrgetter

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

## Models
from django.urls import reverse

from .forms import StudentUserForm
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
    athlete = Athlete.objects.get(id=athlete_id)
    sportevents = athlete.sportevent_set.all()
    sportevents = sorted(sportevents, key=attrgetter('date', 'time'), reverse=True)
    for event in sportevents:
        if event.video != None:
            return JsonResponse({'video_url':str(event.video)})
    return JsonResponse({'video_url': str("")})

def register_student(request):
    if request.method == 'POST':
        form = StudentUserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = form.cleaned_data.get['username']
            first_name = form.cleaned_data.get['first_name']
            last_name = form.cleaned_data.get['last_name']
            password = form.cleaned_data.get['password']
            email = cleaned_data.data.get['email']

            user_model = User.objects.create_user(username=username, password=password)
            user_model.fisrt_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            user_model.save()

            return HttpResponseRedirect(reverse('index'))

    else:
        form = StudentUserForm()

    return render(request, 'OlimpiColombiaApp/register.html',{'form':form})
