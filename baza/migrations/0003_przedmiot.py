# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0002_auto_20151001_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Przedmiot',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nazwa', models.CharField(max_length=100)),
                ('lokalizacja', models.TextField()),
                ('nr', models.CharField(max_length=100)),
                ('wytyczne', models.TextField()),
                ('obiekt', models.ForeignKey(to='baza.Obiekt')),
            ],
        ),
    ]
