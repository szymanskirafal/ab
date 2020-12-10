from django.conf.urls import url


from .views import ZadanieCreateView, ZadanieDetailView

urlpatterns = [
    url(r'^dodaj/(?P<dopuszczenie_id>[0-9]+)/$', ZadanieCreateView.as_view(), name='create'),
    url(r'(?P<zadanie_id>[0-9]+)/(?P<dopuszczenie_id>[0-9]+)/$', ZadanieDetailView.as_view(), name='detail'),
    ]