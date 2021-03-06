# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcauto', '0013_auto_20170526_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicule',
            name='kilomatrage',
        ),
        migrations.AddField(
            model_name='vehicule',
            name='kilometrage',
            field=models.IntegerField(null=True, verbose_name='Kilom\xe9trage'),
        ),
        migrations.AlterField(
            model_name='carnet',
            name='dateFinTravaux',
            field=models.DateTimeField(verbose_name='Date de fin de travaux'),
        ),
        migrations.AlterField(
            model_name='carnet',
            name='imma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicules', to='parcauto.Vehicule', verbose_name='Immatriculation'),
        ),
        migrations.AlterField(
            model_name='carnet',
            name='kilometrage',
            field=models.FloatField(verbose_name='Kilom\xe9trage'),
        ),
        migrations.AlterField(
            model_name='carnet',
            name='motifIntervention',
            field=models.CharField(max_length=50, verbose_name="Motif d' intervention"),
        ),
        migrations.AlterField(
            model_name='carnet',
            name='natureTravaux',
            field=models.CharField(max_length=50, verbose_name='Nature des travaux'),
        ),
        migrations.AlterField(
            model_name='garage',
            name='marqueGarage',
            field=models.CharField(max_length=25, verbose_name='marque du garage'),
        ),
        migrations.AlterField(
            model_name='garage',
            name='nomGarage',
            field=models.CharField(max_length=25, verbose_name='Nom du garage'),
        ),
        migrations.AlterField(
            model_name='garage',
            name='nomGerant',
            field=models.CharField(max_length=25, verbose_name='Nom du g\xe9rant du garage'),
        ),
        migrations.AlterField(
            model_name='reparation',
            name='facture',
            field=models.FloatField(verbose_name='facture de la reparation'),
        ),
        migrations.AlterField(
            model_name='revision',
            name='dateFin',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de fin de r\xe9vision'),
        ),
        migrations.AlterField(
            model_name='revision',
            name='facture',
            field=models.FloatField(verbose_name='Facture de la r\xe9vision'),
        ),
        migrations.AlterField(
            model_name='revision',
            name='natureRevision',
            field=models.CharField(max_length=25, verbose_name='Nature de la r\xe9vision'),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='anneeFabr',
            field=models.DateField(verbose_name='Ann\xe9e de fabrication'),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='carnets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicules', to='parcauto.Carnet', verbose_name='Carnet du  v\xe9hicule'),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='imma',
            field=models.CharField(max_length=25, unique=True, verbose_name='Immatriculation'),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='modeles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modeles', to='parcauto.Modele', verbose_name='Model du v\xe9hicule'),
        ),
    ]
