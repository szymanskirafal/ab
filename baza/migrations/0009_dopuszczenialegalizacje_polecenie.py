# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-12-03 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0008_auto_20201203_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='dopuszczenialegalizacje',
            name='polecenie',
            field=models.TextField(blank=True, null=True),
        ),
    ]
