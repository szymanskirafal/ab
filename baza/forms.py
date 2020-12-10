
from django.forms import ModelForm, Select, TextInput, Textarea



from .models import Miejsce, ObiektK, DopuszczeniaLegalizacje, PrzegladyTechniczne, Obiekt, Urzadzenie, Przedmiot

from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper


class LoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-control'


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
            'uwagi',
            )
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
                    attrs={
                        'class':'form-control',
                        'placeholder':'format daty 2016-07-01'
                        }
                    ),
                'nr_decyzji': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'data_najblizszej_czynnosci': TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'format daty 2016-07-02'
                        }
                    ),
                'osoba_odpowiedzialna_za_nadzor': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'uwagi': Textarea(
                    attrs={'class':'form-control'}
                    ),

                }


class PrzegladyTechniczneForm(ModelForm):
    class Meta:
        model = PrzegladyTechniczne
        fields = (
            'nazwa_urzadzenia',
            'nr_urzadzenia',
            'opis_czynnosci',
            'jednostka_kontrolujaca',
            'data_ostatniej_czynnosci',
            'nr_protokolu',
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
                'jednostka_kontrolujaca': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'data_ostatniej_czynnosci': TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'format daty 2016-05-21'
                        }
                    ),
                'nr_protokolu': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'data_najblizszej_czynnosci': TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'format daty 2016-05-22'
                        }
                    ),
                'osoba_odpowiedzialna_za_nadzor': TextInput(
                    attrs={'class':'form-control'}
                    ),
                'uwagi': Textarea(
                    attrs={'class':'form-control'}
                    ),
                }





# poniżej stare formsyy ------------------------

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





class SzukajObiektForm(ModelForm):

    class Meta:
        model = Obiekt
        fields = ('typ',)
        widgets = {
                'typ': Select(
                    attrs={'class': 'form-control'}
                    )}

