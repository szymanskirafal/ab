# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-01 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0003_auto_20180103_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiwumPrzeglad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nazwa_urzadzenia', models.CharField(max_length=100)),
                ('nr_urzadzenia', models.CharField(blank=True, max_length=50, null=True)),
                ('opis_czynnosci', models.CharField(max_length=150)),
                ('jednostka_kontrolujaca', models.CharField(max_length=150)),
                ('data_ostatniej_czynnosci', models.DateField(blank=True, null=True)),
                ('nr_protokolu', models.CharField(blank=True, max_length=100, null=True)),
                ('data_najblizszej_czynnosci', models.DateField()),
                ('osoba_odpowiedzialna_za_nadzor', models.CharField(max_length=100)),
                ('uwagi', models.TextField(blank=True, null=True)),
                ('przeglad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza.PrzegladyTechniczne')),
            ],
        ),
    ]