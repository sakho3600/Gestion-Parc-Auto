# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcauto', '0020_modele_couleur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modele',
            name='puissanceMod',
            field=models.IntegerField(verbose_name='puissance du model'),
        ),
        migrations.AlterField(
            model_name='reparation',
            name='imma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raparations', to='parcauto.Vehicule', verbose_name='immatriculation '),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='modeles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicules', to='parcauto.Modele', verbose_name='Model du véhicule'),
        ),
    ]
