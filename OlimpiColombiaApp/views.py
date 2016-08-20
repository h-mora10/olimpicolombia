from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

## Models
from OlimpiColombiaApp.models import *

# Create your views here.

def index(request):
    #ToDo write a seed file
    sports = Sport.objects.order_by(('name'))
    sports[0].atletas
    return render(request, 'OlimpiColombiaApp/index.html',{'sports': sports})
def test(request):
    return render(request, 'OlimpiColombiaApp/index.html', )


