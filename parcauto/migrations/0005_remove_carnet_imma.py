# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 08:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcauto', '0004_auto_20170526_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carnet',
            name='imma',
        ),
    ]
