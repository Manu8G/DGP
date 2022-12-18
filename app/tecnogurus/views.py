from cgi import print_arguments
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Alumno, Curso, Usuario, Tarea, ImageList, Image
from .forms import  modificarTareaForm, crearTareaForm, creaListaImagenesForm
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

def tarea(request, id_tarea):
    tarea=Tarea.objects.get(id_tarea=id_tarea)
    lista=ImageList.objects.get(id_image_list=tarea.image_list.id_image_list)
    Limages=lista.images_id.all()

    return render(request, 'tarea.html', {'tarea': tarea, 'Limages':Limages, 'id_image_list':tarea.image_list.id_image_list})

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


def modificarTarea(request, id_tarea):

    tarea=Tarea.objects.get(id_tarea=id_tarea)
    form=modificarTareaForm(tarea)
    
    if request.method == "POST":
        form = modificarTareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.save()
            return redirect("index")

    else:
        form = modificarTareaForm(instance=tarea)

    return render (request, "modificarTarea.html",{'form': form,'tarea':tarea,'id_tarea':id_tarea})
    

def duplicarTarea(request):
    if request.method == 'POST':
        msg = 'ok'
        arr = request.POST.getlist('borrar[]')
        a_dup = arr[0]
        tar = Tarea.objects.all()
        for t in tar:
            if t.id_tarea == a_dup:
                id = t.id_tarea+'_copia'
                tipo = t.tipo_tarea
                desc = t.descripcion
                id_image = t.id_image_list
                enc = t.encargado
                nueva = Tarea.objects.create(id_tarea=id, tipo_tarea=tipo, descripcion=desc, id_image_list=id_image, encargado=enc)
                return (request, "fin_tarea.html")

        return JsonResponse(a_dup, safe=False)


def listaTarea(request):
    tareas=Tarea.objects.all()
    return render(request, "listaTarea.html", {'tareas':tareas})
    

def listaImagenes(request, id_image_list):
    lista=ImageList.objects.get(id_image_list=id_image_list)
    Limages=lista.images_id.all()
    return render(request, "imagenesPaso.html", {'Limages':Limages, 'id_image_list':id_image_list})


def creaListaImagenes(request):

    if request.method == "POST":
        form = creaListaImagenesForm(request.POST, request.FILES)

        if form.is_valid():
            lista = form.save(commit=False)
            lista.save()
            form.save_m2m()
            return redirect("fin_tarea")

    else:
        form = creaListaImagenesForm()

    return render(request, "creaListaImagenes.html", {'form': form})


def editListaImagenes(request):
    lista = get_object_or_404(ImageList.objects.filter(id_image_list=request.GET.get('edit_lista')))
    
    if request.method == "POST":
        form = creaListaImagenesForm(request.POST, request.FILES, instance=lista)

        if form.is_valid():
            lista = form.save(commit=False)
            lista.save()
            form.save_m2m()

            return redirect('fin_tarea')

    else:
        form = creaListaImagenesForm(instance=lista)


    return render(request, "creaListaImagenes.html", {'form': form})


def crearTarea(request):
    form=crearTareaForm()
    if request.method == "POST":
        form = crearTareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.save()
            return redirect("index")

    else:
        form = crearTareaForm()

    return render(request, "crearTarea.html", {'form': form})
