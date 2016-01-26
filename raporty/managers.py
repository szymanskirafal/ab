from django.db import models
from django.db.models import Q

from itertools import chain
from operator import attrgetter

from baza.models import Miejsce, ObiektK, DopuszczeniaLegalizacje, PrzegladyTechniczne

from .utils import DateRanges


# class MembersManager(models.Manager):


def all_members_in_current_user_groups(current_user):
    user_groups = current_user.groups.all()

    all_members = []
    for group in user_groups:
        for member in group.user_set.all():
            all_members.append(member.username)

    return all_members



class ObiektyManager(models.Manager):

    def objects_selected_for_current_user(current_user):
        all_members = all_members_in_current_user_groups(current_user)
        miejsca = Miejsce.objects.all().filter(created_by__in = all_members)
        obiekty = ObiektK.objects.all().filter(miejsce__in = miejsca)
        return obiekty



    def dopuszczenia(current_user):
        obiekty = ObiektyManager.objects_selected_for_current_user(current_user)
        dopuszczenia = DopuszczeniaLegalizacje.objects.all().filter(Q(obiektk__in = obiekty))
        return dopuszczenia

    def przeglady(current_user):
        obiekty = ObiektyManager.objects_selected_for_current_user(current_user)
        przeglady = PrzegladyTechniczne.objects.all().filter(Q(obiektk__in = obiekty))
        return przeglady



    def overdue_dopuszczenia(current_user):
        dopuszczenia = ObiektyManager.dopuszczenia(current_user).filter(Q(data_najblizszej_czynnosci__lt = DateRanges.current_date))
        return dopuszczenia

    def overdue_przeglady(current_user):
        przeglady = ObiektyManager.przeglady(current_user).filter(Q(data_najblizszej_czynnosci__lt = DateRanges.current_date))
        return przeglady



    def dopuszczenia_in_current_week(current_user):
        dopuszczenia = ObiektyManager.dopuszczenia(current_user).filter(
            Q(data_najblizszej_czynnosci__gte = DateRanges.current_date),
            Q(data_najblizszej_czynnosci__lte = DateRanges.current_week_ends_in()))
        return dopuszczenia

    def przeglady_in_current_week(current_user):
        przeglady = ObiektyManager.przeglady(current_user).filter(
            Q(data_najblizszej_czynnosci__gte = DateRanges.current_date),
            Q(data_najblizszej_czynnosci__lte = DateRanges.current_week_ends_in()))
        return przeglady



    def dopuszczenia_in_next_week(current_user):
        dopuszczenia = ObiektyManager.dopuszczenia(current_user).filter(
            Q(data_najblizszej_czynnosci__gt = DateRanges.current_week_ends_in()),
            Q(data_najblizszej_czynnosci__lte = DateRanges.next_week_ends_in()))
        return dopuszczenia

    def przeglady_in_next_week(current_user):
        przeglady = ObiektyManager.przeglady(current_user).filter(
            Q(data_najblizszej_czynnosci__gt = DateRanges.current_week_ends_in()),
            Q(data_najblizszej_czynnosci__lte = DateRanges.next_week_ends_in()))
        return przeglady



    def dopuszczenia_in_current_month(current_user):
        dopuszczenia = ObiektyManager.dopuszczenia(current_user).filter(
            Q(data_najblizszej_czynnosci__gt = DateRanges.next_week_ends_in()),
            Q(data_najblizszej_czynnosci__lte = DateRanges.current_month_ends_in()))
        return dopuszczenia

    def przeglady_in_current_month(current_user):
        przeglady = ObiektyManager.przeglady(current_user).filter(
            Q(data_najblizszej_czynnosci__gt = DateRanges.next_week_ends_in()),
            Q(data_najblizszej_czynnosci__lte = DateRanges.current_month_ends_in()))
        return przeglady




    def overdue_objects(current_user):
        query1 = ObiektyManager.overdue_dopuszczenia(current_user)
        query2 = ObiektyManager.overdue_przeglady(current_user)
        overdue_objects = sorted(chain(query1, query2), key=attrgetter('data_najblizszej_czynnosci'))
        return overdue_objects

    def current_week_objects(current_user):
        query1 = ObiektyManager.dopuszczenia_in_current_week(current_user)
        query2 = ObiektyManager.przeglady_in_current_week(current_user)
        current_week_objects = sorted(chain(query1, query2), key=attrgetter('data_najblizszej_czynnosci'))
        return current_week_objects

    def next_week_objects(current_user):
        query1 = ObiektyManager.dopuszczenia_in_next_week(current_user)
        query2 = ObiektyManager.przeglady_in_next_week(current_user)
        next_week_objects = sorted(chain(query1, query2), key=attrgetter('data_najblizszej_czynnosci'))
        return next_week_objects

    def current_month_objects(current_user):
        query1 = ObiektyManager.dopuszczenia_in_current_month(current_user)
        query2 = ObiektyManager.przeglady_in_current_month(current_user)
        current_month_objects = sorted(chain(query1, query2), key=attrgetter('data_najblizszej_czynnosci'))
        return current_month_objects




    # wszystkie obiekty:
    # miejsce
    #    obiekt
    #        dopuszczenie
    #        przegląd

    # czyli wszystkie miejsca stworzone przez current user lub kolegów z jego grup
    # kto jest current user
    # w jakich grupach
    # kim są koledzy z grup

    # check if current_user belongs to some group






    # obiekty, których termin mija w tym tygodniu
    # obiekty, których 'data_najbliższej_czynnosci' jest mniejsza, niż 'this_week_ends_in'
    # obiekty, to:





    # 'data_najblizszej_czynnosci__lte = this_week_ends_in
    # 'this_week_ends_in', to:




    # return render(request, 'raporty/raport.html',
    #    {
    #        'current_date': current_date,
    #        'current_date2': current_date2,
    #        'current_weekday': current_weekday,
    #        'days_remaining_to_full_week': days_remaining_to_full_week,
    #        'this_week_ends_in': this_week_ends_in,
    #        'next_week_starts_in': next_week_starts_in,
    #       'next_week_ends_in': next_week_ends_in,
    #        'rest_of_this_month_starts_in': rest_of_this_month_starts_in,
     #       'this_month': this_month,
      #      'this_year': this_year,
       #     'weekday_of_first_day': weekday_of_first_day,
        #    'number_of_days': number_of_days,
         #   'this_month_ends_in': this_month_ends_in,
          #  'next_month_starts_in': next_month_starts_in,
           #'miejsca': miejsca,
            #'obiekty': obiekty,
            #'dopuszczenia': dopuszczenia,
            #'przeglady': przeglady,

            #})


# Create your models here.