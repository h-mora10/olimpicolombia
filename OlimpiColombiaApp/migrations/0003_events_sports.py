# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OlimpiColombiaApp', '0002_sportman'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('sport_event', models.CharField(max_length=400)),
                ('result', models.CharField(max_length=255)),
                ('video', models.FileField(upload_to=b'')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OlimpiColombiaApp.Sportman')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OlimpiColombiaApp.Sport'),
        ),
    ]
