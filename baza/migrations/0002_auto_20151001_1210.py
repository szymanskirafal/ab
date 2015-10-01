# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obiekt',
            name='lokalizacja',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='obiekt',
            name='nr',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='obiekt',
            name='wytyczne',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='obiekt',
            name='typ',
            field=models.CharField(choices=[('stacja', 'Stacja Paliw'), ('magazyn', 'Magazyn Paliw')], max_length=100),
        ),
        migrations.DeleteModel(
            name='TypObiektu',
        ),
    ]
