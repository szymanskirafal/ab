from django.db import models

from django.contrib.auth.models import Group


class CustomGroup(Group):
    group_creator = models.CharField(max_length = 30)
