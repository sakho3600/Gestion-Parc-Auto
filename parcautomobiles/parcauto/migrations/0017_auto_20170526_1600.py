# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcauto', '0016_auto_20170526_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparation',
            name='vehicules',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veihcules', to='parcauto.Vehicule'),
        ),
    ]
