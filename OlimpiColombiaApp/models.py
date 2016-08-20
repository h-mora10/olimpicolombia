from __future__ import unicode_literals

from django.db import models

from datetime import date
# Create your models here.


class Coach(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,

    )

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])



class Sport(models.Model):

    name = models.CharField(
        max_length=255,
    )
    img_url = models.ImageField(
        null=True,
    )

    def __str__(self):

        return ' '.join([
            self.name,
        ])


class SportEvent(models.Model):

    date = models.DateField()
    time = models.TimeField()
    sport_event = models.CharField(
        max_length=400,
    )
    sport = models.ForeignKey(Sport)
    result = models.CharField(
        max_length=255,
    )
    video = models.FileField()

    def __str__(self):

        return ' '.join([
            self.date,
            self.time,
            self.sport_event,
            self.athlete,
            self.sport,
            self.result
        ])
    

class Athlete(models.Model):
    img_url = models.ImageField(
        null=True,
    )
    sport = models.ForeignKey(Sport)
    sportevents = models.ManyToManyField(SportEvent)
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,

    )
    birth_place = models.CharField(
        max_length=400,

    )
    birth_date = models.DateField()

    weight = models.FloatField()
    height = models.FloatField()

    coach = models.ForeignKey(Coach)

    def age(self):
        born = self.birth_date
        today = date.today()
        return today.year - born.year # - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])
