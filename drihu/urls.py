from django.urls import path
from drihu.views import *

urlpatterns = [
    path('session/', session, name='session'),
    path('admin/', admin,name='admin'),
    path('cerrar_session/',cerrar_session,name='cerrar_session'),
    path('wiki/',wiki,name='subir_wiki'),
]