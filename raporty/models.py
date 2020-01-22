from django.db import models

from django.contrib.auth.models import User

class ScopeOfEmailReport(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    stations_reports = models.BooleanField(default = True)
    bases_reports = models.BooleanField(default = True)
