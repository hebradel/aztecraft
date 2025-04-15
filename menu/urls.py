from django.contrib import admin
from django.urls import path
from menu.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('wiki/', wiki),
]