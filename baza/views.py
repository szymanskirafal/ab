from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

from .forms import MiejsceForm, ObiektKForm, DopuszczeniaLegalizacjeForm, PrzegladyTechniczneForm, ObiektForm, StacjaForm, SzukajObiektForm, UrzadzenieForm, PrzedmiotForm
from .models import Miejsce, ObiektK, DopuszczeniaLegalizacje, PrzegladyTechniczne, Obiekt, Urzadzenie, Przedmiot

# from grupa.models import CustomGroup


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
            elif 'delete' in request.POST:
                obiekt.delete()
                return HttpResponseRedirect(reverse('baza:profile'))

    return render(request, 'baza/edytuj_dopuszczenie.html', {'form': form})

@login_required
def edytuj_przeglad(request, obiekt_id):
    obiekt = PrzegladyTechniczne.objects.get(pk = obiekt_id)
    form = PrzegladyTechniczneForm(instance = obiekt)

    if request.method == 'POST':
        form = PrzegladyTechniczneForm(request.POST, instance = obiekt)
        if form.is_valid():
            if 'save' in request.POST:
                form.save()
                return HttpResponseRedirect('/dodane/')
            elif 'delete' in request.POST:
                obiekt.delete()

                return HttpResponseRedirect(reverse('baza:profile'))

    return render(request, 'baza/edytuj_przeglad.html', {'form': form})





def home(request):
    return render(request, 'baza/home.html')


@login_required
def miejsca(request, miejsca):

    if miejsca == 'magazyn':
        typ_miejsca = 'Magazyn paliw'
    elif miejsca == 'stacja':
        typ_miejsca = 'Stacja paliw'
    else:
        typ_miejsca = 'Budynek'

    # check if user belongs to some group
    user = request.user
    user_groups = user.groups.all()

    # check all members of these groups

    all_members = []
    for group in user_groups:
        for member in group.user_set.all():
            all_members.append(member.username)

    # find objects created by these members



    miejsca = Miejsce.objects.all().filter(typ=miejsca).filter(created_by__in = all_members)


    return render(request, 'baza/miejsca.html',
        {
            'typ_miejsca': typ_miejsca,
            'miejsca': miejsca,

            })





@login_required
def miejsce(request, miejsce_id):

    # pokaż nazwę i adres miejsca o podanym id
    miejsce = Miejsce.objects.get(pk = miejsce_id)

    # pokaż wszystkie obiektyK dla tego miejsca
    obiekty = ObiektK.objects.all().filter(miejsce = miejsce)

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

