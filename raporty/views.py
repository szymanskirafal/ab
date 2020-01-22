from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .managers import ObiektyManager

def raport(request):
    current_user = request.user
    overdue_objects = ObiektyManager.overdue_objects(current_user)
    current_week_objects = ObiektyManager.current_week_objects(current_user)
    next_week_objects = ObiektyManager.next_week_objects(current_user)
    current_month_objects = ObiektyManager.current_month_objects(current_user)
    context = {
        'overdue_objects': overdue_objects,
        'current_week_objects': current_week_objects,
        'next_week_objects': next_week_objects,
        'current_month_objects': current_month_objects,
        }

    return render(request, 'raporty/raport.html', context)

def raport_nowy(request):
    current_user = request.user
    overdue_objects = ObiektyManager.overdue_objects(current_user)
    current_week_objects = ObiektyManager.current_week_objects(current_user)
    next_week_objects = ObiektyManager.next_week_objects(current_user)
    current_month_objects = ObiektyManager.current_month_objects(current_user)
    context = {
        'overdue_objects': overdue_objects,
        'current_week_objects': current_week_objects,
        'next_week_objects': next_week_objects,
        'current_month_objects': current_month_objects,
        }

    return render(request, 'raporty/raport.html', context)

