# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-12-09 22:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0011_auto_20201207_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zadanie',
            name='dopuszczenie',
        ),
        migrations.DeleteModel(
            name='Zadanie',
        ),
    ]
