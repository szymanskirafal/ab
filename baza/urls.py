from django.conf.urls import url


from baza import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^bazy/$', views.BazyListView.as_view(), name='bazy'),
    url(r'^stacje/$', views.StacjeListView.as_view(), name='stacje'),
    url(r'^dodaj/miejsce/$', views.dodaj_miejsce, name='dodaj_miejsce'),
    url(r'^dodaj/(?P<miejsce_id>[0-9]+)/obiekt/$', views.dodaj_obiekt, name='dodaj_obiekt'),
    url(r'^dodaj/dopuszczenie/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.dodaj_dopuszczenie, name='dodaj_dopuszczenie'),
    url(r'^dodaj/przeglad/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.dodaj_przeglad, name='dodaj_przeglad'),
    url(r'^dodaj/(?P<miejsce_id>[0-9]+)/obiekt/wybor-opcji/$', views.DodajObiektWyborOpcjiTemplateView.as_view(), name='dodaj_obiekt_wybor_opcji'),
    url(r'^dodaj/(?P<miejsce_id>[0-9]+)/obiekt/gotowy/$', views.DodajObiektGotowyCreateView.as_view(), name='dodaj_obiekt_gotowy'),
    url(r'^dodaj/(?P<miejsce_id>[0-9]+)/odmierzacz$', views.DodajOdmierzaczCreateView.as_view(), name='dodaj_odmierzacz'),
    url(r'^dodaj/(?P<miejsce_id>[0-9]+)/pawilon$', views.DodajPawilonCreateView.as_view(), name='dodaj_pawilon'),
    url(r'^dodaj/(?P<miejsce_id>[0-9]+)/zbiornik$', views.DodajZbiornikCreateView.as_view(), name='dodaj_zbiornik'),
    url(r'^dodane/$', views.dodane, name='dodane'),
    url(r'^dopuszczenie/(?P<pk>[0-9]+)/$', views.DopuszczenieDetailView.as_view(), name='dopuszczenie_detail'),
    url(r'^dopuszczenie/(?P<obiekt_id>[0-9]+)/archiwum/$', views.ArchiwumListView.as_view(), name='archiwum'),
    url(r'^dopuszczenie/archiwum/(?P<pk>[0-9]+)$', views.ArchiwumDetailView.as_view(), name='archiwum-detail'),
    url(r'^dopuszczenie/archiwum/(?P<pk>[0-9]+)/delete/$', views.ArchiwumDopuszczenieDeleteView.as_view(), name='archiwum-dopuszczenie-delete'),
    url(r'^edytuj/obiekt/(?P<obiekt_id>[0-9]+)/$', views.edytuj_obiekt, name="edytuj_obiekt"),
    url(r'^edytuj/dopuszczenie/(?P<obiekt_id>[0-9]+)/$', views.edytuj_dopuszczenie, name="edytuj_dopuszczenie"),
    url(r'^edytuj/miejsce(?P<miejsce_id>[0-9]+)/$', views.edytuj_miejsce, name="edytuj_miejsce"),
    url(r'^edytuj/przeglad/(?P<przeglad_id>[0-9]+)/$', views.edytuj_przeglad, name="edytuj_przeglad"),
    url(r'^miejsce/(?P<miejsce_id>[0-9]+)/$', views.miejsce, name='miejsce'),
    url(r'^niedodane/$', views.niedodane, name='niedodane'),
    url(r'^obiekt/(?P<miejsce_id>[0-9]+)/(?P<obiekt_id>[0-9]+)/$', views.obiekt, name='obiekt'),
    url(r'^przeglad/(?P<przeglad_id>[0-9]+)/archiwum/$', views.ArchiwumPrzegladListView.as_view(), name='archiwum-przeglad'),
    url(r'^przeglad/archiwum/(?P<pk>[0-9]+)$', views.ArchiwumPrzegladDetailView.as_view(), name='archiwum-przeglad-detail'),
    url(r'^przeglad/archiwum/(?P<pk>[0-9]+)/delete/$', views.ArchiwumPrzegladDeleteView.as_view(), name='archiwum-przeglad-delete'),
    url(r'^usuniete/$', views.usuniete, name='usuniete'),

]