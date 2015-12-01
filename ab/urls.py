"""ab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from baza import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^dodaj/miejsce/$', views.dodaj_miejsce, name='dodaj_miejsce'),
    url(r'^dodaj/obiekt/(?P<miejsce_id>[0-9]+)/$', views.dodaj_obiekt, name='dodaj_obiekt'),
    url(r'^dodaj/dopuszczenie/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.dodaj_dopuszczenie, name='dodaj_dopuszczenie'),
    url(r'^dodaj/przeglad/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.dodaj_przeglad, name='dodaj_przeglad'),
    url(r'^edytuj/obiekt/(?P<obiekt_id>[0-9]+)/$', views.edytuj_obiekt, name="edytuj_obiekt"),
    url(r'^edytuj/dopuszczenie(?P<obiekt_id>[0-9]+)/$', views.edytuj_dopuszczenie, name="edytuj_dopuszczenie"),
    url(r'^edytuj/przeglad(?P<obiekt_id>[0-9]+)/$', views.edytuj_przeglad, name="edytuj_przeglad"),
    url(r'^miejsca/(?P<miejsca>[a-z]+)/$', views.miejsca, name='miejsca'),
    url(r'^miejsce/(?P<miejsce_id>[0-9]+)/$', views.miejsce, name='miejsce'),
    url(r'^obiekt/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.obiekt, name='obiekt'),
    url(r'^niedodane/$', views.niedodane, name='niedodane'),


    # poniżej stare urls


    url(r'dodajobiekt/$', views.dodajobiekt, name='dodajobiekt'),
    url(r'dodajurzadzenie/$', views.dodajurzadzenie, name='dodajurzadzenie'),
    url(r'dodaj/urzadzenie/$', views.dodaj_urzadzenie, name='dodaj_urzadzenie'),
    url(r'dodaj/urzadzenie/dostacji/(?P<obiekt_id>[0-9]+)/$', views.wybrana_stacja_dla_urzadzenia, name='wybrana_stacja_dla_urzadzenia'),
    url(r'dodaj/urzadzenie/dostacji/doobiektu/(?P<stacja_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.wybrany_obiekt_dla_urzadzenia, name='wybrany_obiekt_dla_urzadzenia'),
    url(r'doobiektu/$', views.wybrany_obiekt_dla_urzadzenia, name='wybrany_obiekt_dla_urzadzenia'),
    url(r'dodane/$', views.dodane, name='dodane'),
    url(r'^obiektdlaurzadzenia/(?P<obiekt_id>[0-9]+)/$', views.obiektdlaurzadzenia, name='obiektdlaurzadzenia'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^szukajobiekt/$', views.szukajobiekt, name='szukajobiekt'),
    url(r'szukajurzadzenie/$', views.szukajurzadzenie, name='szukajurzadzenie'),
    url(r'szukaj/urzadzenie/$', views.szukajurzadzenie, name='szukajurzadzenie'),
    url(r'profile/dodaje/stacje/$', views.dodaj_stacje, name='dodaj_stacje'),
    url(r'profile/szukaj/$', views.szukaj, name='szukaj'),

    url(r'profile/szukaj/stacja/(?P<stacja_id>[0-9]+)/$', views.stacja, name='stacja'),
    url(r'profile/szukaj/stacja/obiekt/urzadzenie/(?P<stacja_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/(?P<urzadzenie_id>[0-9]+)$', views.urzadzenie, name='urzadzenie'),

    url(r'^wybranyobiekt/(?P<obiekt_id>[0-9]+)/$', views.wybranyobiekt, name='wybranyobiekt'),
    url(r'^znalezionyobiekt/(?P<obiekt_id>[0-9]+)/$', views.znalezionyobiekt, name='znalezionyobiekt'),
    url(r'^znalezioneurzadzenie/(?P<urzadzenie_id>[0-9]+)/$', views.znalezioneurzadzenie, name='znalezioneurzadzenie'),

    url(r'^rafal/$', views.rafal, name='rafal'),
]
