from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from datetime import date


from raporty.managers import ObiektyManager



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        today = date.today()
        current_weekday = today.isoweekday()
        mojemail = User.objects.get(username='RafalSzymanski').email
        if current_weekday == 1:
            users = User.objects.all().filter(username__startswith="R")

            for user in users:

                current_user = user
                overdue_objects = ObiektyManager.overdue_objects(current_user)
                current_week_objects = ObiektyManager.current_week_objects(current_user)
                next_week_objects = ObiektyManager.next_week_objects(current_user)
                current_month_objects = ObiektyManager.current_month_objects(current_user)

                template_name = 'tasks/raport.html'

                context = {
                    'overdue_objects': overdue_objects,
                    'current_week_objects': current_week_objects,
                    'next_week_objects': next_week_objects,
                    'current_month_objects': current_month_objects,
                }

                message = render_to_string(template_name, context)

                send_mail('Terminy przeglądów', message, 'email@terminyprzegladow.pl', [user.email])
        else:
            send_mail('Powiadomienie', 'Działam, ale dzisiaj nie wysyłam', 'email@terminyprzegladow.pl', [mojemail])


