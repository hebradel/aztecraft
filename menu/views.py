from django.shortcuts import *
from menu.models import *

# Create your views here.
def inicio(request):

    context={
        'wiki':Wiki.objects.all(),
    }
    return render(request,'menu.html',context)

def wiki(request):
    if request.method == "POST" and request.POST.get("wiki"):
        print(request.POST.get("wiki"))
        wi=Wiki(wiki=request.POST.get("wiki"))
        wi.save()
    
    context={
        'wiki':Wiki.objects.all(),
    }
    return render(request,'wiki.html',context)