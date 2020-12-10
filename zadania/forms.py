from django.forms import ModelForm, Select, TextInput, Textarea

from .models import Zadanie

class ZadanieForm(ModelForm):
    class Meta:
        model = Zadanie
        fields = (
            'tresc',
            'termin',
            'wykonawca',
            )
        widgets = {
                'tresc': Textarea(
                    attrs={'class':'form-control'}
                    ),
                'termin': TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'format daty 2016-07-01'
                        }
                    ),
                'wykonawca': TextInput(
                    attrs={'class':'form-control'}
                    ),

                }