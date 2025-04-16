from django.shortcuts import *
from drihu.models import *
from django.contrib.auth.hashers import make_password, check_password

def session(request):
    if request.method == "POST":
        user=request.POST.get("user")
        password=request.POST.get("password")
        adm= Admin.objects.filter(usuario=user).first()
        if adm:
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

def admin(request):
    if not Admin.objects.filter(usuario=request.COOKIES.get('usuario')).first():
        return redirect('index')
    return render(request,'admin.html')