__author__ = 'Jasmo2'
# python manage.py shell < seed.py

from OlimpiColombiaApp.models import *
from faker import Factory
fake = Factory.create()

sports_list = [
    'Archery','Badminton','Basketball','Beach volleyball','Boxing','Canoe slalom',
    'Canoe sprint','Cycling - BMX','Cycling - Mountain bike','Cycling - Road','Cycling - Track','Diving',
    'Fencing','Field hockey','Football','Golf','Gymnastics','Handball','Judo','Marathon swimming','Modern pentathlon',
    'Rhythmic gymnastics', 'Rowing', 'Rugby sevens', 'Sailing', 'Shooting', 'Swimming',
    'Synchronized swimming', 'Table tennis', 'Taekwondo', 'Tennis', 'Trampoline', 'Triathlon',
    'Volleyball', 'Water polo', 'Weightlifting', 'Wrestling'
]
def create_Sports():
    for sport_item in sports_list:
        sport = Sport(
         name = sport_item
        )
        sport.save()

create_Sports()
