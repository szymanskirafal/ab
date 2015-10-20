# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0003_przedmiot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urzadzenie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nazwa', models.CharField(max_length=100)),
                ('lokalizacja', models.TextField()),
                ('nr', models.CharField(max_length=100)),
                ('wytyczne', models.TextField()),
                ('obiekt', models.ForeignKey(to='baza.Obiekt')),
            ],
        ),
    ]
