# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-10-10 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupa', '0002_auto_20191010_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customgroup',
            name='magazyny',
        ),
        migrations.RemoveField(
            model_name='customgroup',
            name='stacje',
        ),
    ]