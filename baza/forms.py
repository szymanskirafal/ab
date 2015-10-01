from django.forms import ModelForm, Select, TextInput, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import Obiekt




class ObiektForm(ModelForm):
    class Meta:
        model = Obiekt
        fields = ('typ', 'nazwa', 'lokalizacja', 'nr', 'wytyczne')
        widgets = {
                'typ': Select(
                    attrs={'class': 'form-control'}
                    ),
                'nazwa': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'lokalizacja': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'nr': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'wytyczne': Textarea(
                    attrs={'class':'form-control'}
                    ),
            }

