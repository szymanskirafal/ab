# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miejsce',
            name='created_by',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
