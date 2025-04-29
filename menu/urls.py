from django.contrib import admin
from django.urls import path
from menu.views import *

urlpatterns = [
    path('inicio/', inicio, name='Minicio'),
    path('wiki/', wiki,name='Mwiki'),
    path('wiki/<str:wiki>/', apartado,name='Mapartado'),
]