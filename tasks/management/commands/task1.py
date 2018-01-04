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
        if current_weekday == 1:
            groups = CustomGroup.objects.all()
            for group in groups:
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

                    send_mail('Terminy przeglądów', message, 'support@terminyprzegladow.com', [member.email])

        else:
            send_mail('Powiadomienie', 'Działam, ale dzisiaj nie wysyłam', 'support@terminyprzegladow.com', [admin_email])


