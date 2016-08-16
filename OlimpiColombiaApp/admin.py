from django.contrib import admin
from .models import Athlete, Coach, Sport, Event
# Register your models here.
admin.site.register(Coach)
admin.site.register(Athlete)
admin.site.register(Sport)
admin.site.register(Event)
