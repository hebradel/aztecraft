from django.test import TestCase
from drihu.models import *
from django.shortcuts import *

# Create your tests here.
def veri(request):
    if not Admin.objects.filter(usuario=request.COOKIES.get('usuario')).first():
        return redirect('index')