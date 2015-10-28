from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .forms import ObiektForm, SzukajObiektForm, UrzadzenieForm, PrzedmiotForm
from .models import Obiekt, Urzadzenie, Przedmiot


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

#def dobierzobiekt(request):

    
 #   return render(request, 'baza/dobierzobiekt.html', {'form': form})




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


def profile(request):
    return render(request, 'baza/profile.html')


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

