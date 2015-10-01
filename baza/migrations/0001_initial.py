# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obiekt',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nazwa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypObiektu',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('typ', models.CharField(choices=[('stacja', 'Stacja Paliw'), ('magazyn', 'Magazyn Paliw')], max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='obiekt',
            name='typ',
            field=models.ForeignKey(to='baza.TypObiektu'),
        ),
    ]
