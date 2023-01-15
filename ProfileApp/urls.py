from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('test/',views.test,name='test'),
    path('firstweb/',views.firstweb, name='firstweb'),
    path('secondpage/',views.secondpage, name='secondpage'),
    path('thirdpage/',views.thirdpage, name='thirdpage'),
    path('hny/',views.hny, name='hny'),
]