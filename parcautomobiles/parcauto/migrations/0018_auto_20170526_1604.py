# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcauto', '0017_auto_20170526_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reparation',
            name='vehicules',
        ),
        migrations.AddField(
            model_name='reparation',
            name='imma',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='raparations', to='parcauto.Vehicule'),
        ),
    ]
