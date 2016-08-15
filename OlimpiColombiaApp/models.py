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


class Sportman(models.Model):

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
    height  = models.FloatField()

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