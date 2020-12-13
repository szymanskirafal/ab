from django.conf.urls import url


from .views import ZadanieCreateView, ZadanieDetailView, ZadanieUpdateView

urlpatterns = [
    url(r'^dodaj/(?P<dopuszczenie_id>[0-9]+)/$', ZadanieCreateView.as_view(), name='create'),
    url(r'(?P<pk>[0-9]+)/detail/$', ZadanieDetailView.as_view(), name='detail'),
    url(r'(?P<pk>[0-9]+)/update/$', ZadanieUpdateView.as_view(), name='update'),
    ]