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
    url(r'^profile/$', views.profile, name='profile'),    
    url(r'dodajobiekt/$', views.dodajobiekt, name='dodajobiekt'),
    url(r'dodajurzadzenie/$', views.dodajurzadzenie, name='dodajurzadzenie'),
    url(r'dodaj/urzadzenie/$', views.dodaj_urzadzenie, name='dodaj_urzadzenie'),
    url(r'dodaj/urzadzenie/dostacji/(?P<obiekt_id>[0-9]+)/$', views.wybrana_stacja_dla_urzadzenia, name='wybrana_stacja_dla_urzadzenia'),
    url(r'doobiektu/$', views.wybrany_obiekt_dla_urzadzenia, name='wybrany_obiekt_dla_urzadzenia'),
    url(r'dodane/$', views.dodane, name='dodane'),
    url(r'niedodane/$', views.niedodane, name='niedodane'),
    url(r'^obiektdlaurzadzenia/(?P<obiekt_id>[0-9]+)/$', views.obiektdlaurzadzenia, name='obiektdlaurzadzenia'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^szukajobiekt/$', views.szukajobiekt, name='szukajobiekt'),
    url(r'szukajurzadzenie/$', views.szukajurzadzenie, name='szukajurzadzenie'),
    url(r'^wybranyobiekt/(?P<obiekt_id>[0-9]+)/$', views.wybranyobiekt, name='wybranyobiekt'),
    url(r'^znalezionyobiekt/(?P<obiekt_id>[0-9]+)/$', views.znalezionyobiekt, name='znalezionyobiekt'),
    url(r'^znalezioneurzadzenie/(?P<urzadzenie_id>[0-9]+)/$', views.znalezioneurzadzenie, name='znalezioneurzadzenie'),

    url(r'^rafal/$', views.rafal, name='rafal'),
]
