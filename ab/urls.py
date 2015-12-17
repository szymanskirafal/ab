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

import baza.views
import grupa.views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', baza.views.home, name='home'),
    url(r'^accounts/profile/$', baza.views.profile, name='profile'),
    url(r'^dodaj/miejsce/$', baza.views.dodaj_miejsce, name='dodaj_miejsce'),
    url(r'^dodaj/obiekt/(?P<miejsce_id>[0-9]+)/$', baza.views.dodaj_obiekt, name='dodaj_obiekt'),
    url(r'^dodaj/dopuszczenie/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', baza.views.dodaj_dopuszczenie, name='dodaj_dopuszczenie'),
    url(r'^dodaj/przeglad/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', baza.views.dodaj_przeglad, name='dodaj_przeglad'),
    url(r'^edytuj/obiekt/(?P<obiekt_id>[0-9]+)/$', baza.views.edytuj_obiekt, name="edytuj_obiekt"),
    url(r'^edytuj/dopuszczenie(?P<obiekt_id>[0-9]+)/$', baza.views.edytuj_dopuszczenie, name="edytuj_dopuszczenie"),
    url(r'^edytuj/przeglad(?P<obiekt_id>[0-9]+)/$', baza.views.edytuj_przeglad, name="edytuj_przeglad"),
    url(r'^grupy/$', grupa.views.grupy, name='grupy'),
    url(r'^grupa/nowa/$', grupa.views.nowa, name='nowa'),
    url(r'^grupa/dodaj/(?P<group_name>[A-Za-z0-9 _]+)/$', grupa.views.add_new_member, name='add_new_member'),
    url(r'^grupa/group/(?P<group_name>[A-Za-z0-9 _]+)/$', grupa.views.group, name='group'),
    url(r'^miejsca/(?P<miejsca>[a-z]+)/$', baza.views.miejsca, name='miejsca'),
    url(r'^miejsce/(?P<miejsce_id>[0-9]+)/$', baza.views.miejsce, name='miejsce'),
    url(r'^obiekt/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', baza.views.obiekt, name='obiekt'),
    url(r'^niedodane/$', baza.views.niedodane, name='niedodane'),
    url(r'dodane/$', baza.views.dodane, name='dodane'),


]
