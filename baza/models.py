from django.db import models



class Obiekt(models.Model):
    

    TYPY_OBIEKTOW = (
        ('stacja', 'Stacja Paliw'),
        ('magazyn', 'Magazyn Paliw'),
    )

    typ = models.CharField(max_length=100, choices=TYPY_OBIEKTOW)
    
    nazwa = models.CharField(max_length=100)
    lokalizacja = models.CharField(max_length=100, default=None)
    nr = models.CharField(max_length=100, default=None)
    wytyczne = models.TextField(default=None)

class Urzadzenie(models.Model):
    obiekt = models.ForeignKey(Obiekt)
    nazwa = models.CharField(max_length=100)
    lokalizacja = models.TextField()
    nr = models.CharField(max_length=100)
    wytyczne = models.TextField()


class Przedmiot(models.Model):
    obiekt = models.ForeignKey(Obiekt)
    nazwa = models.CharField(max_length=100)
    lokalizacja = models.TextField()
    nr = models.CharField(max_length=100)
    wytyczne = models.TextField()

# Create your models here.
