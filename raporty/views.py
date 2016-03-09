
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


