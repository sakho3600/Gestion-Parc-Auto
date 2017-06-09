# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motifIntervention', models.CharField(max_length=50)),
                ('natureTravaux', models.CharField(max_length=50)),
                ('dateFinTravaux', models.DateTimeField(auto_now=True)),
                ('kilometrage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Effectuer_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Effectuer_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomGarage', models.CharField(max_length=25)),
                ('nomGerant', models.CharField(max_length=25)),
                ('marqueGarage', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Modele',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbPlace', models.IntegerField()),
                ('puissanceMod', models.IntegerField()),
                ('carburant', models.CharField(max_length=25)),
                ('marqueMod', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Reparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natureReparation', models.CharField(max_length=25)),
                ('dateAccident', models.DateTimeField(auto_now=True)),
                ('dateFin', models.DateTimeField(auto_now=True)),
                ('facture', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natureRevision', models.CharField(max_length=25)),
                ('dateFin', models.DateTimeField(auto_now=True)),
                ('facture', models.FloatField()),
                ('carnets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcauto.Carnet')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imma', models.CharField(max_length=25, unique=True)),
                ('anneeFabr', models.DateTimeField(auto_now=True)),
                ('kilomatrage', models.IntegerField()),
                ('carnets', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='parcauto.Carnet')),
                ('modeles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcauto.Modele')),
            ],
        ),
        migrations.AddField(
            model_name='revision',
            name='vehicules',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcauto.Vehicule'),
        ),
        migrations.AddField(
            model_name='reparation',
            name='vehicules',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcauto.Vehicule'),
        ),
        migrations.AddField(
            model_name='effectuer_2',
            name='garages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcauto.Garage'),
        ),
        migrations.AddField(
            model_name='effectuer_2',
            name='reparations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcauto.Reparation'),
        ),
        migrations.AddField(
            model_name='effectuer_1',
            name='garages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcauto.Garage'),
        ),
        migrations.AddField(
            model_name='effectuer_1',
            name='revisions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcauto.Revision'),
        ),
        migrations.AddField(
            model_name='carnet',
            name='vehicules',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcauto.Vehicule'),
        ),
    ]
