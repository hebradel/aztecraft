from django.shortcuts import *
from menu.models import *

# Create your views here.
def inicio(request):

    context={
        'wiki':Wiki.objects.all(),
    }
    return render(request,'menu.html',context)

def wiki(request):
    
    context={
        'wiki':Wiki.objects.all(),
    }
    return render(request,'wiki.html',context)

def apartado(request,wiki):
    id=Wiki.objects.get(wiki=wiki)
    context={
        'wiki':Campo.objects.filter(wiki=id),
    }
    return render(request,'apartado.html',context)