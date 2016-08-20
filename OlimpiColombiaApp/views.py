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
def test(request):
    return render(request, 'OlimpiColombiaApp/index.html', )
def sport(request,sportname):
    thissport = Sport.objects.get(name=sportname)
    athletes = Athlete.objects.filter(sport=thissport.id)
    return render(request, 'OlimpiColombiaApp/sport.html',{'athletes':athletes,'sport':sportname})


