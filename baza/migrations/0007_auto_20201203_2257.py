# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-12-03 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0006_auto_20201203_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dopuszczenialegalizacje',
            name='termin_wykonania_zalecen',
        ),
        migrations.AddField(
            model_name='dopuszczenialegalizacje',
            name='termin_wykonania_polecenia',
            field=models.DateField(blank=True, null=True, verbose_name='termin wykonania zalecenia'),
        ),
    ]
