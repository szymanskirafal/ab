from django.db import models

from baza.models import DopuszczeniaLegalizacje


class Zadanie(models.Model):
    dopuszczenie = models.ForeignKey(DopuszczeniaLegalizacje)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tresc = models.TextField(verbose_name="treść")
    termin = models.DateField(verbose_name="termin wykonania")
    wykonawca = models.CharField(max_length = 150, verbose_name="wykonawca")
    wykonane = models.BooleanField(default=False, verbose_name="wykonane")
