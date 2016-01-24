from django.conf.urls import url


from raporty import views

urlpatterns = [
    url(r'^$', views.raport, name='raport'),

]