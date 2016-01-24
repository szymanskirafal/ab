from django.db import models
from django.db.models import Q

from baza.models import Miejsce, ObiektK, DopuszczeniaLegalizacje, PrzegladyTechniczne

from .utils import current_week_ends_in


class SelectingObjectsManager(models.Manager):

    def objects_selected_for_current_user(current_user):
        user_groups = current_user.groups.all()

        all_members = []
        for group in user_groups:
            for member in group.user_set.all():
                all_members.append(member.username)

        miejsca = Miejsce.objects.all().filter(created_by__in = all_members)

        obiekty = ObiektK.objects.all().filter(miejsce__in = miejsca)

        objects_selected_for_current_user = DopuszczeniaLegalizacje.objects.all().filter(
            Q(obiektk__in = obiekty))
            #| PrzegladyTechniczne.objects.all().filter(
            #Q(obiektk__in = obiekty))

        return objects_selected_for_current_user



    def current_week_objects(current_user):
        current_week_objects = SelectingObjectsManager.objects_selected_for_current_user(current_user).filter(
            Q(data_najblizszej_czynnosci__lte = current_week_ends_in()))
        return current_week_objects



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