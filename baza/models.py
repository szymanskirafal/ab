from django.db import models





class Miejsce(models.Model):
    TYPY_MIEJSC = (
        ('stacja', 'Stacja Paliw'),
        ('magazyn', 'Magazyn Paliw'),
    )

    typ = models.CharField(max_length = 50, choices = TYPY_MIEJSC)
    nazwa = models.CharField(max_length = 100)
    adres = models.CharField(max_length = 150)
    telefon = models.CharField(max_length = 30)
    created_by = models.CharField(max_length = 30, null = True, blank = True)
    grupa = models.CharField(max_length = 20, null = True, blank = True)




class ObiektK(models.Model):
    miejsce = models.ForeignKey(Miejsce)
    nazwa = models.CharField(max_length = 100)
    dane_techniczne = models.TextField()

class DopuszczeniaLegalizacje(models.Model):
    obiektk = models.ForeignKey(ObiektK)
    nazwa_urzadzenia = models.CharField(max_length = 100)
    nr_urzadzenia = models.CharField(max_length = 50, null = True, blank = True)
    opis_czynnosci = models.CharField(max_length = 150)
    jednostka_dozorowa = models.CharField(max_length = 150)
    data_ostatniej_czynnosci = models.DateField(null = True, blank = True)
    nr_decyzji = models.CharField(max_length = 100, null = True, blank = True)
    data_najblizszej_czynnosci = models.DateField()
    osoba_odpowiedzialna_za_nadzor = models.CharField(max_length = 100)
    uwagi = models.TextField(null = True, blank = True)


class ArchiwumDopuszczenie(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    dopuszczenie = models.ForeignKey(DopuszczeniaLegalizacje)
    nazwa_urzadzenia = models.CharField(max_length = 100)
    nr_urzadzenia = models.CharField(max_length = 50, null = True, blank = True)
    opis_czynnosci = models.CharField(max_length = 150)
    jednostka_dozorowa = models.CharField(max_length = 150)
    data_ostatniej_czynnosci = models.DateField(null = True, blank = True)
    nr_decyzji = models.CharField(max_length = 100, null = True, blank = True)
    data_najblizszej_czynnosci = models.DateField()
    osoba_odpowiedzialna_za_nadzor = models.CharField(max_length = 100)
    uwagi = models.TextField(null = True, blank = True)




class PrzegladyTechniczne(models.Model):
    obiektk = models.ForeignKey(ObiektK)
    nazwa_urzadzenia = models.CharField(max_length = 100)
    nr_urzadzenia = models.CharField(max_length = 50, null = True, blank = True)
    opis_czynnosci = models.CharField(max_length = 150)
    jednostka_kontrolujaca = models.CharField(max_length = 150)
    data_ostatniej_czynnosci = models.DateField(null = True, blank = True)
    nr_protokolu = models.CharField(max_length = 100, null = True, blank = True)
    data_najblizszej_czynnosci = models.DateField()
    osoba_odpowiedzialna_za_nadzor = models.CharField(max_length = 100)
    uwagi = models.TextField(null = True, blank = True)



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
