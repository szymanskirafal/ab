from django.conf.urls import url


from grupa import views

urlpatterns = [
    url(r'^$', views.grupy, name='grupy'),
    url(r'^grupa/nowa/$', views.nowa, name='nowa'),
    url(r'^grupa/created/(?P<group_name>[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ0-9 _.-]+)/$', views.group_created, name='group_created'),
    url(r'^created/add/(?P<group_name>[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ0-9 _.-]+)/$', views.add_member, name='add_member'),
    url(r'^created/member/(?P<group_name>[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ0-9 ]+)/(?P<member>[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ0-9 _.-]+)/$', views.member, name='member'),
    url(r'^grupa/group/(?P<group_name>[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ0-9 _.-]+)/$', views.group, name='group'),
]