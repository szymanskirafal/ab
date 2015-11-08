from django.forms import ModelForm, Select, TextInput, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import Miejsce, ObiektK, DopuszczeniaLegalizacje, Obiekt, Urzadzenie, Przedmiot

class MiejsceForm(ModelForm):
    class Meta:
        model = Miejsce
        fields = ('typ', 'nazwa', 'adres', 'telefon')
        widgets = {
                'typ': Select(
                    attrs={'class': 'form-control'}
                    ),
                'nazwa': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'adres': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'telefon': TextInput(
                    attrs={'class':'form-control'}
                    ),
                } 


class ObiektKForm(ModelForm):
    class Meta:
        model = ObiektK
        fields = ('nazwa', 'dane_techniczne')
        widgets = {
                'nazwa': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'dane_techniczne': Textarea(
                    attrs={'class':'form-control'}
                    ),
                } 


class DopuszczeniaLegalizacjeForm(ModelForm):
    class Meta:
        model = DopuszczeniaLegalizacje
        fields = (
            'nazwa_urzadzenia',
            'nr_urzadzenia',
            'opis_czynnosci',
            'jednostka_dozorowa',
            'data_ostatniej_czynnosci',
            'nr_decyzji',
            'data_najblizszej_czynnosci',
            'osoba_odpowiedzialna_za_nadzor',
            'uwagi')
        widgets = {
                'nazwa_urzadzenia': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'nr_urzadzenia': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'opis_czynnosci': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'jednostka_dozorowa': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'data_ostatniej_czynnosci': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'nr_decyzji': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'data_najblizszej_czynnosci': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'osoba_odpowiedzialna_za_nadzor': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'uwagi': Textarea(
                    attrs={'class':'form-control'}
                    ),
                } 
# poniżej stare fomrsyy ------------------------

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



class StacjaForm(ObiektForm):
    class Meta(ObiektForm.Meta):
        exclude = ('typ',)






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
                
