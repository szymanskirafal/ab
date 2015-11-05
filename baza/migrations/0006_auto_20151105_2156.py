# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0005_auto_20151020_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='DopuszczeniaLegalizacje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nazwa_urzadzenia', models.CharField(max_length=100)),
                ('nr_urzadzenia', models.CharField(max_length=50)),
                ('opis_czynnosci', models.CharField(max_length=150)),
                ('jednostka_dozorowa', models.CharField(max_length=50)),
                ('data_ostatniej_czynnosci', models.DateField()),
                ('nr_decyzji', models.CharField(max_length=100)),
                ('data_najblizszej_czynnosci', models.DateField()),
                ('osoba_odpowiedzialna_za_nadzor', models.CharField(max_length=100)),
                ('uwagi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Miejsce',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('typ', models.CharField(choices=[('stacja', 'Stacja Paliw'), ('magazyn', 'Magazyn Paliw'), ('budynek', 'Budynek')], max_length=50)),
                ('nazwa', models.CharField(max_length=100)),
                ('adres', models.CharField(max_length=150)),
                ('telefon', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ObiektK',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nazwa', models.CharField(max_length=100)),
                ('dane_techniczne', models.TextField()),
                ('miejsce', models.ForeignKey(to='baza.Miejsce')),
            ],
        ),
        migrations.CreateModel(
            name='PrzegladyTechniczne',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nazwa_urzadzenia', models.CharField(max_length=100)),
                ('nr_urzadzenia', models.CharField(max_length=50)),
                ('opis_czynnosci', models.CharField(max_length=150)),
                ('jednostka_kontrolujaca', models.CharField(max_length=50)),
                ('data_ostatniej_czynnosci', models.DateField()),
                ('nr_protokolu', models.CharField(max_length=100)),
                ('data_najblizszej_czynnosci', models.DateField()),
                ('osoba_odpowiedzialna_za_nadzor', models.CharField(max_length=100)),
                ('uwagi', models.TextField()),
                ('obiektk', models.ForeignKey(to='baza.ObiektK')),
            ],
        ),
        migrations.AddField(
            model_name='dopuszczenialegalizacje',
            name='obiektk',
            field=models.ForeignKey(to='baza.ObiektK'),
        ),
    ]
