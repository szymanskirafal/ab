from django.shortcuts import render


from .managers import ObiektyManager



def raport(request):
    current_user = request.user
    overdue_objects = ObiektyManager.overdue_objects(current_user)
    current_week_objects = ObiektyManager.current_week_objects(current_user)
    next_week_objects = ObiektyManager.next_week_objects(current_user)
    current_month_objects = ObiektyManager.current_month_objects(current_user)

    return render(request, 'raporty/raport.html',
        {
            'overdue_objects': overdue_objects,
            'current_week_objects': current_week_objects,
            'next_week_objects': next_week_objects,
            'current_month_objects': current_month_objects,
            })


#
 #   return render(request, 'raporty/raport.html',
  #      {
   #         'current_date': current_date,
    #        'current_date2': current_date2,
     #       'current_weekday': current_weekday,
#            'days_remaining_to_full_week': days_remaining_to_full_week,
 #           'this_week_ends_in': this_week_ends_in,
  #          'next_week_starts_in': next_week_starts_in,
   #         'next_week_ends_in': next_week_ends_in,
    #        'rest_of_this_month_starts_in': rest_of_this_month_starts_in,
#            'this_month': this_month,
 #           'this_year': this_year,
  #          'weekday_of_first_day': weekday_of_first_day,
   #         'number_of_days': number_of_days,
    #        'this_month_ends_in': this_month_ends_in,
#
#            'next_month_ends_in': next_month_ends_in,
#            'miejsca': miejsca,
 #           'obiekty': obiekty,
  #          'dopuszczenia': dopuszczenia,
   #         'przeglady': przeglady,
    #        'nowe_obiekty': nowe_obiekty,

     #       })
# Create your views here.
