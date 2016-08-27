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
        upload_to='sports',
        max_length=1000,
    )

    def __str__(self):

        return ' '.join([
            self.name,
        ])


class Athlete(models.Model):
    img_url = models.ImageField(
        null=True,
        upload_to='athletes',
        max_length=1000,
    )
    sport = models.ForeignKey(Sport)
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
            self.last_name + ' - ',
            self.sport.name,
        ])


class SportEvent(models.Model):
    athletes = models.ManyToManyField(Athlete, blank=True)

    date = models.DateField()
    time = models.TimeField()
    sport_event = models.CharField(
        max_length=400,
    )
    sport = models.ForeignKey(Sport)
    result = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    video = models.FileField(
        null=True,
        blank=True,
        upload_to='events',
        max_length=1000,
    )

    def __str__(self):

        return ' '.join([
            '{:%m/%d/%Y}'.format(self.date) + ' ',
            '{:%H:%M:%S}'.format(self.time) + ' - ',
            self.sport.name + ' - ',
            self.sport_event,

        ])

    def save(self, *args, **kwargs):
        if not self.result:
            self.result = None
        if not self.video:
            self.video = None
        super(SportEvent, self).save(*args, **kwargs)

