# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0004_urzadzenie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='przedmiot',
            name='obiekt',
        ),
        migrations.AddField(
            model_name='przedmiot',
            name='urzadzenie',
            field=models.ForeignKey(to='baza.Urzadzenie', default=None),
        ),
    ]
