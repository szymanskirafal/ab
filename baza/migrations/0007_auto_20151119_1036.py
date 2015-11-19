# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0006_auto_20151105_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dopuszczenialegalizacje',
            name='data_ostatniej_czynnosci',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='przegladytechniczne',
            name='data_ostatniej_czynnosci',
            field=models.DateField(blank=True),
        ),
    ]
