from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import StudentUserForm
from .models import *

from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseBadRequest
import json
from django.core import serializers

# Create your views here.

def index(request):
    #ToDo write a seed file
    sports = Sport.objects.order_by(('name'))
    dict_sport = [sport.as_dict() for sport in sports]

    return JsonResponse({'sports': dict_sport}, safe=False)

def logout(request):
    return render(request, 'OlimpiColombiaApp/logged_out.html',)

@login_required
def sport(request,sport_id):
    this_sport = Sport.objects.get(id=sport_id)
    dict_sport = this_sport.as_dict()

    athletes = Athlete.objects.filter(sport=this_sport.id)
    dict_athletes = [athlete.as_dict() for athlete in athletes]

    return JsonResponse({'sport': dict_sport, 'athletes': dict_athletes}, safe=False)


@login_required
def calendar(request,athlete_id):
    athlete = Athlete.objects.get(id=athlete_id)
    sportevents = athlete.sportevent_set.all()
    sportevents = sorted(sportevents, key=attrgetter('date', 'time'), reverse=True)

    return render(request, 'OlimpiColombiaApp/calendar.html',{'athlete': athlete, 'sportevents': sportevents})

@login_required
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
        if request.is_ajax():
            student = json.loads(request.body.decode("utf-8"))
            password = Student.objects.make_random_password()
            Student.get_or_set_email(student);
            #user.set_password(password)
            student_model = Student.objects.create_user(username=student["name"],
                                                        first_name=student["first_name"],
                                                        last_name=student["last_name"],
                                                        password=password,
                                                        email=student["email"],
                                                        uid=student["id"])

            student_valid = Student.authenticate(token=student_model.uid)

            if student_valid is not None:
                # Officially log the user in
                login(request, student_valid)
                data = {'success': True}
                return JsonResponse(data)
            else:
                return HttpResponseForbidden()

        else:
            form = StudentUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('email')

                student_model = Student.objects.create_user(username=username, password=password)
                student_model.first_name = first_name
                student_model.last_name = last_name
                student_model.email = email
                student_model.save()

                return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentUserForm()

    return render(request, 'OlimpiColombiaApp/register.html',{'form':form})


def show_student_by_uid(request,student_uid):
    student = Student.objects.filter(uid=student_uid).first()
    if student:
        if student.username and student.password:
            # Test username/password combination
            student_valid = Student.authenticate(token=student_uid)
            # Found a match
            if student_valid is not None:
                # Officially log the user in
                login(request, student_valid)
                data = {'success': True}
                return JsonResponse(data)
            else:
                return HttpResponseForbidden()
        else:
            # Request method is not POST or one of username or password is missing
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotFound()



