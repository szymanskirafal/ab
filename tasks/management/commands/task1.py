from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from datetime import date
from grupa.models import CustomGroup


from raporty.managers import ObiektyManager



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        today = date.today()
        current_weekday = today.isoweekday()
        admin_email = User.objects.get(username='RafalSzymanski').email

        if current_weekday == 4:
            groups = CustomGroup.objects.all()
            for group in groups:
                if group.name == 'STACJE PALIW LEGALIZACJE':

                    members_of_group = group.user_set.all()
                    for member in members_of_group:
                        overdue_objects = ObiektyManager.overdue_dopuszczenia(member)
                        current_week_objects = ObiektyManager.dopuszczenia_in_current_week(member)
                        next_week_objects = ObiektyManager.dopuszczenia_in_next_week(member)
                        current_month_objects = ObiektyManager.dopuszczenia_in_current_month(member)
                        template_name = 'tasks/raport.html'

                        context = {
                            'overdue_objects': overdue_objects,
                            'current_week_objects': current_week_objects,
                            'next_week_objects': next_week_objects,
                            'current_month_objects': current_month_objects,
                        }

                        message = render_to_string(template_name, context)
                        subject = 'Terminy przeglądów'
                        from_email = 'Terminy Przeglądów <terminyprzegladow@gmail.com>'
                        send_mail(subject, message, from_email, [admin_email])

                else:
                    members_of_group = group.user_set.all()
                    for member in members_of_group:
                        overdue_objects = ObiektyManager.overdue_objects(member)
                        current_week_objects = ObiektyManager.current_week_objects(member)
                        next_week_objects = ObiektyManager.next_week_objects(member)
                        current_month_objects = ObiektyManager.current_month_objects(member)
                        template_name = 'tasks/raport.html'

                        context = {
                            'overdue_objects': overdue_objects,
                            'current_week_objects': current_week_objects,
                            'next_week_objects': next_week_objects,
                            'current_month_objects': current_month_objects,
                        }

                        message = render_to_string(template_name, context)
                        subject = 'Terminy przeglądów'
                        from_email = 'Terminy Przeglądów <terminyprzegladow@gmail.com>'
                        send_mail(subject, message, from_email, [admin_email])

        else:
            send_mail('Powiadomienie', 'Działam, ale nie wysyłam raportu dzisiaj', 'Terminy Przeglądów <terminyprzegladow@gmail.com>', [admin_email])


