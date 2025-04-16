from django.contrib import admin
from django.urls import path
from drihu.views import *

urlpatterns = [
    path('session/', session, name='session'),
    path('admin/', admin,name='admin'),
]