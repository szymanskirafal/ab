from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime


from .forms import MiejsceForm, ObiektKForm, DopuszczeniaLegalizacjeForm, PrzegladyTechniczneForm, ObiektForm, StacjaForm, SzukajObiektForm, UrzadzenieForm, PrzedmiotForm
from .models import Miejsce, ObiektK, DopuszczeniaLegalizacje, ArchiwumDopuszczenie, PrzegladyTechniczne, ArchiwumPrzeglad, Obiekt, Urzadzenie, Przedmiot

# from grupa.models import CustomGroup

class BazyListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'miejsca'
    template_name = "baza/bazy.html"

    def get_queryset(self, *args, **kwargs):
        return Miejsce.objects.all().filter(typ='magazyn')

class StacjeListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'miejsca'
    template_name = "baza/stacje.html"

    def get_queryset(self, *args, **kwargs):
        return Miejsce.objects.all().filter(typ='stacja')


class ArchiwumListView(LoginRequiredMixin, generic.ListView):

    context_object_name = 'archiwum_lista'
    template_name = "baza/archiwum.html"

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs['obiekt_id']
        self.dopuszczenie = DopuszczeniaLegalizacje.objects.get(pk = pk)
        return ArchiwumDopuszczenie.objects.all().filter(dopuszczenie=self.dopuszczenie)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dopuszczenie'] = self.dopuszczenie
        return context


class ArchiwumDetailView(LoginRequiredMixin, generic.DetailView):

    model = ArchiwumDopuszczenie
    template_name = "baza/archiwum-detail.html"


class ArchiwumDopuszczenieDeleteView(LoginRequiredMixin, generic.DeleteView):

    model = ArchiwumDopuszczenie
    template_name = "baza/archiwum-dopuszczenie-delete.html"
    success_url = reverse_lazy('baza:profile')


class ArchiwumPrzegladListView(LoginRequiredMixin, generic.ListView):

    context_object_name = 'archiwum_lista'
    template_name = "baza/archiwum-przeglad.html"

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs['przeglad_id']
        self.przeglad = PrzegladyTechniczne.objects.get(pk = pk)
        return ArchiwumPrzeglad.objects.all().filter(przeglad=self.przeglad)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['przeglad'] = self.przeglad
        return context


class ArchiwumPrzegladDetailView(LoginRequiredMixin, generic.DetailView):

    model = ArchiwumPrzeglad
    template_name = "baza/archiwum-przeglad-detail.html"


class ArchiwumPrzegladDeleteView(LoginRequiredMixin, generic.DeleteView):

    model = ArchiwumPrzeglad
    template_name = "baza/archiwum-przeglad-delete.html"
    success_url = reverse_lazy('baza:profile')


@login_required
def profile(request):
    return render(request, 'baza/profile.html')


@login_required
def edytuj_miejsce(request, miejsce_id):
    miejsce = Miejsce.objects.get(pk=miejsce_id)
    form = MiejsceForm(instance = miejsce)
    if request.method == 'POST':
        form = MiejsceForm(request.POST, instance = miejsce)
        if form.is_valid():
            if 'save' in request.POST:
                form.save()
                return HttpResponseRedirect('/dodane/')
            elif 'delete' in request.POST:
                miejsce.delete()
                return HttpResponseRedirect(reverse('baza:profile'))

        else:
            return HttpResponseRedirect('/niedodane/')



    return render(request, 'baza/edytuj_miejsce.html', {'form': form})




@login_required
def edytuj_obiekt(request, obiekt_id):
    obiekt = ObiektK.objects.get(pk=obiekt_id)
    form = ObiektKForm(instance = obiekt)
    if request.method == 'POST':
        form = ObiektKForm(request.POST, instance = obiekt)
        if form.is_valid():
            if 'save' in request.POST:
                form.save()
                return HttpResponseRedirect('/dodane/')
            elif 'delete' in request.POST:
                obiekt.delete()
                return HttpResponseRedirect(reverse('baza:profile'))

        else:
            return HttpResponseRedirect('/niedodane/')



    return render(request, 'baza/edytuj_obiekt.html', {'form': form})


@login_required
def edytuj_dopuszczenie(request, obiekt_id):
    obiekt = DopuszczeniaLegalizacje.objects.get(pk = obiekt_id)
    form = DopuszczeniaLegalizacjeForm(instance = obiekt)

    if request.method == 'POST':
        form = DopuszczeniaLegalizacjeForm(request.POST, instance = obiekt)
        if form.is_valid():
            if 'save' in request.POST:
                form.save()
                return HttpResponseRedirect('/dodane/')
            elif 'archive' in request.POST:
                dopuszczenie = obiekt
                nazwa_urzadzenia = form.cleaned_data['nazwa_urzadzenia']
                nr_urzadzenia = form.cleaned_data['nr_urzadzenia']
                opis_czynnosci = form.cleaned_data['opis_czynnosci']
                jednostka_dozorowa = form.cleaned_data['jednostka_dozorowa']
                data_ostatniej_czynnosci = form.cleaned_data['data_ostatniej_czynnosci']
                nr_decyzji = form.cleaned_data['nr_decyzji']
                data_najblizszej_czynnosci = form.cleaned_data['data_najblizszej_czynnosci']
                osoba_odpowiedzialna_za_nadzor = form.cleaned_data['osoba_odpowiedzialna_za_nadzor']
                uwagi = form.cleaned_data['uwagi']

                ArchiwumDopuszczenie.objects.create(
                    dopuszczenie = dopuszczenie,
                    nazwa_urzadzenia = nazwa_urzadzenia,
                    nr_urzadzenia = nr_urzadzenia,
                    opis_czynnosci = opis_czynnosci,
                    jednostka_dozorowa = jednostka_dozorowa,
                    data_ostatniej_czynnosci = data_ostatniej_czynnosci,
                    nr_decyzji = nr_decyzji,
                    data_najblizszej_czynnosci = data_najblizszej_czynnosci,
                    osoba_odpowiedzialna_za_nadzor = osoba_odpowiedzialna_za_nadzor,
                    uwagi = uwagi
                )

                return HttpResponseRedirect('/dodane/')
            elif 'delete' in request.POST:
                obiekt.delete()
                return HttpResponseRedirect(reverse('baza:profile'))

    return render(request, 'baza/edytuj_dopuszczenie.html', {'form': form, 'obiekt':obiekt})

@login_required
def edytuj_przeglad(request, przeglad_id):
    przeglad = PrzegladyTechniczne.objects.get(pk = przeglad_id)
    form = PrzegladyTechniczneForm(instance = przeglad)

    if request.method == 'POST':
        form = PrzegladyTechniczneForm(request.POST, instance = przeglad)
        if form.is_valid():
            if 'save' in request.POST:
                form.save()

                return HttpResponseRedirect('/dodane/')
            elif 'archive' in request.POST:
                przeglad = przeglad
                nazwa_urzadzenia = form.cleaned_data['nazwa_urzadzenia']
                nr_urzadzenia = form.cleaned_data['nr_urzadzenia']
                opis_czynnosci = form.cleaned_data['opis_czynnosci']
                jednostka_kontrolujaca = form.cleaned_data['jednostka_kontrolujaca']
                data_ostatniej_czynnosci = form.cleaned_data['data_ostatniej_czynnosci']
                nr_protokolu = form.cleaned_data['nr_protokolu']
                data_najblizszej_czynnosci = form.cleaned_data['data_najblizszej_czynnosci']
                osoba_odpowiedzialna_za_nadzor = form.cleaned_data['osoba_odpowiedzialna_za_nadzor']
                uwagi = form.cleaned_data['uwagi']

                ArchiwumPrzeglad.objects.create(
                    przeglad = przeglad,
                    nazwa_urzadzenia = nazwa_urzadzenia,
                    nr_urzadzenia = nr_urzadzenia,
                    opis_czynnosci = opis_czynnosci,
                    jednostka_kontrolujaca = jednostka_kontrolujaca,
                    data_ostatniej_czynnosci = data_ostatniej_czynnosci,
                    nr_protokolu = nr_protokolu,
                    data_najblizszej_czynnosci = data_najblizszej_czynnosci,
                    osoba_odpowiedzialna_za_nadzor = osoba_odpowiedzialna_za_nadzor,
                    uwagi = uwagi
                )

                return HttpResponseRedirect('/dodane/')
            elif 'delete' in request.POST:
                przeglad.delete()
                return HttpResponseRedirect(reverse('baza:profile'))

    return render(request, 'baza/edytuj_przeglad.html', {'form': form, 'przeglad':przeglad})





def home(request):
    return render(request, 'baza/home.html')


@login_required
def miejsce(request, miejsce_id):

    # pokaż nazwę i adres miejsca o podanym id
    miejsce = Miejsce.objects.get(pk = miejsce_id)

    # pokaż wszystkie obiektyK dla tego miejsca
    obiekty = ObiektK.objects.all().filter(miejsce = miejsce)
    obiekty = obiekty.order_by(Lower('nazwa'))
    # dodaj nowy obiektK
    # link w template do funkcji dodaj_obiektK

    return render(request, 'baza/miejsce.html', {'obiekty': obiekty, 'miejsce': miejsce})






@login_required
def obiekt(request, miejsce_id, obiekt_id):

    # pokaż nazwę i adres miejsca o podanym id
    miejsce = Miejsce.objects.get(pk = miejsce_id)

    # pokaż dane obiektu o podanym id
    obiekt = ObiektK.objects.get(pk = obiekt_id)

    # pokaż wszystkie dopuszczenia
    dopuszczenia = DopuszczeniaLegalizacje.objects.all().filter(obiektk = obiekt)

    # pokaż wszystkie przeglady
    przeglady = PrzegladyTechniczne.objects.all().filter(obiektk = obiekt)


    return render(request, 'baza/obiekt.html', {
        'miejsce': miejsce,
        'obiekt': obiekt,
        'dopuszczenia': dopuszczenia,
        'przeglady': przeglady})



@login_required
def dodaj_miejsce(request):
    if request.method == 'POST':
        form = MiejsceForm(request.POST)
        username = request.user.username

        if form.is_valid():

            typ = form.cleaned_data['typ']
            nazwa = form.cleaned_data['nazwa']
            adres = form.cleaned_data['adres']
            telefon = form.cleaned_data['telefon']
            created_by = username
            Miejsce.objects.create(
                typ = typ,
                nazwa = nazwa,
                adres = adres,
                telefon = telefon,
                created_by = created_by)

            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/niedodane/')

    else:
        form = MiejsceForm()

    return render(request, 'baza/dodaj_miejsce.html', {'form': form})

class DodajObiektWyborOpcjiTemplateView(generic.TemplateView):
    template_name = 'baza/dodaj-obiekt-wybor-opcji.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        miejsce_id = self.kwargs['miejsce_id']
        miejsce = Miejsce.objects.get(pk = miejsce_id)
        context['miejsce'] = miejsce
        return context

class DodajObiektGotowyCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ObiektKForm
    model = ObiektK
    success_url = '/dodane/'
    template_name = "baza/dodaj-obiekt-initial.html"
    initial = {

        'nazwa': 'agregat proszkowy typ TEX 25 l nr 550/1998 nr doz. N2329002015',
        'dane_techniczne': 'prod. Grodków typ. TEX 25 L'
    }

    def form_valid(self, form):
        miejsce_id = self.kwargs['miejsce_id']
        miejsce = Miejsce.objects.get(pk = miejsce_id)
        form.instance.miejsce = miejsce
        self.object = form.save()
        now = datetime.datetime.now()
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = self.object.nazwa,
            nr_urzadzenia = 'nr',
            opis_czynnosci = 'rewizja wewnetrzna',
            jednostka_dozorowa = 'UDT',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'b/d',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Rafał Tyrka',
            uwagi = 'brak'
        )
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = self.object.nazwa,
            nr_urzadzenia = '550',
            opis_czynnosci = 'próba ciśnieniowa',
            jednostka_dozorowa = 'UDT',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'b/d',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Rafał Tyrka',
            uwagi = 'brak'
        )
        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = self.object.nazwa,
            nr_urzadzenia = '550',
            opis_czynnosci = 'okresowy przegląd agregatu',
            jednostka_kontrolujaca = 'Best Sp. Jawna',
            data_ostatniej_czynnosci = now,
            nr_protokolu = '43/2017',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Rafał Tyrka',
            uwagi = 'brak'
        )

        return super().form_valid(form)


class DodajOdmierzaczCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ObiektKForm
    model = ObiektK
    success_url = '/dodane/'
    template_name = "baza/dodaj-obiekt-initial.html"
    initial = {

        'nazwa': 'Odmierzacz paliw serii HELIX 6000 model C(NH/LM) 33-33, RV2 nr',
        'dane_techniczne': 'Odmierzacz paliw serii HELIX 6000 model C(NH/LM) 33-33, RV2,  prod.  Wayne Dresser  rok prod. 2018 trzyproduktowy   (dwie benzyny oraz ON ) sześciowężowy (2 węże ON, 2 węże Pb95, 2 węże Pb 98); o wydajności 40 dm3/min,'
    }

    def form_valid(self, form):
        miejsce_id = self.kwargs['miejsce_id']
        miejsce = Miejsce.objects.get(pk = miejsce_id)
        form.instance.miejsce = miejsce
        self.object = form.save()
        now = datetime.datetime.now()
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Czujnik objętości cieczy',
            nr_urzadzenia = 'x',
            opis_czynnosci = 'Legalizacja ponowna',
            jednostka_dozorowa = 'OUM w Zielonej Górze',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'Świadectwo Legalizacji ponownej znak wniosku:  WZ4.400.864.18.2018',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Czujnik objętości cieczy',
            nr_urzadzenia = 'x',
            opis_czynnosci = 'Legalizacja ponowna',
            jednostka_dozorowa = 'OUM w Zielonej Górze',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'Świadectwo Legalizacji ponownej znak wniosku:  WZ4.400.864.18.2018',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Czujnik objętości cieczy',
            nr_urzadzenia = 'x',
            opis_czynnosci = 'Legalizacja ponowna',
            jednostka_dozorowa = 'OUM w Zielonej Górze',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'Świadectwo Legalizacji ponownej znak wniosku:  WZ4.400.864.18.2018',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Czujnik objętości cieczy',
            nr_urzadzenia = 'x',
            opis_czynnosci = 'Legalizacja ponowna',
            jednostka_dozorowa = 'OUM w Zielonej Górze',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'Świadectwo Legalizacji ponownej znak wniosku:  WZ4.400.864.18.2018',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Czujnik objętości cieczy',
            nr_urzadzenia = 'x',
            opis_czynnosci = 'Legalizacja ponowna',
            jednostka_dozorowa = 'OUM w Zielonej Górze',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'Świadectwo Legalizacji ponownej znak wniosku:  WZ4.400.864.18.2018',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Czujnik objętości cieczy',
            nr_urzadzenia = 'x',
            opis_czynnosci = 'Legalizacja ponowna',
            jednostka_dozorowa = 'OUM w Zielonej Górze',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'Świadectwo Legalizacji ponownej znak wniosku:  WZ4.400.864.18.2018',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Czujnik objętości cieczy',
            nr_urzadzenia = 'x',
            opis_czynnosci = 'Legalizacja ponowna',
            jednostka_dozorowa = 'OUM w Zielonej Górze',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'Świadectwo Legalizacji ponownej znak wniosku:  WZ4.400.864.18.2018',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Czujnik objętości cieczy',
            nr_urzadzenia = 'x',
            opis_czynnosci = 'Legalizacja ponowna',
            jednostka_dozorowa = 'OUM w Zielonej Górze',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'Świadectwo Legalizacji ponownej znak wniosku:  WZ4.400.864.18.2018',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Odmierzacz paliw typ Helix 6000 model C(NH/LM)33-33 nr',
            nr_urzadzenia = '...',
            opis_czynnosci = 'Przegląd stanu technicznego odmierzacza',
            jednostka_kontrolujaca = 'Grzegorz Staszak',
            data_ostatniej_czynnosci = now,
            nr_protokolu = 'x',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Odmierzacz paliw typ Helix 6000 model C(NH/LM)33-33 nr',
            nr_urzadzenia = '...',
            opis_czynnosci = 'badanie VRS',
            jednostka_kontrolujaca = 'GST Grzegorz Staszak',
            data_ostatniej_czynnosci = now,
            nr_protokolu = 'x',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Odmierzacz paliw typ Helix 6000 model C(NH/LM)33-33 nr',
            nr_urzadzenia = '...',
            opis_czynnosci = 'Pomiary instalacji elektrycznej, odgromowej oraz badania oporności węży',
            jednostka_kontrolujaca = 'Baza Paliw Sp. z o.o.',
            data_ostatniej_czynnosci = now,
            nr_protokolu = 'x',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Mirosław Guldziński',
            uwagi = 'brak'
        )

        return super().form_valid(form)


class DodajPawilonCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ObiektKForm
    model = ObiektK
    success_url = '/dodane/'
    template_name = "baza/dodaj-obiekt-initial.html"
    initial = {

        'nazwa': 'Pawilon TRIP FREE',
        'dane_techniczne': 'brak'
    }

    def form_valid(self, form):
        miejsce_id = self.kwargs['miejsce_id']
        miejsce = Miejsce.objects.get(pk = miejsce_id)
        form.instance.miejsce = miejsce
        self.object = form.save()
        now = datetime.datetime.now()

        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'instalacja wentylacji grawitacyjnej',
            nr_urzadzenia = 'brak',
            opis_czynnosci = 'okresowa kontrola stanu przewodów wentylacyjnych',
            jednostka_kontrolujaca = 'Zakład kominiarski Bogusław Szymkiewicz',
            data_ostatniej_czynnosci = now,
            nr_protokolu = '63/10/17',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Rafał Tyrka',
            uwagi = 'brak'
        )

        return super().form_valid(form)


class DodajZbiornikCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ObiektKForm
    model = ObiektK
    success_url = '/dodane/'
    template_name = "baza/dodaj-obiekt-initial.html"
    initial = {

        'nazwa': 'Zbiornik magazynowy ZP- 50 nr fabr. .....',
        'dane_techniczne': 'Zbiornik dwupłaszczowy poj. 50 m3, dwukomorowy (25 m3 Pb 98, 25 m3 ON) prod. Metalchem Kościan nr fabr. 98015 nr ew. N2726000097 rok budowy 1998. Zbiornik wyposażony w przerywacze płomieni PPK-50 prod. Limet o nr 25,26/1994, Zawory oddechowe EKO ZO-50 prod. LIMET nr 21,22/1994. Przestrzeń między płaszczowa monitorowana detektorem wycieku LAG-14 ER prod. Afriso. System kontrolno pomiarowy SITE SENTINEL 2'
    }

    def form_valid(self, form):
        miejsce_id = self.kwargs['miejsce_id']
        miejsce = Miejsce.objects.get(pk = miejsce_id)
        form.instance.miejsce = miejsce
        self.object = form.save()
        now = datetime.datetime.now()
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = self.object.nazwa,
            nr_urzadzenia = 'nr',
            opis_czynnosci = 'rewizja wewnetrzna',
            jednostka_dozorowa = 'UDT',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'b/d',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        DopuszczeniaLegalizacje.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = self.object.nazwa,
            nr_urzadzenia = '...',
            opis_czynnosci = 'prewizja zewnetrzna',
            jednostka_dozorowa = 'UDT',
            data_ostatniej_czynnosci = now,
            nr_decyzji = 'b/d',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'płaszcz zbiornika',
            nr_urzadzenia = '...',
            opis_czynnosci = 'oględziny i pomiary instalacji elektrycznej',
            jednostka_kontrolujaca = 'UE Benedykt Brenk',
            data_ostatniej_czynnosci = now,
            nr_protokolu = 'b/d',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Zdzisław Kaczorowski',
            uwagi = 'obejmują oględziny puszek, połączeń ekwipotencjalnych, zadławień przewodów'
        )
        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'System pomiarowy Site Sentinel system pomiarowy tzw. mokry',
            nr_urzadzenia = 'b/d',
            opis_czynnosci = 'okresowa kontrola stanu technicznego urzadzenia',
            jednostka_kontrolujaca = 'Petromarketing Sp. z o.o. tel. 601 533 997',
            data_ostatniej_czynnosci = now,
            nr_protokolu = 'b/d',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'Zawór oddechowy EKO ZO 50',
            nr_urzadzenia = '...',
            opis_czynnosci = 'przegląd techniczny',
            jednostka_kontrolujaca = 'Grzegorz Staszak',
            data_ostatniej_czynnosci = now,
            nr_protokolu = 'b/d',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'przerywacz płowmienia PPK-50',
            nr_urzadzenia = '...',
            opis_czynnosci = 'przegląd techniczny urzadzenia',
            jednostka_kontrolujaca = 'Grzegorz Staszak',
            data_ostatniej_czynnosci = now,
            nr_protokolu = 'b/d',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )
        PrzegladyTechniczne.objects.create(
            obiektk = self.object,
            nazwa_urzadzenia = 'przyłacze oparów UNIMAT',
            nr_urzadzenia = '...',
            opis_czynnosci = 'przegląd techniczny urzadzenia',
            jednostka_kontrolujaca = 'Grzegorz Staszak',
            data_ostatniej_czynnosci = now,
            nr_protokolu = 'b/d',
            data_najblizszej_czynnosci = now,
            osoba_odpowiedzialna_za_nadzor = 'Grzegorz Staszak',
            uwagi = 'brak'
        )

        return super().form_valid(form)



@login_required
def dodaj_obiekt(request, miejsce_id):
    if request.method == 'POST':
        form = ObiektKForm(request.POST)
        if form.is_valid():
            miejsce = Miejsce.objects.get(pk = miejsce_id)
            nazwa = form.cleaned_data['nazwa']
            dane_techniczne = form.cleaned_data['dane_techniczne']
            ObiektK.objects.create(
                miejsce = miejsce,
                nazwa = nazwa,
                dane_techniczne = dane_techniczne)
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/niedodane/')

    else:
        form = ObiektKForm()
    return render(request, 'baza/dodaj_obiekt.html', {'form': form})

@login_required
def dodaj_dopuszczenie(request, miejsce_id, obiekt_id):
    if request.method == 'POST':
        form = DopuszczeniaLegalizacjeForm(request.POST)
        if form.is_valid():
            obiektk = ObiektK.objects.get(pk = obiekt_id)
            nazwa_urzadzenia = form.cleaned_data['nazwa_urzadzenia']
            nr_urzadzenia = form.cleaned_data['nr_urzadzenia']
            opis_czynnosci = form.cleaned_data['opis_czynnosci']
            jednostka_dozorowa = form.cleaned_data['jednostka_dozorowa']
            data_ostatniej_czynnosci = form.cleaned_data['data_ostatniej_czynnosci']
            nr_decyzji = form.cleaned_data['nr_decyzji']
            data_najblizszej_czynnosci = form.cleaned_data['data_najblizszej_czynnosci']
            osoba_odpowiedzialna_za_nadzor = form.cleaned_data['osoba_odpowiedzialna_za_nadzor']
            uwagi = form.cleaned_data['uwagi']

            DopuszczeniaLegalizacje.objects.create(
                obiektk = obiektk,
                nazwa_urzadzenia = nazwa_urzadzenia,
                nr_urzadzenia = nr_urzadzenia,
                opis_czynnosci = opis_czynnosci,
                jednostka_dozorowa = jednostka_dozorowa,
                data_ostatniej_czynnosci = data_ostatniej_czynnosci,
                nr_decyzji = nr_decyzji,
                data_najblizszej_czynnosci = data_najblizszej_czynnosci,
                osoba_odpowiedzialna_za_nadzor = osoba_odpowiedzialna_za_nadzor,
                uwagi = uwagi)
            return HttpResponseRedirect('/dodane/')
     #   else:
      #      return HttpResponseRedirect('/niedodane/')

    else:
        form = DopuszczeniaLegalizacjeForm()
    return render(request, 'baza/dodaj_dopuszczenia.html', {'form': form})

def dodaj_przeglad(request, miejsce_id, obiekt_id):
    if request.method == 'POST':
        form = PrzegladyTechniczneForm(request.POST)
        if form.is_valid():
            obiektk = ObiektK.objects.get(pk = obiekt_id)
            nazwa_urzadzenia = form.cleaned_data['nazwa_urzadzenia']
            nr_urzadzenia = form.cleaned_data['nr_urzadzenia']
            opis_czynnosci = form.cleaned_data['opis_czynnosci']
            jednostka_kontrolujaca = form.cleaned_data['jednostka_kontrolujaca']
            data_ostatniej_czynnosci = form.cleaned_data['data_ostatniej_czynnosci']
            nr_protokolu = form.cleaned_data['nr_protokolu']
            data_najblizszej_czynnosci = form.cleaned_data['data_najblizszej_czynnosci']
            osoba_odpowiedzialna_za_nadzor = form.cleaned_data['osoba_odpowiedzialna_za_nadzor']
            uwagi = form.cleaned_data['uwagi']

            PrzegladyTechniczne.objects.create(
                obiektk = obiektk,
                nazwa_urzadzenia = nazwa_urzadzenia,
                nr_urzadzenia = nr_urzadzenia,
                opis_czynnosci = opis_czynnosci,
                jednostka_kontrolujaca = jednostka_kontrolujaca,
                data_ostatniej_czynnosci = data_ostatniej_czynnosci,
                nr_protokolu = nr_protokolu,
                data_najblizszej_czynnosci = data_najblizszej_czynnosci,
                osoba_odpowiedzialna_za_nadzor = osoba_odpowiedzialna_za_nadzor,
                uwagi = uwagi)
            return HttpResponseRedirect('/dodane/')
     #   else:
      #      return HttpResponseRedirect('/niedodane/')

    else:
        form = PrzegladyTechniczneForm()
    return render(request, 'baza/dodaj_przeglad.html', {'form': form})










#  ponizej stare views -------------------------------------------


def dodajobiekt(request):
    if request.method == 'POST':
        form = ObiektForm(request.POST)

        if form.is_valid():

            typ = form.cleaned_data['typ']
            nazwa = form.cleaned_data['nazwa']
            lokalizacja = form.cleaned_data['lokalizacja']
            numer = form.cleaned_data['nr']
            wytyczne = form.cleaned_data['wytyczne']
            obiekt = Obiekt.objects.create(
                typ=typ,
                nazwa=nazwa,
                lokalizacja=lokalizacja,
                nr=numer,
                wytyczne=wytyczne)
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/')

    else:
        form = ObiektForm()

    return render(request, 'baza/dodajobiekt.html', {'form': form})





def dodaj_urzadzenie(request):
    if request.method == 'POST':
        form = SzukajObiektForm(request.POST)

        if form.is_valid():

            typ = form.cleaned_data['typ']
            obiekty = Obiekt.objects.all().filter(typ=typ)

            return render(request, 'baza/okresl_stacje_dla_urzadzenia.html', {'obiekty': obiekty})
        else:
            return HttpResponseRedirect('/')

    form = SzukajObiektForm()
    return render(request, 'baza/wybierz_stacje_dla_urzadzenia.html', {'form': form})




def dodajurzadzenie(request):
    if request.method == 'POST':
        form = SzukajObiektForm(request.POST)

        if form.is_valid():

            typ = form.cleaned_data['typ']
            obiekty = Obiekt.objects.all().filter(typ=typ)

            return render(request, 'baza/okreslobiekt.html', {'obiekty': obiekty})
        else:
            return HttpResponseRedirect('/')

    form = SzukajObiektForm()
    return render(request, 'baza/dobierzobiekt.html', {'form':form})

def dodane(request):
    return render(request, 'baza/dodane.html')

def usuniete(request):
    return render(request, 'baza/usuniete.html')

def niedodane(request):
    return render(request, 'baza/niedodane.html')





def rafal(request):
    return render(request, 'baza/rafal.html')






def signin(request):
    return render(request, 'baza/signin.html')

def szukajobiekt(request):
    if request.method == 'POST':
        form = SzukajObiektForm(request.POST)

        if form.is_valid():

            typ = form.cleaned_data['typ']
            obiekty = Obiekt.objects.all().filter(typ=typ)

            return render(request, 'baza/wybierzobiekt.html', {'obiekty': obiekty})
        else:
            return HttpResponseRedirect('/')


    else:
        form = SzukajObiektForm()
    return render(request, 'baza/szukajobiekt.html', {'form':form})

def dodaj_stacje(request):
    if request.method == 'POST':
        form = ObiektForm(request.POST)

        if form.is_valid():

            typ = form.cleaned_data['typ']
            nazwa = form.cleaned_data['nazwa']
            lokalizacja = form.cleaned_data['lokalizacja']
            numer = form.cleaned_data['nr']
            wytyczne = form.cleaned_data['wytyczne']
            obiekt = Obiekt.objects.create(
                typ=typ,
                nazwa=nazwa,
                lokalizacja=lokalizacja,
                nr=numer,
                wytyczne=wytyczne)
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/niedodane/')

    else:
        form = ObiektForm()

    return render(request, 'baza/dodaj_stacje.html', {'form': form})





def dodaj_okt(request, stacja_id):
    stacja = Obiekt.objects.get(pk=stacja_id)
    nazwa_stacji = stacja.nazwa
    if request.method == 'POST':
        form = UrzadzenieForm(request.POST)
        if form.is_valid():
            obiekt = stacja
            nazwa = form.cleaned_data['nazwa']
            lokalizacja = form.cleaned_data['lokalizacja']
            numer = form.cleaned_data['nr']
            wytyczne = form.cleaned_data['wytyczne']
            urzadzenie = Urzadzenie.objects.create(
                obiekt=obiekt,
                nazwa=nazwa,
                lokalizacja=lokalizacja,
                nr=numer,
                wytyczne=wytyczne)
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/niedodane/')
    else:
        form = UrzadzenieForm()
    return render(request, 'baza/dodaj_obiekt.html', {'nazwa_stacji': nazwa_stacji, 'form': form})




def szukaj(request):
    # pobrać z bazy wszystkie stacje
    stacje = Obiekt.objects.all().filter(typ='stacja')

    # przekazać wszystkie pobrane stacje do renderowania
    return render(request, 'baza/szukaj.html', {'obiekty': stacje})






def stacja (request, stacja_id):
    stacja = Obiekt.objects.get(pk=stacja_id)
    form = StacjaForm(instance=stacja)
    obiekty = Urzadzenie.objects.all().filter(obiekt=stacja)
    if request.method == 'POST':
        form = StacjaForm(request.POST, instance=stacja)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/niedodane/')

    return render(request, 'baza/stacja.html', {'stacja': stacja, 'form': form, 'obiekty': obiekty})

def obit(request, stacja_id, obiekt_id):
    stacja = Obiekt.objects.get(pk=stacja_id)
    obiekt = Urzadzenie.objects.get(pk=obiekt_id)
    form = UrzadzenieForm(instance=obiekt)
    urzadzenia = Przedmiot.objects.all().filter(urzadzenie=obiekt)

    if request.method =='POST':
        form = UrzadzenieForm(request.POST, instance=obiekt)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/niedodane/')

    return render(request, 'baza/obiekt.html', {'stacja': stacja, 'obiekt': obiekt, 'form': form, 'urzadzenia': urzadzenia})

def urzadzenie(request, stacja_id, obiekt_id, urzadzenie_id):
    stacja = Obiekt.objects.get(pk=stacja_id)
    obiekt = Urzadzenie.objects.get(pk=obiekt_id)
    urzadzenie = Przedmiot.objects.get(pk=urzadzenie_id)
    form = PrzedmiotForm(instance=urzadzenie)

    if request.method =='POST':
        form = PrzedmiotForm(request.POST, instance=urzadzenie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/niedodane/')

    return render(request, 'baza/urzadzenie.html', {'stacja': stacja, 'obiekt': obiekt, 'form': form})



def szukajurzadzenie(request):
    if request.method == 'POST':
        form = SzukajObiektForm(request.POST)

        if form.is_valid():

            typ = form.cleaned_data['typ']
            obiekty = Obiekt.objects.all().filter(typ=typ)

            return render(request, 'baza/wybierzobiekt-urzadzenie.html', {'obiekty': obiekty})
        else:
            return HttpResponseRedirect('/')


    else:
        form = SzukajObiektForm()

    return render(request, 'baza/szukajobiekt-urzadzenie.html', {'form':form})


def urzadzenie_dla_obiektu(request, obiekt_id):
    obiekt = Urzadzenie.objects.get(pk=obiekt_id)
    return render(request, 'baza/wybrana_stacja_dla_urzadzenia.html')

def wybrana_stacja_dla_urzadzenia(request, obiekt_id):
    stacja = Obiekt.objects.get(pk=obiekt_id)
    obiekty = Urzadzenie.objects.all().filter(obiekt=stacja)
    return render(request, 'baza/wybrana_stacja_dla_urzadzenia.html', {'stacja': stacja, 'obiekty': obiekty})


def wybrany_obiekt_dla_urzadzenia(request, stacja_id, obiekt_id):

    # zwrócić nazwę stacji
    stacja = Obiekt.objects.get(pk=stacja_id)
    nazwa_stacji = stacja.nazwa

    # zwrócić nazwę obiektu
    obiekt = Urzadzenie.objects.get(pk=obiekt_id)
    nazwa_obiektu = obiekt.nazwa

    if request.method == 'POST':
        form = PrzedmiotForm(request.POST)
        if form.is_valid():
            urzadzenie = obiekt
            nazwa = form.cleaned_data['nazwa']
            lokalizacja = form.cleaned_data['lokalizacja']
            numer = form.cleaned_data['nr']
            wytyczne = form.cleaned_data['wytyczne']
            przedmiot = Przedmiot.objects.create(
                urzadzenie=urzadzenie,
                nazwa=nazwa,
                lokalizacja=lokalizacja,
                nr=numer,
                wytyczne=wytyczne)
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/')

    else:


    # wyświetlić formularz do wpisania danych urządzenia
        form = PrzedmiotForm()


    return render(request, 'baza/urzadzenie.html',
        {
        'stacja': nazwa_stacji,
        'obiekt' : nazwa_obiektu,
        'form': form
        })



def wybranyobiekt(request, obiekt_id):
    obiekt = Obiekt.objects.get(pk=obiekt_id)
    nazwa_obiektu = obiekt.nazwa
    adres_obiektu = obiekt.lokalizacja
    if request.method == 'POST':
        form = UrzadzenieForm(request.POST)

        if form.is_valid():

            obiekt = obiekt
            nazwa = form.cleaned_data['nazwa']
            lokalizacja = form.cleaned_data['lokalizacja']
            numer = form.cleaned_data['nr']
            wytyczne = form.cleaned_data['wytyczne']
            urzadzenie = Urzadzenie.objects.create(
                obiekt=obiekt,
                nazwa=nazwa,
                lokalizacja=lokalizacja,
                nr=numer,
                wytyczne=wytyczne)
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/')

    else:
        form = UrzadzenieForm()



    return render(request, 'baza/dodajurzadzenie.html',
        {
        'obiekt': nazwa_obiektu,
        'adres': adres_obiektu,
        'form': form})





def znalezionyobiekt(request, obiekt_id):
    obiekt = Obiekt.objects.get(pk=obiekt_id)
    form = ObiektForm(instance=obiekt)
    if request.method =='POST':
        form = ObiektForm(request.POST, instance=obiekt)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/niedodane/')



    # obiekt = get_object_or_404(Obiekt, pk=obiekt_id)

    return render(request, 'baza/znalezionyobiekt.html', {'form': form})
#    return render(request, 'baza/znalezionyobiekt.html', {'obiekt': obiekt})

def znalezioneurzadzenie(request, urzadzenie_id):
    urzadzenie = Urzadzenie.objects.get(pk=urzadzenie_id)
    form = UrzadzenieForm(instance=urzadzenie)

    if request.method == 'POST':
        form = UrzadzenieForm(request.POST, instance=urzadzenie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodane/')
        else:
            return HttpResponseRedirect('/niedodane/')

    return render(request, 'baza/znalezioneurzadzenie.html', {'form': form})


def obiektdlaurzadzenia(request, obiekt_id):

    obiekt = Obiekt.objects.get(pk=obiekt_id)
    urzadzenia = Urzadzenie.objects.all().filter(obiekt = obiekt)


    return render(request, 'baza/obiektdlaurzadzenia.html',
            {
                'obiekt': obiekt,
                'urzadzenia': urzadzenia
                })

