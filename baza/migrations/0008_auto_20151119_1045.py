# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0007_auto_20151119_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dopuszczenialegalizacje',
            name='data_ostatniej_czynnosci',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='przegladytechniczne',
            name='data_ostatniej_czynnosci',
            field=models.DateField(null=True, blank=True),
        ),
    ]
