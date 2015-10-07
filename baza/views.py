from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .forms import ObiektForm, SzukajObiektForm
from .models import Obiekt


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


def dodane(request):
    return render(request, 'baza/dodane.html')


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
           # lista_obiektow = []
           # for obiekt in obiekty:
           #     lista_obiektow.append(obiekt.nazwa)
           #     return lista_obiektow
             
            return render(request, 'baza/wybierzobiekt.html', {'obiekty': obiekty})
        else:
            return HttpResponseRedirect('/')


    
          #    return HttpRequestRedirect('/znaleziony/')
  #  else:
    form = SzukajObiektForm()
    return render(request, 'baza/szukajobiekt.html', {'form':form})

def znalezionyobiekt(request, obiekt_id):

    obiekt = get_object_or_404(Obiekt, pk=obiekt_id)
    return render(request, 'baza/znalezionyobiekt.html', {'obiekt': obiekt})
