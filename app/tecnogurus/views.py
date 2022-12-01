from cgi import print_arguments
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Alumno, Curso, Usuario, Tarea
import json

def index(request):
    context={}
    return render(request, "index.html", context)


def chat_rooms(request):
    usuario = request.user
    busqueda = Alumno.objects.filter(user=request.user)

    if busqueda:
        cursos = Curso.objects.filter(id_curso=busqueda[0].id_curso.id_curso)
        curso = cursos[0]
    else:
        curso = ""

    return render(request, "chat_rooms.html", {"curso": curso}) 


def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})


def login_picto(request):
    contra = Usuario.password
    user = Usuario.objects.all()
    users = Usuario.objects.all().count
    
    return render(request, 'login_picto.html', context={'contra':contra, 'user':user, 'users':users})


def request_login(request):
   return render(request, 'request_login.html')


def buscador(request):
    return render(request, 'buscador.html')


def login_ok(request):
    return render(request, 'login_ok.html')


def failed_login(request):
    return render(request, 'failed_login.html')


def prueba(request):
    if request.method == 'POST':
        arr = request.POST.getlist('arr[]')
        us = arr[0]
        prueba = ''
        cont = ''
        cont += arr[1]
        cont += arr[2]
        cont += arr[3]
        cont += arr[4]
        guardar = 'nok'

        user = Usuario.objects.all()
        for u in user:
            if u.usuario == us:
                prueba = 'perfect'
                if u.password == cont:
                    prueba = 'perfectx2'
                    JsonResponse(prueba, safe=False)
                
            else:
                prueba = 'fallo'

        
            
        return JsonResponse(prueba, safe=False)
    else:
        return JsonResponse(guardar, safe=False)

def borrar_tarea(request):
    msg1 = 'ok'
    if request.method == 'POST':
        arr = request.POST.getlist('borrar[]')
        a_borrar = arr[0]
        tar = Tarea.objects.all()
        for t in tar:
            if t.id_tarea == a_borrar:
                t.delete()

        return JsonResponse(a_borrar, safe=False)


def fin_tarea(request):
    num_tareas = Tarea.objects.all().count
    id_t = Tarea.id_tarea
    tarea_p = Tarea.objects.all()
    return render(
        request, 'fin_tarea.html', 
        context={'num_tareas':num_tareas, 'id_t':id_t, 'tarea_p':tarea_p}
    )
