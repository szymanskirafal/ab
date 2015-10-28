from django.forms import ModelForm, Select, TextInput, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import Obiekt, Urzadzenie, Przedmiot




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


class UrzadzenieForm(ModelForm):
    class Meta:
        model = Urzadzenie
        fields = ('nazwa', 'lokalizacja', 'nr', 'wytyczne')
        widgets = {
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





class PrzedmiotForm(ModelForm):
    class Meta:
        model = Przedmiot
        fields = ('nazwa', 'lokalizacja', 'nr', 'wytyczne')
        widgets = {
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
       
#class ObiektFormValueIsFieldValue(ObiektForm):
 #    widgets = {
  #           'typ': Select(
 #                attrs={'class': 'form-control', 'value': typ}
  #               ),
   #          'nazwa': TextInput(
    #             attrs={'class':'form-control', 'value': nazwa}
     #            ),
      #       'lokalizacja': TextInput(
       #          attrs={'class':'form-control', 'value': lokalizacja}
        #         ),
         #    'nr': TextInput(
  #               attrs={'class':'form-control', 'value': nr}
   #              ),
    #         'wytyczne': Textarea(
     #            attrs={'class':'form-control', 'value': wytyczne}
      #           ),
       #      }



class SzukajObiektForm(ModelForm):

    class Meta:
        model = Obiekt
        fields = ('typ',)
        widgets = {
                'typ': Select(
                    attrs={'class': 'form-control'}
                    )}
                
