from django.urls import *

urlpatterns = [
    path('menu/', include('menu.urls')),
]