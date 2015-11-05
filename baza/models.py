from django.db import models




class Miejsce(models.Model):
    TYPY_MIEJSC = (
        ('stacja', 'Stacja Paliw'),
        ('magazyn', 'Magazyn Paliw'),
        ('budynek', 'Budynek'),
    )

    typ = models.CharField(max_length = 50, choices = TYPY_MIEJSC)
    nazwa = models.CharField(max_length = 100)
    adres = models.CharField(max_length = 150)
    telefon = models.CharField(max_length = 30)



class ObiektK(models.Model):
    miejsce = models.ForeignKey(Miejsce)
    nazwa = models.CharField(max_length = 100)
    dane_techniczne = models.TextField()

class DopuszczeniaLegalizacje(models.Model):
    obiektk = models.ForeignKey(ObiektK)
    nazwa_urzadzenia = models.CharField(max_length = 100)
    nr_urzadzenia = models.CharField(max_length = 50)
    opis_czynnosci = models.CharField(max_length = 150)
    jednostka_dozorowa = models.CharField(max_length = 50)
    data_ostatniej_czynnosci = models.DateField()
    nr_decyzji = models.CharField(max_length = 100)
    data_najblizszej_czynnosci = models.DateField()
    osoba_odpowiedzialna_za_nadzor = models.CharField(max_length = 100)
    uwagi = models.TextField()

class PrzegladyTechniczne(models.Model):
    obiektk = models.ForeignKey(ObiektK)
    nazwa_urzadzenia = models.CharField(max_length = 100)
    nr_urzadzenia = models.CharField(max_length = 50)
    opis_czynnosci = models.CharField(max_length = 150)
    jednostka_kontrolujaca = models.CharField(max_length = 50)
    data_ostatniej_czynnosci = models.DateField()
    nr_protokolu = models.CharField(max_length = 100)
    data_najblizszej_czynnosci = models.DateField()
    osoba_odpowiedzialna_za_nadzor = models.CharField(max_length = 100)
    uwagi = models.TextField()



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
    urzadzenie = models.ForeignKey(Urzadzenie, default=None)
    nazwa = models.CharField(max_length=100)
    lokalizacja = models.TextField()
    nr = models.CharField(max_length=100)
    wytyczne = models.TextField()

# Create your models here.
