<<<<<<< HEAD
from django.shortcuts import render
from .models import Profile, Friend

def index(request):
    user = request.user.profile
    friends = user.friends.all()
    context = {"user": user, "friends": friends}
    return render(request, 'tecnogurus/index.html', context)

def detail(request,pk):
    friend = Friend.object.get(profile_id=pk)
    context = {"friend": friend}
    return render(request, "tecnogurus/detail.html", context)
=======
from cgi import print_arguments
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Alumno, Curso
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
>>>>>>> prueba_luis
