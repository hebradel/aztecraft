from django.shortcuts import *
from drihu.models import *
from drihu.tests import *
from menu.models import *
from django.contrib.auth.hashers import make_password, check_password

def session(request):
    if Admin.objects.filter(usuario=request.COOKIES.get('usuario')).first():
        return redirect('admin')
    if request.method == "POST":
        user=request.POST.get("user")
        password=request.POST.get("password")
        print(user, password)
        adm= Admin.objects.filter(usuario=user).first()
        if adm:
            print('hola')
            if check_password(password,adm.password):
                response = redirect('admin')
                response.set_cookie('usuario', adm.usuario, max_age=3600)
                return response
        else:
            context={
                'mensaje':'usuario incorrecto',
            }
    context={
        'mensaje':'',
    }
    return render(request,'session.html',context)

def cerrar_session(request):
    response=redirect('session')
    response.delete_cookie('usuario')
    return response


def admin(request):
    if not Admin.objects.filter(usuario=request.COOKIES.get('usuario')).first():
        return redirect('index')
    context={
        'wiki':Wiki.objects.all(),
    }
    return render(request,'admin.html',context)

def wiki(request):
    veri(request)
    if request.method == "POST" and request.POST.get("wiki"):
        print(request.POST.get("wiki"))
        wi=Wiki(
            wiki=request.POST.get("wiki"),
            context=request.POST.get("texto")
            )
        wi.save()

    context={
        'wiki':Wiki.objects.all(),
    }
    return render(request,'wiki_subir.html',context)