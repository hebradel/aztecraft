from django.urls import *

urlpatterns = [
    path('menu/', include('menu.urls')),
    path('', include('inicio.urls')),
    path('admin/', include('drihu.urls')),
]