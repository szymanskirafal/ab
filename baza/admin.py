from django.contrib import admin
from .models import Miejsce

@admin.register(Miejsce)
class MiejsceAdmin(admin.ModelAdmin):
    pass
