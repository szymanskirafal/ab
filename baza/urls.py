from django.conf.urls import url


from baza import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^dodaj/miejsce/$', views.dodaj_miejsce, name='dodaj_miejsce'),
    url(r'^dodaj/obiekt/(?P<miejsce_id>[0-9]+)/$', views.dodaj_obiekt, name='dodaj_obiekt'),
    url(r'^dodaj/dopuszczenie/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.dodaj_dopuszczenie, name='dodaj_dopuszczenie'),
    url(r'^dodaj/przeglad/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.dodaj_przeglad, name='dodaj_przeglad'),
    url(r'^dodane/$', views.dodane, name='dodane'),
    url(r'^dopuszczenie/(?P<obiekt_id>[0-9]+)/archiwum/$', views.ArchiwumListView.as_view(), name='archiwum'),
    url(r'^dopuszczenie/archiwum/(?P<pk>[0-9]+)$', views.ArchiwumDetailView.as_view(), name='archiwum-detail'),
    url(r'^edytuj/obiekt/(?P<obiekt_id>[0-9]+)/$', views.edytuj_obiekt, name="edytuj_obiekt"),
    url(r'^edytuj/dopuszczenie(?P<obiekt_id>[0-9]+)/$', views.edytuj_dopuszczenie, name="edytuj_dopuszczenie"),
    url(r'^edytuj/miejsce(?P<miejsce_id>[0-9]+)/$', views.edytuj_miejsce, name="edytuj_miejsce"),
    url(r'^edytuj/przeglad(?P<obiekt_id>[0-9]+)/$', views.edytuj_przeglad, name="edytuj_przeglad"),
    url(r'^miejsca/(?P<miejsca>[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ0-9 _.-]+)/$', views.miejsca, name='miejsca'),
    url(r'^miejsce/(?P<miejsce_id>[0-9]+)/$', views.miejsce, name='miejsce'),
    url(r'^niedodane/$', views.niedodane, name='niedodane'),
    url(r'^obiekt/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.obiekt, name='obiekt'),
]