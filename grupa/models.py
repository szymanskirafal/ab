from django.db import models

from django.contrib.auth.models import Group


class CustomGroup(Group):
    group_creator = models.CharField(max_length = 30)
    #stacje = models.BooleanField(default = False)
    #magazyny = models.BooleanField(default = False)
